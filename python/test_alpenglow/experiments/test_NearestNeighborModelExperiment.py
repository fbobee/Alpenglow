import alpenglow as prs
import alpenglow.Getter as rs
import alpenglow.experiments
import pandas as pd
import math


class TestNearestNeighborModelExperiment:
    def test_nearestNeighborModelExperiment(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_4",
            sep=' ',
            header=None,
            names=['time', 'user', 'item', 'id', 'score', 'eval']
        )
        experiment = alpenglow.experiments.NearestNeighborModelExperiment(
            top_k=100,
            seed=254938879,
            compute_similarity_period=100,
            num_of_neighbors=100
        )
        rankings = experiment.run(data, verbose=True)
        assert rankings.top_k == 100
        desired_ranks = [101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 1, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 4, 101, 101, 4, 101, 5, 101, 101, 101, 101, 101, 101, 101, 101, 101, 15, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 8, 101, 101, 101, 101, 101, 4, 101, 101, 101, 101, 101, 101, 101, 101, 3, 13, 101, 3, 101, 101, 13, 101, 101, 101, 101, 101, 101, 11, 20, 17, 1, 101, 101, 101, 101, 101, 13, 3, 101, 101, 101, 22, 1, 40, 101, 18, 14, 10, 101, 8, 4, 7, 101, 7, 101, 101, 25, 52, 63, 101, 29, 101, 2, 2, 2, 101, 101, 101, 101, 101, 1, 101, 14, 101, 101, 20, 33, 29, 22, 1, 101, 2, 101, 101, 13, 101, 101, 101, 101, 9, 101, 9, 9, 101, 101, 101, 101, 101, 7, 34, 101, 101, 36, 101, 1, 101, 101, 49, 101, 4, 101, 101, 13, 6, 101, 9, 56, 101, 2, 7, 12, 101, 101, 101, 101, 3, 101, 2, 101, 7, 101, 14, 2, 101, 101, 41, 3, 101, 26, 101, 101, 44, 42, 37, 1, 101, 2, 101, 101, 46, 1, 96, 6, 26, 101, 101, 101, 101, 101, 101, 17, 6, 101, 22, 36, 21, 28, 3, 101, 58, 14, 1, 80, 101, 101, 55, 101, 31, 19, 36, 101, 12, 58, 89, 16, 6, 7, 101, 55, 8, 101, 101, 101, 101, 11, 85, 7, 101, 101, 78, 101, 39, 60, 101, 23, 67, 6, 12, 2, 24, 101, 101, 101, 33, 101, 101, 13, 101, 10, 79, 101, 101, 101, 101, 7, 17, 49, 7, 8, 6, 9, 32, 101, 101, 101, 101, 7, 101, 4, 101, 57, 101, 12, 101, 53, 3, 67, 101, 12, 21, 25, 12, 2, 101, 100, 2, 101, 19, 101, 47, 5, 8, 11, 21, 101, 12, 12, 101, 15, 101, 5, 14, 75, 7, 43, 15, 20, 101, 1, 101, 101, 101, 2, 12, 20, 28, 101, 101, 101, 1, 13, 101, 10, 19, 101, 6, 12, 101, 82, 86, 13, 12, 49, 101, 1, 4, 101, 88, 23, 15, 101, 36, 27, 101, 101, 53, 11, 101, 14, 101, 52, 101, 32, 70, 55, 101, 101, 65, 5, 101, 1, 101, 101, 101, 101, 101, 11, 1, 53, 67, 37, 101, 39, 26, 24, 101, 55, 101, 15, 101, 4, 84, 44, 101, 101, 6, 101, 16, 11, 14, 17, 1, 7, 59, 5, 24, 2, 1, 23, 5, 7, 79, 41, 6, 61, 101, 62, 7, 101, 36, 17, 21, 15, 30, 60, 101, 24, 2, 19, 6, 10, 101, 1, 101, 11, 101, 66, 101, 101, 21, 101, 101, 101, 5, 101, 81, 43, 52, 91, 4, 101, 75, 11, 61, 38, 101, 101, 99, 67, 101, 38, 12, 13, 37, 2, 11, 24, 101, 101, 2, 40, 14, 101, 92, 1, 101, 43, 4, 21, 97, 101, 101, 17, 1, 7, 32, 101, 101, 7, 101, 71, 22, 101, 8, 101, 101, 55, 8, 101, 11, 86, 56, 67, 101, 101, 1, 90, 7, 4, 101, 3, 3, 5, 35, 26, 27, 101, 65, 62, 44, 28, 101, 50, 101, 60, 101, 3, 101, 48, 101, 5, 4, 51, 2, 101, 28, 101, 26, 69, 101, 101, 101, 42, 101, 101, 27, 27, 101, 101, 101, 101, 3, 101, 35, 101, 8, 10, 38, 14, 26, 4, 39, 101, 5, 101, 12, 49, 52, 13, 39, 13, 101, 101, 101, 6, 101, 101, 22, 48, 82, 39, 101, 20, 58, 69, 1, 52, 68, 28, 101, 77, 101, 18, 26, 10, 101, 101, 6, 101, 101, 32, 101, 10, 29, 101, 101, 101, 36, 62, 55, 101, 101, 62, 29, 101, 11, 101, 71, 24, 11, 16, 88, 4, 58, 17, 1, 9, 101, 25, 30, 4, 101, 4, 32, 1, 61, 24, 2, 6, 101, 39, 39, 101, 14, 101, 101, 3, 101, 2, 101, 17, 25, 15, 12, 16, 84, 63, 22, 2, 101, 101, 8, 2, 101, 3, 101, 31, 101, 46, 25, 36, 51, 16, 8, 101, 101, 22, 19, 19, 86, 101, 8, 15, 5, 101, 44, 9, 97, 23, 20, 14, 18, 37, 6, 101, 76, 49, 38, 80, 5, 9, 74, 101, 63, 57, 19, 6, 35, 101, 1, 2, 22, 39, 5, 15, 4, 76, 101, 55, 7, 17, 4, 101, 35, 89, 101, 101, 18, 44, 11, 36, 37, 14, 101, 19, 16, 6, 6, 101, 101, 94, 101, 44, 101, 21, 6, 89, 101, 95, 2, 15, 10, 8, 35, 67, 59, 11, 1, 3, 10, 20, 14, 12, 101, 16, 3, 101, 7, 8, 12, 82, 5, 29, 46, 10, 22, 1, 101, 101, 101, 101, 101, 18, 28, 51, 101, 11, 15, 2, 23, 39, 15, 101, 40, 101, 101, 17, 101, 101, 6, 16, 11, 40, 101, 79, 61, 9, 34, 15, 5, 73, 8, 9, 90, 101, 95, 10, 101, 101, 17, 17, 25, 30, 52, 101, 20, 22, 21, 101, 7, 25, 15, 50, 11, 15, 9, 25, 93, 6, 1, 46, 57, 10, 16, 4, 101, 37, 57, 24, 101, 81, 2, 7, 41, 52, 13, 101, 23, 8, 63, 101, 45, 101, 60, 3, 35, 24, 17, 10, 101, 1, 101, 101, 63, 101, 101, 18, 26, 15, 101, 42, 1, 101, 5, 101, 6, 41, 1, 7, 101, 101, 24, 44, 101, 101, 20, 101, 15, 101, 23, 6, 3, 11, 1, 6, 4, 30, 101, 1, 64, 8, 25, 101, 4, 66, 101, 19, 34, 2, 6, 23, 75, 13, 1, 46, 39, 19, 83, 30, 3, 79, 1, 7, 25, 8, 101, 5, 20, 49, 101, 26, 1, 101, 1, 3, 58, 101, 7, 14, 15, 30, 101, 101, 101]
        assert list(rankings["rank"].fillna(101)) == desired_ranks
