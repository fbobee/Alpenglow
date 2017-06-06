import alpenglow as prs
import alpenglow.Getter as rs
import alpenglow.experiments
import pandas as pd
import math


class TestSimulatedBatchExperiment:
    def test_simulatedBatchExperiment(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_4",
            sep=' ',
            header=None,
            names=['time', 'user', 'item', 'id', 'score', 'eval']
        )
        sbExperiment = alpenglow.experiments.SimulatedBatchExperiment(
            top_k=100,
            seed=254938879,
            period_length=1000
        )
        rankings = sbExperiment.run(data, verbose=True)
        assert rankings.top_k == 100
        assert [i.rank for i in rankings.logs] == [102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 36, 30, 53, 14, 56, 0, 102, 102, 102, 102, 91, 102, 58, 102, 10, 102, 72, 45, 102, 102, 57, 97, 30, 17, 102, 102, 30, 89, 67, 12, 102, 21, 102, 61, 6, 17, 26, 77, 48, 100, 102, 102, 102, 102, 102, 100, 91, 102, 102, 99, 97, 100, 31, 102, 6, 11, 74, 10, 102, 102, 36, 102, 85, 10, 6, 102, 10, 12, 28, 26, 25, 2, 102, 102, 28, 102, 102, 102, 102, 100, 84, 2, 102, 102, 82, 102, 10, 32, 102, 91, 96, 76, 100, 2, 19, 102, 102, 102, 100, 102, 102, 11, 102, 44, 75, 102, 102, 102, 102, 0, 100, 102, 102, 102, 6, 100, 27, 102, 102, 102, 102, 102, 102, 102, 102, 100, 102, 33, 102, 23, 1, 102, 102, 100, 1, 39, 100, 26, 102, 24, 12, 102, 37, 102, 102, 8, 39, 3, 88, 102, 2, 100, 102, 27, 102, 102, 102, 16, 15, 97, 102, 5, 102, 30, 102, 102, 102, 100, 100, 31, 100, 102, 102, 102, 15, 21, 102, 100, 96, 102, 100, 100, 102, 102, 100, 102, 20, 100, 102, 40, 100, 102, 11, 43, 100, 2, 19, 3, 102, 102, 100, 17, 102, 100, 102, 63, 102, 49, 91, 17, 102, 102, 49, 102, 102, 22, 102, 102, 102, 102, 102, 41, 39, 55, 24, 82, 102, 55, 30, 92, 102, 92, 102, 1, 102, 11, 73, 74, 102, 102, 102, 102, 102, 8, 24, 100, 7, 10, 83, 1, 4, 0, 49, 12, 13, 49, 29, 83, 55, 76, 102, 1, 91, 102, 100, 59, 18, 36, 100, 52, 71, 46, 9, 100, 8, 3, 102, 0, 102, 75, 102, 52, 102, 48, 30, 102, 102, 102, 3, 102, 62, 100, 97, 75, 61, 102, 100, 11, 17, 13, 102, 102, 85, 100, 102, 45, 28, 102, 56, 18, 3, 72, 62, 102, 26, 60, 1, 98, 85, 0, 100, 63, 13, 88, 100, 102, 102, 18, 5, 15, 7, 102, 102, 10, 102, 84, 41, 102, 21, 102, 102, 89, 17, 102, 29, 54, 29, 98, 102, 102, 100, 89, 50, 3, 102, 16, 102, 47, 37, 44, 20, 102, 102, 42, 70, 93, 102, 100, 102, 100, 102, 17, 102, 44, 102, 33, 1, 13, 53, 102, 100, 102, 100, 62, 102, 102, 17, 100, 12, 102, 100, 29, 51, 100, 102, 99, 102, 102, 14, 102, 10, 2, 19, 14, 14, 4, 13, 102, 0, 102, 14, 46, 23, 26, 12, 5, 102, 56, 102, 8, 102, 102, 49, 29, 19, 20, 102, 15, 100, 14, 0, 6, 100, 32, 61, 34, 100, 2, 15, 7, 102, 102, 9, 102, 102, 17, 102, 8, 22, 102, 102, 100, 17, 46, 21, 100, 102, 20, 30, 102, 2, 102, 31, 42, 27, 38, 28, 1, 31, 6, 1, 20, 102, 13, 17, 3, 100, 2, 33, 5, 50, 7, 1, 29, 102, 25, 25, 102, 14, 102, 71, 2, 75, 13, 102, 65, 1, 1, 21, 48, 58, 40, 100, 10, 102, 102, 0, 7, 102, 3, 100, 14, 102, 20, 31, 30, 12, 102, 4, 102, 102, 35, 19, 100, 100, 102, 2, 3, 4, 102, 17, 10, 8, 3, 14, 19, 23, 23, 18, 100, 63, 28, 11, 40, 3, 0, 100, 102, 46, 14, 22, 0, 37, 102, 2, 0, 100, 47, 19, 28, 1, 100, 102, 23, 4, 14, 0, 102, 14, 33, 102, 102, 1, 36, 12, 15, 15, 6, 102, 1, 18, 2, 15, 102, 102, 56, 48, 61, 102, 13, 14, 100, 95, 22, 1, 102, 9, 8, 100, 100, 29, 15, 2, 0, 12, 24, 7, 2, 100, 18, 2, 100, 0, 0, 25, 100, 0, 38, 50, 5, 24, 0, 102, 102, 100, 102, 102, 11, 11, 2, 102, 5, 32, 20, 13, 100, 3, 80, 25, 102, 35, 100, 102, 102, 8, 5, 7, 16, 102, 100, 19, 19, 29, 9, 1, 55, 8, 21, 100, 102, 100, 100, 102, 102, 16, 15, 27, 15, 23, 102, 5, 17, 19, 102, 30, 8, 0, 10, 34, 18, 6, 3, 46, 8, 102, 100, 39, 5, 16, 1, 102, 10, 5, 5, 102, 20, 7, 5, 28, 100, 49, 102, 17, 8, 22, 102, 24, 102, 100, 18, 7, 16, 16, 33, 102, 7, 94, 102, 100, 102, 102, 27, 20, 14, 102, 44, 1, 100, 8, 102, 12, 2, 4, 13, 100, 102, 100, 34, 102, 102, 8, 102, 15, 102, 11, 12, 0, 17, 3, 35, 0, 100, 100, 3, 21, 5, 3, 102, 18, 47, 102, 7, 5, 26, 0, 39, 100, 14, 2, 25, 100, 11, 32, 13, 0, 58, 0, 8, 36, 23, 102, 1, 7, 16, 54, 2, 0, 102, 0, 2, 62, 100, 10, 21, 26, 41, 100, 100, 102]