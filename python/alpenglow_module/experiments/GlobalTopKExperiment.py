import alpenglow.Getter as rs
import alpenglow as prs


class GlobalTopKExperiment(prs.OnlineExperiment):
    def config(self, elems):
        proceeding_logger = rs.ProceedingLogger()
        proceeding_logger.set_data_iterator(elems['randomAccessIterator'])
        config = self.parameterDefaults(
            topK=100,
            minTime=0,
            seed=0,
            outFile=None,
            filters=[],
        )
        config['loggers'] = [proceeding_logger] if self.verbose else []

        model = rs.FactorModel(**self.parameterDefaults(
            begin_min=-0.01,
            begin_max=0.01,
            dimension=10,
            initialize_all=False,
        ))

        updater = rs.FactorModelGradientUpdater(**self.parameterDefaults(
            learning_rate=0.05,
            regularization_rate=0.0
        ))
        updater.set_model(model)

        learner = rs.ImplicitGradientLearner()
        learner.set_train_matrix(elems['trainMatrix'])
        learner.add_gradient_updater(updater)
        learner.set_model(model)

        negative_sample_generator = rs.UniformNegativeSampleGenerator(**self.parameterDefaults(
            negative_rate=0.0,
            initialize_all=False,
            seed=0,
        ))
        negative_sample_generator.set_train_matrix(elems['trainMatrix'])
        negative_sample_generator.set_items(elems['items'])
        learner.set_negative_sample_generator(negative_sample_generator)

        pointWise = rs.ObjectiveMSE()
        gradient_computer = rs.GradientComputerPointWise(pointWise)
        gradient_computer.set_model(model)
        learner.set_gradient_computer(gradient_computer)

        fmfilter = rs.FactorModelFilter()
        fmfilter.setModel(model)
        fmfilter.setUsers(elems['users'])
        fmfilter.setItems(elems['items'])

        prediction_creator = rs.PredictionCreatorGlobal(**self.parameterDefaults(
            topK=10000,
            # initialThreshold=1000,
            lookback=0
        ))
        prediction_creator.setModel(model)
        prediction_creator.setFilter(fmfilter)
        online_predictor = rs.OnlinePredictor(**self.parameterDefaults(
            minTime=0,
            timeFrame=86400,
            fileName=""
        ))
        online_predictor.setPredictionCreator(prediction_creator)

        config['loggers'].append(online_predictor)

        return {
            'config': config,
            'model': model,
            'learner': learner
        }
