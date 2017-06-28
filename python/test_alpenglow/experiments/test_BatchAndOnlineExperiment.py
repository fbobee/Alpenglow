import alpenglow as prs
import alpenglow.Getter as rs
import alpenglow.experiments
import pandas as pd
import math


class TestBatchAndOnlineExperiment:
    def test_batchAndOnlineExperiment(self):
        boModelExperiment = alpenglow.experiments.BatchAndOnlineExperiment(
            top_k=100,
            seed=254938879,
            dimension=10,
            period_length=1000,
            batch_learning_rate=0.07,
            batch_negative_rate=20,
            online_learning_rate=0.15,
            online_negative_rate=120,
            number_of_iterations=3,
            clear_model=True,
        )
        boRankings = boModelExperiment.run("python/test_alpenglow/test_data_4", experimentType="online_id", verbose=True)
        assert boRankings.top_k == 100
        assert [i.rank for i in boRankings.logs] == [102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 2, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 4, 102, 102, 1, 102, 102, 102, 102, 102, 102, 102, 0, 102, 102, 102, 102, 102, 102, 102, 102, 2, 102, 102, 102, 25, 18, 29, 102, 102, 11, 102, 20, 102, 102, 102, 102, 102, 102, 19, 102, 22, 37, 39, 102, 102, 102, 102, 102, 102, 11, 102, 3, 102, 25, 102, 102, 102, 56, 102, 102, 34, 102, 43, 54, 102, 102, 102, 102, 102, 102, 56, 102, 5, 43, 102, 61, 56, 48, 11, 102, 102, 46, 102, 102, 102, 64, 33, 9, 21, 102, 59, 2, 102, 102, 20, 71, 102, 102, 102, 0, 71, 32, 102, 12, 62, 16, 29, 0, 12, 7, 102, 15, 102, 102, 63, 65, 67, 102, 57, 25, 33, 13, 24, 38, 102, 47, 102, 102, 6, 102, 31, 71, 102, 48, 60, 13, 4, 57, 102, 73, 102, 102, 23, 102, 102, 102, 102, 60, 102, 4, 70, 102, 102, 102, 102, 82, 43, 45, 102, 102, 19, 102, 65, 102, 40, 73, 57, 66, 102, 102, 86, 32, 102, 41, 64, 38, 14, 19, 6, 102, 102, 102, 102, 57, 102, 56, 102, 6, 102, 95, 5, 102, 102, 24, 40, 39, 31, 102, 102, 96, 18, 26, 85, 102, 8, 102, 10, 68, 15, 19, 8, 8, 14, 102, 102, 102, 102, 102, 53, 68, 102, 8, 13, 100, 44, 78, 102, 34, 51, 17, 97, 102, 102, 2, 102, 26, 85, 81, 102, 30, 77, 3, 100, 54, 13, 102, 100, 15, 102, 102, 102, 102, 16, 79, 12, 102, 102, 100, 102, 84, 49, 102, 56, 63, 47, 100, 32, 10, 102, 102, 102, 33, 102, 26, 10, 102, 100, 36, 102, 102, 102, 102, 35, 71, 65, 86, 11, 4, 32, 80, 102, 102, 102, 102, 78, 102, 76, 102, 30, 102, 84, 102, 12, 48, 63, 102, 22, 100, 100, 45, 15, 102, 32, 11, 102, 50, 102, 100, 27, 38, 7, 100, 102, 11, 100, 102, 61, 102, 2, 33, 93, 45, 95, 0, 17, 102, 25, 30, 102, 102, 21, 100, 42, 100, 102, 102, 102, 1, 66, 102, 52, 95, 102, 53, 3, 102, 100, 61, 88, 86, 100, 40, 31, 90, 102, 31, 39, 100, 52, 79, 18, 102, 102, 97, 17, 102, 3, 102, 37, 102, 94, 100, 46, 102, 102, 10, 24, 102, 28, 102, 102, 102, 102, 102, 2, 6, 34, 35, 19, 102, 100, 32, 68, 102, 91, 102, 0, 102, 6, 28, 100, 102, 102, 10, 102, 14, 58, 9, 100, 18, 42, 26, 77, 39, 0, 56, 57, 100, 18, 11, 16, 100, 68, 102, 55, 100, 102, 100, 14, 60, 34, 61, 46, 78, 38, 8, 100, 3, 12, 102, 0, 102, 91, 102, 87, 102, 100, 1, 102, 102, 102, 1, 102, 100, 84, 100, 99, 0, 102, 83, 2, 100, 12, 102, 102, 1, 100, 102, 11, 48, 100, 22, 7, 3, 56, 100, 102, 0, 100, 19, 48, 100, 20, 41, 33, 33, 10, 11, 102, 43, 16, 100, 72, 21, 102, 102, 0, 102, 75, 3, 102, 0, 102, 102, 12, 9, 102, 22, 2, 76, 100, 102, 102, 9, 100, 5, 8, 102, 22, 100, 33, 78, 26, 29, 102, 25, 59, 57, 69, 100, 63, 102, 70, 102, 12, 102, 44, 102, 12, 2, 69, 8, 102, 100, 102, 100, 41, 102, 102, 100, 55, 100, 102, 93, 17, 100, 96, 102, 48, 23, 102, 15, 102, 1, 0, 26, 11, 11, 2, 3, 102, 1, 102, 12, 100, 17, 8, 30, 1, 102, 27, 102, 21, 102, 102, 100, 11, 100, 30, 102, 12, 100, 12, 0, 100, 26, 100, 84, 100, 63, 49, 40, 39, 102, 102, 100, 102, 102, 100, 102, 43, 100, 102, 102, 100, 35, 7, 73, 100, 102, 15, 74, 102, 0, 102, 5, 61, 15, 0, 36, 8, 4, 9, 3, 48, 102, 24, 42, 2, 82, 31, 46, 25, 100, 100, 0, 4, 102, 72, 39, 102, 39, 102, 100, 22, 100, 6, 102, 43, 100, 100, 4, 100, 8, 25, 100, 16, 102, 102, 15, 17, 102, 8, 100, 56, 102, 11, 12, 9, 8, 100, 69, 102, 102, 66, 48, 27, 36, 102, 5, 100, 1, 102, 17, 59, 35, 10, 31, 100, 7, 100, 12, 48, 68, 31, 100, 42, 5, 40, 100, 102, 56, 74, 100, 0, 6, 102, 11, 0, 100, 15, 0, 38, 0, 100, 102, 37, 100, 17, 4, 102, 82, 12, 102, 102, 0, 38, 12, 14, 26, 13, 102, 15, 30, 7, 83, 102, 27, 100, 66, 25, 102, 13, 2, 36, 78, 16, 5, 2, 100, 26, 100, 100, 35, 56, 100, 0, 51, 19, 4, 7, 100, 3, 8, 99, 0, 100, 15, 100, 0, 14, 96, 21, 14, 0, 102, 102, 100, 102, 102, 1, 10, 3, 102, 11, 4, 100, 33, 100, 3, 100, 35, 102, 86, 83, 102, 102, 11, 3, 17, 18, 102, 94, 19, 12, 16, 4, 4, 100, 100, 17, 100, 102, 100, 38, 102, 102, 2, 19, 41, 17, 31, 102, 3, 19, 54, 102, 100, 6, 8, 55, 49, 6, 16, 12, 100, 3, 4, 49, 33, 0, 18, 2, 102, 21, 12, 8, 102, 38, 16, 8, 29, 100, 100, 102, 17, 18, 66, 102, 28, 102, 100, 20, 11, 9, 13, 42, 102, 11, 52, 62, 57, 102, 102, 52, 18, 7, 102, 100, 8, 100, 48, 102, 13, 0, 29, 44, 100, 102, 25, 45, 102, 102, 8, 102, 6, 102, 12, 18, 4, 6, 1, 24, 0, 54, 100, 2, 100, 25, 9, 102, 6, 100, 102, 27, 6, 45, 0, 43, 100, 6, 5, 18, 66, 100, 100, 14, 0, 100, 1, 8, 51, 19, 102, 3, 99, 19, 63, 5, 0, 102, 0, 1, 41, 85, 4, 17, 51, 50, 100, 100, 102]
