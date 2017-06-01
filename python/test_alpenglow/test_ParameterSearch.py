import alpenglow as prs
import alpenglow.Getter as rs
import alpenglow.experiments
import pandas as pd
import math
import unittest


class TestParameterSearch(unittest.TestCase):
    def test__getConfigurations(self):
        c = prs.ParameterSearch(None, None)
        c.set_parameterValues('negative_rate', [1, 2, 3])
        c.set_parameterValues('learning_rate', [0.05, 0.1])

        params = c._getConfigurations()
        self.assertCountEqual(params, [
            {'negative_rate': 1, 'learning_rate': 0.05},
            {'negative_rate': 1, 'learning_rate': 0.1},
            {'negative_rate': 2, 'learning_rate': 0.05},
            {'negative_rate': 2, 'learning_rate': 0.1},
            {'negative_rate': 3, 'learning_rate': 0.05},
            {'negative_rate': 3, 'learning_rate': 0.1},
        ])

    def test_runOneConfig(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_4",
            sep=' ',
            header=None,
            names=['time', 'user', 'item', 'id', 'score', 'eval']
        )
        model = alpenglow.experiments.PopularityModelExperiment(
            top_k=100,
            seed=254938879
        )
        c = prs.ParameterSearch(model, prs.NdcgScore)
        r = c.run(data)
        ranks = [102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 4, 102, 102, 1, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 0, 102, 102, 2, 102, 102, 12, 0, 102, 102, 102, 27, 22, 102, 102, 102, 102, 102, 6, 1, 2, 102, 102, 3, 2, 10, 12, 102, 102, 8, 102, 30, 102, 102, 102, 102, 102, 102, 18, 102, 0, 2, 9, 102, 102, 10, 102, 102, 102, 6, 102, 2, 102, 6, 102, 102, 13, 0, 102, 1, 0, 102, 15, 42, 102, 102, 102, 102, 13, 102, 47, 9, 3, 14, 102, 55, 7, 27, 1, 102, 6, 26, 102, 102, 102, 4, 5, 5, 0, 102, 4, 0, 102, 102, 5, 1, 10, 102, 102, 13, 3, 28, 102, 12, 16, 19, 50, 10, 18, 2, 102, 2, 102, 102, 17, 15, 46, 14, 2, 5, 1, 43, 4, 47, 102, 0, 102, 0, 5, 44, 10, 80, 102, 9, 4, 54, 10, 2, 102, 3, 102, 102, 10, 2, 102, 102, 102, 17, 102, 4, 5, 102, 2, 102, 102, 70, 26, 22, 102, 102, 16, 102, 3, 102, 10, 4, 24, 1, 102, 5, 16, 19, 102, 3, 19, 15, 4, 25, 13, 102, 102, 102, 102, 13, 102, 7, 3, 0, 102, 3, 11, 102, 1, 0, 2, 77, 12, 102, 102, 14, 89, 11, 3, 19, 14, 102, 0, 8, 16, 67, 2, 7, 20, 102, 102, 102, 102, 102, 0, 14, 102, 53, 62, 3, 1, 6, 102, 91, 3, 7, 27, 102, 102, 35, 13, 1, 7, 12, 102, 2, 87, 34, 2, 0, 9, 102, 79, 13, 102, 102, 9, 17, 6, 40, 10, 102, 102, 49, 102, 23, 66, 102, 1, 90, 5, 1, 0, 13, 102, 1, 102, 5, 6, 100, 13, 16, 2, 41, 102, 102, 102, 102, 0, 10, 100, 6, 8, 8, 28, 26, 102, 102, 102, 102, 4, 102, 0, 102, 37, 102, 5, 102, 20, 1, 35, 7, 100, 7, 4, 9, 1, 102, 100, 4, 102, 2, 7, 86, 0, 1, 1, 31, 7, 1, 4, 102, 3, 102, 6, 15, 21, 0, 35, 6, 19, 102, 0, 86, 5, 102, 8, 2, 11, 100, 19, 4, 102, 0, 3, 102, 0, 23, 102, 2, 3, 102, 20, 85, 13, 6, 96, 53, 1, 2, 102, 47, 12, 27, 17, 36, 100, 9, 102, 83, 11, 102, 46, 3, 18, 39, 26, 100, 14, 102, 102, 6, 6, 102, 7, 102, 102, 102, 102, 102, 3, 4, 100, 3, 24, 102, 37, 35, 22, 102, 19, 102, 3, 102, 6, 46, 40, 102, 2, 13, 102, 7, 14, 16, 100, 0, 2, 39, 0, 6, 0, 2, 19, 20, 8, 42, 42, 11, 26, 102, 30, 50, 102, 6, 14, 32, 13, 87, 51, 96, 19, 1, 33, 0, 1, 102, 0, 102, 8, 102, 35, 30, 100, 9, 102, 102, 102, 1, 102, 100, 46, 100, 100, 3, 102, 60, 3, 46, 15, 102, 102, 29, 100, 102, 9, 14, 8, 21, 15, 2, 38, 100, 102, 0, 100, 5, 82, 74, 1, 100, 58, 4, 26, 49, 102, 100, 16, 1, 4, 11, 15, 102, 0, 13, 27, 8, 102, 2, 102, 102, 22, 3, 102, 4, 15, 43, 100, 102, 38, 30, 100, 7, 1, 8, 4, 6, 1, 34, 5, 10, 102, 65, 59, 25, 20, 2, 100, 102, 65, 102, 5, 18, 25, 102, 3, 0, 42, 2, 102, 54, 102, 37, 34, 102, 102, 25, 19, 38, 102, 9, 12, 100, 100, 102, 100, 8, 102, 2, 4, 7, 3, 14, 4, 10, 0, 19, 102, 2, 102, 9, 55, 19, 16, 28, 8, 102, 90, 102, 10, 4, 102, 52, 8, 12, 25, 102, 15, 64, 9, 0, 5, 61, 17, 100, 35, 100, 1, 21, 4, 13, 2, 5, 102, 102, 17, 102, 6, 20, 0, 102, 89, 12, 37, 30, 100, 102, 20, 34, 102, 0, 102, 18, 33, 33, 12, 43, 4, 5, 4, 0, 12, 102, 30, 15, 0, 100, 0, 37, 3, 34, 12, 0, 6, 102, 29, 18, 102, 26, 102, 83, 2, 100, 12, 102, 44, 4, 2, 6, 41, 56, 61, 44, 14, 2, 102, 0, 4, 6, 4, 100, 14, 102, 22, 18, 14, 10, 3, 9, 102, 102, 32, 20, 66, 100, 102, 2, 1, 0, 102, 18, 17, 14, 5, 28, 25, 12, 27, 12, 100, 100, 28, 16, 59, 7, 0, 100, 102, 77, 24, 15, 1, 15, 102, 2, 0, 100, 34, 2, 25, 0, 100, 102, 29, 2, 21, 1, 102, 25, 32, 102, 102, 0, 40, 14, 10, 11, 6, 102, 6, 11, 0, 17, 102, 100, 70, 49, 38, 102, 6, 8, 48, 84, 26, 2, 6, 16, 5, 34, 61, 18, 10, 2, 2, 7, 24, 7, 2, 100, 11, 3, 64, 0, 3, 31, 100, 0, 23, 77, 2, 25, 0, 7, 102, 100, 102, 102, 10, 19, 2, 102, 6, 21, 14, 19, 75, 3, 100, 30, 11, 55, 100, 102, 102, 4, 8, 6, 10, 102, 45, 17, 20, 23, 9, 2, 55, 8, 27, 66, 102, 100, 38, 3, 1, 11, 16, 27, 25, 39, 102, 1, 20, 29, 102, 24, 7, 1, 11, 36, 13, 11, 4, 43, 6, 6, 63, 36, 4, 17, 0, 102, 16, 10, 6, 102, 17, 4, 5, 24, 100, 46, 102, 11, 8, 29, 102, 34, 102, 99, 19, 7, 18, 19, 27, 102, 11, 100, 100, 59, 0, 102, 19, 21, 12, 102, 53, 1, 100, 10, 102, 18, 0, 6, 23, 100, 102, 27, 35, 102, 102, 10, 102, 18, 102, 10, 9, 2, 1, 1, 21, 0, 31, 91, 3, 32, 14, 17, 102, 13, 81, 102, 17, 7, 38, 1, 37, 100, 19, 1, 31, 28, 22, 40, 13, 1, 85, 0, 12, 33, 13, 102, 1, 7, 9, 65, 14, 1, 9, 0, 0, 51, 85, 9, 22, 25, 27, 100, 100, 102]
        ndcgs = [math.log(2) / math.log(r + 2) if r < 100 else 0 for r in ranks]
        print(r)
        assert r['NdcgScore'][0] - sum(ndcgs) / len(ndcgs) < 0.000000001

    def test_runMultiple(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_4",
            sep=' ',
            header=None,
            names=['time', 'user', 'item', 'id', 'score', 'eval']
        )
        model = alpenglow.experiments.PopularityModelExperiment(
            top_k=100,
            seed=254938879
        )
        c = prs.ParameterSearch(model, prs.NdcgScore)
        c.set_parameterValues('top_k', [100, 50])
        c.set_parameterValues('seed', [254938879, 0])
        r = c.run(data)
        assert len(r) == 4

        ranks = [102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 4, 102, 102, 1, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 0, 102, 102, 2, 102, 102, 12, 0, 102, 102, 102, 27, 22, 102, 102, 102, 102, 102, 6, 1, 2, 102, 102, 3, 2, 10, 12, 102, 102, 8, 102, 30, 102, 102, 102, 102, 102, 102, 18, 102, 0, 2, 9, 102, 102, 10, 102, 102, 102, 6, 102, 2, 102, 6, 102, 102, 13, 0, 102, 1, 0, 102, 15, 42, 102, 102, 102, 102, 13, 102, 47, 9, 3, 14, 102, 55, 7, 27, 1, 102, 6, 26, 102, 102, 102, 4, 5, 5, 0, 102, 4, 0, 102, 102, 5, 1, 10, 102, 102, 13, 3, 28, 102, 12, 16, 19, 50, 10, 18, 2, 102, 2, 102, 102, 17, 15, 46, 14, 2, 5, 1, 43, 4, 47, 102, 0, 102, 0, 5, 44, 10, 80, 102, 9, 4, 54, 10, 2, 102, 3, 102, 102, 10, 2, 102, 102, 102, 17, 102, 4, 5, 102, 2, 102, 102, 70, 26, 22, 102, 102, 16, 102, 3, 102, 10, 4, 24, 1, 102, 5, 16, 19, 102, 3, 19, 15, 4, 25, 13, 102, 102, 102, 102, 13, 102, 7, 3, 0, 102, 3, 11, 102, 1, 0, 2, 77, 12, 102, 102, 14, 89, 11, 3, 19, 14, 102, 0, 8, 16, 67, 2, 7, 20, 102, 102, 102, 102, 102, 0, 14, 102, 53, 62, 3, 1, 6, 102, 91, 3, 7, 27, 102, 102, 35, 13, 1, 7, 12, 102, 2, 87, 34, 2, 0, 9, 102, 79, 13, 102, 102, 9, 17, 6, 40, 10, 102, 102, 49, 102, 23, 66, 102, 1, 90, 5, 1, 0, 13, 102, 1, 102, 5, 6, 100, 13, 16, 2, 41, 102, 102, 102, 102, 0, 10, 100, 6, 8, 8, 28, 26, 102, 102, 102, 102, 4, 102, 0, 102, 37, 102, 5, 102, 20, 1, 35, 7, 100, 7, 4, 9, 1, 102, 100, 4, 102, 2, 7, 86, 0, 1, 1, 31, 7, 1, 4, 102, 3, 102, 6, 15, 21, 0, 35, 6, 19, 102, 0, 86, 5, 102, 8, 2, 11, 100, 19, 4, 102, 0, 3, 102, 0, 23, 102, 2, 3, 102, 20, 85, 13, 6, 96, 53, 1, 2, 102, 47, 12, 27, 17, 36, 100, 9, 102, 83, 11, 102, 46, 3, 18, 39, 26, 100, 14, 102, 102, 6, 6, 102, 7, 102, 102, 102, 102, 102, 3, 4, 100, 3, 24, 102, 37, 35, 22, 102, 19, 102, 3, 102, 6, 46, 40, 102, 2, 13, 102, 7, 14, 16, 100, 0, 2, 39, 0, 6, 0, 2, 19, 20, 8, 42, 42, 11, 26, 102, 30, 50, 102, 6, 14, 32, 13, 87, 51, 96, 19, 1, 33, 0, 1, 102, 0, 102, 8, 102, 35, 30, 100, 9, 102, 102, 102, 1, 102, 100, 46, 100, 100, 3, 102, 60, 3, 46, 15, 102, 102, 29, 100, 102, 9, 14, 8, 21, 15, 2, 38, 100, 102, 0, 100, 5, 82, 74, 1, 100, 58, 4, 26, 49, 102, 100, 16, 1, 4, 11, 15, 102, 0, 13, 27, 8, 102, 2, 102, 102, 22, 3, 102, 4, 15, 43, 100, 102, 38, 30, 100, 7, 1, 8, 4, 6, 1, 34, 5, 10, 102, 65, 59, 25, 20, 2, 100, 102, 65, 102, 5, 18, 25, 102, 3, 0, 42, 2, 102, 54, 102, 37, 34, 102, 102, 25, 19, 38, 102, 9, 12, 100, 100, 102, 100, 8, 102, 2, 4, 7, 3, 14, 4, 10, 0, 19, 102, 2, 102, 9, 55, 19, 16, 28, 8, 102, 90, 102, 10, 4, 102, 52, 8, 12, 25, 102, 15, 64, 9, 0, 5, 61, 17, 100, 35, 100, 1, 21, 4, 13, 2, 5, 102, 102, 17, 102, 6, 20, 0, 102, 89, 12, 37, 30, 100, 102, 20, 34, 102, 0, 102, 18, 33, 33, 12, 43, 4, 5, 4, 0, 12, 102, 30, 15, 0, 100, 0, 37, 3, 34, 12, 0, 6, 102, 29, 18, 102, 26, 102, 83, 2, 100, 12, 102, 44, 4, 2, 6, 41, 56, 61, 44, 14, 2, 102, 0, 4, 6, 4, 100, 14, 102, 22, 18, 14, 10, 3, 9, 102, 102, 32, 20, 66, 100, 102, 2, 1, 0, 102, 18, 17, 14, 5, 28, 25, 12, 27, 12, 100, 100, 28, 16, 59, 7, 0, 100, 102, 77, 24, 15, 1, 15, 102, 2, 0, 100, 34, 2, 25, 0, 100, 102, 29, 2, 21, 1, 102, 25, 32, 102, 102, 0, 40, 14, 10, 11, 6, 102, 6, 11, 0, 17, 102, 100, 70, 49, 38, 102, 6, 8, 48, 84, 26, 2, 6, 16, 5, 34, 61, 18, 10, 2, 2, 7, 24, 7, 2, 100, 11, 3, 64, 0, 3, 31, 100, 0, 23, 77, 2, 25, 0, 7, 102, 100, 102, 102, 10, 19, 2, 102, 6, 21, 14, 19, 75, 3, 100, 30, 11, 55, 100, 102, 102, 4, 8, 6, 10, 102, 45, 17, 20, 23, 9, 2, 55, 8, 27, 66, 102, 100, 38, 3, 1, 11, 16, 27, 25, 39, 102, 1, 20, 29, 102, 24, 7, 1, 11, 36, 13, 11, 4, 43, 6, 6, 63, 36, 4, 17, 0, 102, 16, 10, 6, 102, 17, 4, 5, 24, 100, 46, 102, 11, 8, 29, 102, 34, 102, 99, 19, 7, 18, 19, 27, 102, 11, 100, 100, 59, 0, 102, 19, 21, 12, 102, 53, 1, 100, 10, 102, 18, 0, 6, 23, 100, 102, 27, 35, 102, 102, 10, 102, 18, 102, 10, 9, 2, 1, 1, 21, 0, 31, 91, 3, 32, 14, 17, 102, 13, 81, 102, 17, 7, 38, 1, 37, 100, 19, 1, 31, 28, 22, 40, 13, 1, 85, 0, 12, 33, 13, 102, 1, 7, 9, 65, 14, 1, 9, 0, 0, 51, 85, 9, 22, 25, 27, 100, 100, 102]
        ndcgs = [math.log(2) / math.log(r + 2) if r < 100 else 0 for r in ranks]

        hit = 0
        for (k, s, v) in r.values:
            if k == 100 and s == 254938879:
                self.assertAlmostEqual(v, sum(ndcgs) / len(ndcgs))
                hit += 1
        assert hit == 1
