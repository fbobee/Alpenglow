#ifndef PERIODIC_LEARNER
#define PERIODIC_LEARNER

#include <string>
#include <gtest/gtest_prod.h>
#include "../models/ModelUpdater.h"
#include "../models/GroupUpdater.h"
#include "../recommender_data/RecommenderDataIterator.h"
#include "../general_interfaces/INeedExperimentEnvironment.h"
#include "../general_interfaces/Initializable.h"
#include "../general_interfaces/Updater.h"

struct PeriodicLearnerParameters{
  int period_length;
  int start_time;
  bool read_model;
  bool write_model;
  string base_in_file_name;
  string base_out_file_name;
  bool clear_model;
  //bool learn;
  string mode;
  int samplenum_in_periods;
};

class PeriodicLearner : public Updater,  public Initializable, public INeedExperimentEnvironment {
  public:
    PeriodicLearner(PeriodicLearnerParameters* params){
      start_time_ = params->start_time;
      period_length_ = params->period_length;
      read_model_ = params->read_model;
      write_model_ = params->write_model;
      clear_model_ = params->clear_model;
      base_in_file_name_ = params->base_in_file_name;
      base_out_file_name_ = params->base_out_file_name;
      mode_ = (params->mode==""?"time-based":params->mode);
      samplenum_in_periods_ = params->samplenum_in_periods;
      period_num_ = 0;
      model_ = NULL;
      recommender_data_ = NULL;
      end_period_num_ = -1;
    }
    virtual ~PeriodicLearner(){}
    void update(RecDat* rec_dat) override;
    void set_recommender_data_iterator(RecommenderDataIterator* recommender_data){ recommender_data_ = recommender_data; }
    void set_experiment_environment(ExperimentEnvironment* experiment_environment) override {
      experiment_environment_=experiment_environment;
    }
    void add_simple_updater(ModelSimpleUpdater* model_updater) {
      model_simple_updaters_.push_back(model_updater);
    }
    void add_gradient_updater(ModelGradientUpdater* model_updater) {
      model_gradient_updaters_.push_back(model_updater);
    }
    void add_multi_updater(ModelMultiUpdater* model_updater) {
      model_multi_updaters_.push_back(model_updater);
    }
    virtual void set_model(Model* model){model_=model;}
    bool self_test(){
      bool ok = Updater::self_test();
      if(mode_!="time-based" and mode_!="samplenum-based"){ cerr << "PeriodicLearner::mode should be time-based or samplenum-based." << endl; ok=false; }
      if(mode_ == "time-based" and period_length_<=0){ cerr << "PeriodicLearner::period_length_ oops." << endl; ok = false; }
      if(recommender_data_==NULL){ cerr << "PeriodicLearner::recommender_data_ oops." << endl; ok=false; }
      if(model_==NULL && (read_model_ || write_model_ || clear_model_)){ cerr << "PeriodicLearner::model_ oops." << endl; ok = false; }
      return ok;
    }
  protected:
    bool autocalled_initialize() override;
    int compute_next_period_num(RecDat*);
    const RecommenderDataIterator* recommender_data_;
    ExperimentEnvironment* experiment_environment_;
    int start_time_;
    int period_length_;
    bool read_model_;
    bool clear_model_;
    bool write_model_;
    string base_in_file_name_;
    string base_out_file_name_;
    int period_num_;
    string mode_;
    int samplenum_in_periods_;
    int end_period_num_;
    vector<ModelSimpleUpdater*> model_simple_updaters_;
    vector<ModelGradientUpdater*> model_gradient_updaters_;
    vector<ModelMultiUpdater*> model_multi_updaters_;
    Model* model_;
    FRIEND_TEST(TestPeriodicLearner, test_periodic);
  private: //in c++, it is possible to override private virtual functions
    virtual void read_model(RecDat*);
    virtual void clear_model(RecDat*);
    virtual void write_model(RecDat*);
    virtual void update_model(RecDat*){}

};

#endif
