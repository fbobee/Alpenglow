import alpenglow as prs
import alpenglow.Getter as rs
import alpenglow.experiments
import alpenglow.evaluation
import pandas as pd
import math


class TestFactorExperiment:
    def test_factorExperiment(self):
        factorExperiment = alpenglow.experiments.FactorExperiment(
            top_k=100,
            seed=254938879,
            dimension=10,
            learning_rate=0.1,
            negative_rate=10
        )
        facRankings = factorExperiment.run(
            "python/test_alpenglow/test_data_4",
            experimentType="online_id",
            verbose=True)
        assert facRankings.top_k == 100
        desired_ranks = [101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 8.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 2.0, 101.0, 101.0, 1.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 23.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 2.0, 101.0, 101.0, 101.0, 24.0, 14.0, 33.0, 101.0, 101.0, 38.0, 101.0, 41.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 17.0, 101.0, 4.0, 23.0, 5.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 28.0, 101.0, 4.0, 101.0, 41.0, 101.0, 101.0, 101.0, 14.0, 101.0, 101.0, 57.0, 101.0, 46.0, 52.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 53.0, 101.0, 10.0, 7.0, 101.0, 25.0, 33.0, 9.0, 40.0, 101.0, 101.0, 13.0, 101.0, 101.0, 101.0, 27.0, 2.0, 14.0, 51.0, 101.0, 22.0, 1.0, 101.0, 101.0, 24.0, 21.0, 101.0, 101.0, 101.0, 27.0, 55.0, 62.0, 101.0, 42.0, 37.0, 58.0, 47.0, 3.0, 71.0, 7.0, 101.0, 36.0, 101.0, 101.0, 62.0, 71.0, 64.0, 101.0, 75.0, 36.0, 20.0, 11.0, 68.0, 73.0, 101.0, 72.0, 101.0, 101.0, 56.0, 101.0, 47.0, 33.0, 101.0, 3.0, 22.0, 22.0, 4.0, 23.0, 101.0, 20.0, 101.0, 101.0, 54.0, 101.0, 101.0, 101.0, 101.0, 77.0, 101.0, 3.0, 21.0, 101.0, 101.0, 101.0, 101.0, 1.0, 17.0, 78.0, 101.0, 101.0, 61.0, 101.0, 19.0, 101.0, 44.0, 69.0, 37.0, 40.0, 101.0, 101.0, 51.0, 83.0, 101.0, 47.0, 91.0, 19.0, 5.0, 1.0, 9.0, 101.0, 101.0, 101.0, 101.0, 42.0, 101.0, 11.0, 101.0, 12.0, 101.0, 98.0, 87.0, 101.0, 101.0, 39.0, 31.0, 57.0, 57.0, 101.0, 101.0, 62.0, 66.0, 16.0, 101.0, 101.0, 81.0, 101.0, 77.0, 57.0, 25.0, 26.0, 53.0, 29.0, 1.0, 101.0, 101.0, 101.0, 101.0, 101.0, 38.0, 10.0, 101.0, 30.0, 97.0, 101.0, 43.0, 57.0, 101.0, 99.0, 41.0, 1.0, 2.0, 101.0, 101.0, 16.0, 101.0, 73.0, 97.0, 89.0, 101.0, 82.0, 86.0, 4.0, 75.0, 29.0, 8.0, 101.0, 10.0, 4.0, 101.0, 101.0, 101.0, 101.0, 80.0, 60.0, 9.0, 101.0, 101.0, 72.0, 101.0, 78.0, 45.0, 101.0, 78.0, 21.0, 70.0, 22.0, 20.0, 85.0, 101.0, 101.0, 101.0, 6.0, 101.0, 61.0, 1.0, 101.0, 47.0, 66.0, 101.0, 101.0, 101.0, 101.0, 101.0, 33.0, 101.0, 12.0, 2.0, 19.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 85.0, 101.0, 101.0, 101.0, 98.0, 101.0, 101.0, 101.0, 78.0, 15.0, 93.0, 101.0, 88.0, 99.0, 89.0, 101.0, 101.0, 101.0, 2.0, 10.0, 101.0, 91.0, 101.0, 57.0, 83.0, 60.0, 15.0, 20.0, 101.0, 9.0, 101.0, 101.0, 25.0, 101.0, 4.0, 6.0, 20.0, 90.0, 76.0, 99.0, 20.0, 101.0, 9.0, 69.0, 101.0, 101.0, 1.0, 3.0, 10.0, 100.0, 101.0, 101.0, 101.0, 51.0, 14.0, 101.0, 8.0, 101.0, 101.0, 50.0, 89.0, 101.0, 73.0, 21.0, 54.0, 97.0, 79.0, 59.0, 101.0, 12.0, 101.0, 15.0, 101.0, 101.0, 76.0, 8.0, 59.0, 101.0, 101.0, 43.0, 101.0, 101.0, 2.0, 101.0, 23.0, 101.0, 42.0, 21.0, 59.0, 101.0, 101.0, 86.0, 86.0, 101.0, 57.0, 101.0, 101.0, 101.0, 101.0, 101.0, 73.0, 34.0, 101.0, 48.0, 7.0, 101.0, 79.0, 28.0, 47.0, 101.0, 101.0, 101.0, 4.0, 101.0, 33.0, 22.0, 60.0, 101.0, 101.0, 9.0, 101.0, 12.0, 101.0, 53.0, 24.0, 3.0, 101.0, 25.0, 44.0, 78.0, 43.0, 66.0, 101.0, 93.0, 99.0, 101.0, 101.0, 74.0, 11.0, 101.0, 24.0, 90.0, 101.0, 40.0, 22.0, 101.0, 68.0, 21.0, 101.0, 101.0, 93.0, 84.0, 33.0, 68.0, 38.0, 101.0, 15.0, 101.0, 68.0, 101.0, 10.0, 101.0, 101.0, 61.0, 101.0, 101.0, 101.0, 32.0, 101.0, 55.0, 20.0, 29.0, 62.0, 23.0, 101.0, 19.0, 97.0, 52.0, 59.0, 101.0, 101.0, 101.0, 65.0, 101.0, 101.0, 101.0, 101.0, 101.0, 14.0, 101.0, 91.0, 40.0, 101.0, 94.0, 101.0, 101.0, 101.0, 22.0, 99.0, 5.0, 51.0, 101.0, 14.0, 3.0, 101.0, 101.0, 17.0, 101.0, 89.0, 69.0, 101.0, 101.0, 52.0, 101.0, 13.0, 101.0, 101.0, 37.0, 101.0, 101.0, 2.0, 97.0, 101.0, 101.0, 59.0, 27.0, 17.0, 101.0, 101.0, 101.0, 58.0, 70.0, 18.0, 101.0, 72.0, 37.0, 90.0, 79.0, 7.0, 66.0, 101.0, 101.0, 99.0, 101.0, 101.0, 50.0, 101.0, 101.0, 100.0, 101.0, 14.0, 101.0, 101.0, 101.0, 66.0, 94.0, 101.0, 23.0, 101.0, 91.0, 101.0, 100.0, 11.0, 101.0, 101.0, 99.0, 101.0, 101.0, 101.0, 101.0, 2.0, 92.0, 98.0, 101.0, 71.0, 10.0, 101.0, 101.0, 101.0, 9.0, 66.0, 101.0, 101.0, 101.0, 101.0, 5.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 21.0, 101.0, 101.0, 101.0, 101.0, 9.0, 101.0, 101.0, 101.0, 101.0, 101.0, 11.0, 101.0, 32.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 46.0, 101.0, 71.0, 46.0, 76.0, 101.0, 101.0, 94.0, 101.0, 101.0, 101.0, 101.0, 4.0, 101.0, 101.0, 101.0, 15.0, 92.0, 31.0, 61.0, 47.0, 101.0, 50.0, 101.0, 101.0, 43.0, 101.0, 71.0, 101.0, 101.0, 74.0, 101.0, 18.0, 50.0, 101.0, 101.0, 10.0, 101.0, 63.0, 101.0, 16.0, 101.0, 43.0, 44.0, 16.0, 13.0, 83.0, 54.0, 53.0, 101.0, 77.0, 19.0, 101.0, 101.0, 101.0, 58.0, 69.0, 101.0, 101.0, 101.0, 84.0, 101.0, 101.0, 101.0, 101.0, 101.0, 89.0, 101.0, 13.0, 101.0, 101.0, 23.0, 14.0, 101.0, 1.0, 4.0, 77.0, 101.0, 17.0, 9.0, 2.0, 44.0, 101.0, 101.0, 101.0, 101.0, 84.0, 28.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 88.0, 91.0, 94.0, 101.0, 101.0, 101.0, 101.0, 101.0, 12.0, 101.0, 101.0, 8.0, 34.0, 101.0, 101.0, 101.0, 76.0, 101.0, 91.0, 101.0, 77.0, 101.0, 7.0, 101.0, 101.0, 101.0, 101.0, 58.0, 35.0, 101.0, 43.0, 101.0, 101.0, 101.0, 101.0, 101.0, 13.0, 101.0, 26.0, 101.0, 101.0, 101.0, 97.0, 100.0, 47.0, 101.0, 101.0, 34.0, 101.0, 101.0, 101.0, 20.0, 41.0, 101.0, 87.0, 98.0, 12.0, 101.0, 101.0, 21.0, 101.0, 101.0, 101.0, 3.0, 101.0, 101.0, 101.0, 88.0, 83.0, 101.0, 59.0, 71.0, 101.0, 11.0, 74.0, 101.0, 101.0, 101.0, 16.0, 101.0, 101.0, 101.0, 1.0, 101.0, 101.0, 101.0, 64.0, 92.0, 101.0, 6.0, 4.0, 4.0, 101.0, 101.0, 71.0, 101.0, 101.0, 101.0, 10.0, 61.0, 101.0, 83.0, 17.0, 101.0, 101.0, 101.0, 101.0, 101.0, 53.0, 101.0, 9.0, 67.0, 101.0, 101.0, 7.0, 67.0, 101.0, 101.0, 101.0, 101.0, 18.0, 101.0, 47.0, 101.0, 13.0, 15.0, 101.0, 20.0, 19.0, 101.0, 66.0, 54.0, 101.0, 101.0, 56.0, 101.0, 3.0, 101.0, 101.0, 101.0, 101.0, 101.0, 36.0, 101.0, 101.0, 4.0, 88.0, 90.0, 101.0, 21.0, 101.0, 101.0, 87.0, 2.0, 17.0, 88.0, 101.0, 97.0, 78.0, 101.0, 101.0, 101.0, 98.0, 44.0, 101.0, 3.0, 35.0, 17.0, 2.0, 101.0, 27.0, 101.0, 94.0, 90.0, 101.0, 101.0, 101.0, 101.0, 101.0, 86.0, 18.0, 101.0, 88.0, 101.0, 101.0, 33.0, 101.0, 101.0, 59.0, 101.0, 101.0, 35.0, 101.0, 30.0, 101.0, 86.0, 84.0, 101.0, 101.0, 101.0, 101.0, 39.0, 71.0, 101.0, 97.0, 101.0, 101.0, 101.0, 101.0, 101.0, 32.0, 101.0, 101.0, 101.0, 96.0, 101.0, 101.0, 30.0, 101.0, 101.0, 3.0, 59.0, 33.0, 46.0, 1.0, 101.0, 2.0, 101.0, 18.0, 68.0, 101.0, 89.0, 43.0, 95.0, 15.0, 101.0, 101.0, 101.0, 1.0, 101.0, 101.0, 62.0, 101.0, 15.0, 101.0, 101.0, 62.0, 75.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 14.0, 11.0, 101.0, 6.0, 101.0, 101.0, 59.0, 101.0, 90.0, 17.0, 101.0, 52.0, 101.0, 101.0]
        assert list(facRankings["rank"].fillna(101)) == desired_ranks

    def test_factorExperiment_2(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_4",
            sep=' ',
            header=None,
            names=['time', 'user', 'item', 'id', 'score', 'eval']
        )
        factorExperiment = alpenglow.experiments.FactorExperiment(
            top_k=100,
            seed=254938879,
            dimension=10,
            learning_rate=0.1,
            negative_rate=10
        )
        facRankings = factorExperiment.run(data, verbose=True)
        assert facRankings.top_k == 100
        desired_ranks = [101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 8.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 2.0, 101.0, 101.0, 1.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 23.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 2.0, 101.0, 101.0, 101.0, 24.0, 14.0, 33.0, 101.0, 101.0, 38.0, 101.0, 41.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 17.0, 101.0, 4.0, 23.0, 5.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 28.0, 101.0, 4.0, 101.0, 41.0, 101.0, 101.0, 101.0, 14.0, 101.0, 101.0, 57.0, 101.0, 46.0, 52.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 53.0, 101.0, 10.0, 7.0, 101.0, 25.0, 33.0, 9.0, 40.0, 101.0, 101.0, 13.0, 101.0, 101.0, 101.0, 27.0, 2.0, 14.0, 51.0, 101.0, 22.0, 1.0, 101.0, 101.0, 24.0, 21.0, 101.0, 101.0, 101.0, 27.0, 55.0, 62.0, 101.0, 42.0, 37.0, 58.0, 47.0, 3.0, 71.0, 7.0, 101.0, 36.0, 101.0, 101.0, 62.0, 71.0, 64.0, 101.0, 75.0, 36.0, 20.0, 11.0, 68.0, 73.0, 101.0, 72.0, 101.0, 101.0, 56.0, 101.0, 47.0, 33.0, 101.0, 3.0, 22.0, 22.0, 4.0, 23.0, 101.0, 20.0, 101.0, 101.0, 54.0, 101.0, 101.0, 101.0, 101.0, 77.0, 101.0, 3.0, 21.0, 101.0, 101.0, 101.0, 101.0, 1.0, 17.0, 78.0, 101.0, 101.0, 61.0, 101.0, 19.0, 101.0, 44.0, 69.0, 37.0, 40.0, 101.0, 101.0, 51.0, 83.0, 101.0, 47.0, 91.0, 19.0, 5.0, 1.0, 9.0, 101.0, 101.0, 101.0, 101.0, 42.0, 101.0, 11.0, 101.0, 12.0, 101.0, 98.0, 87.0, 101.0, 101.0, 39.0, 31.0, 57.0, 57.0, 101.0, 101.0, 62.0, 66.0, 16.0, 101.0, 101.0, 81.0, 101.0, 77.0, 57.0, 25.0, 26.0, 53.0, 29.0, 1.0, 101.0, 101.0, 101.0, 101.0, 101.0, 38.0, 10.0, 101.0, 30.0, 97.0, 101.0, 43.0, 57.0, 101.0, 99.0, 41.0, 1.0, 2.0, 101.0, 101.0, 16.0, 101.0, 73.0, 97.0, 89.0, 101.0, 82.0, 86.0, 4.0, 75.0, 29.0, 8.0, 101.0, 10.0, 4.0, 101.0, 101.0, 101.0, 101.0, 80.0, 60.0, 9.0, 101.0, 101.0, 72.0, 101.0, 78.0, 45.0, 101.0, 78.0, 21.0, 70.0, 22.0, 20.0, 85.0, 101.0, 101.0, 101.0, 6.0, 101.0, 61.0, 1.0, 101.0, 47.0, 66.0, 101.0, 101.0, 101.0, 101.0, 101.0, 33.0, 101.0, 12.0, 2.0, 19.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 85.0, 101.0, 101.0, 101.0, 98.0, 101.0, 101.0, 101.0, 78.0, 15.0, 93.0, 101.0, 88.0, 99.0, 89.0, 101.0, 101.0, 101.0, 2.0, 10.0, 101.0, 91.0, 101.0, 57.0, 83.0, 60.0, 15.0, 20.0, 101.0, 9.0, 101.0, 101.0, 25.0, 101.0, 4.0, 6.0, 20.0, 90.0, 76.0, 99.0, 20.0, 101.0, 9.0, 69.0, 101.0, 101.0, 1.0, 3.0, 10.0, 100.0, 101.0, 101.0, 101.0, 51.0, 14.0, 101.0, 8.0, 101.0, 101.0, 50.0, 89.0, 101.0, 73.0, 21.0, 54.0, 97.0, 79.0, 59.0, 101.0, 12.0, 101.0, 15.0, 101.0, 101.0, 76.0, 8.0, 59.0, 101.0, 101.0, 43.0, 101.0, 101.0, 2.0, 101.0, 23.0, 101.0, 42.0, 21.0, 59.0, 101.0, 101.0, 86.0, 86.0, 101.0, 57.0, 101.0, 101.0, 101.0, 101.0, 101.0, 73.0, 34.0, 101.0, 48.0, 7.0, 101.0, 79.0, 28.0, 47.0, 101.0, 101.0, 101.0, 4.0, 101.0, 33.0, 22.0, 60.0, 101.0, 101.0, 9.0, 101.0, 12.0, 101.0, 53.0, 24.0, 3.0, 101.0, 25.0, 44.0, 78.0, 43.0, 66.0, 101.0, 93.0, 99.0, 101.0, 101.0, 74.0, 11.0, 101.0, 24.0, 90.0, 101.0, 40.0, 22.0, 101.0, 68.0, 21.0, 101.0, 101.0, 93.0, 84.0, 33.0, 68.0, 38.0, 101.0, 15.0, 101.0, 68.0, 101.0, 10.0, 101.0, 101.0, 61.0, 101.0, 101.0, 101.0, 32.0, 101.0, 55.0, 20.0, 29.0, 62.0, 23.0, 101.0, 19.0, 97.0, 52.0, 59.0, 101.0, 101.0, 101.0, 65.0, 101.0, 101.0, 101.0, 101.0, 101.0, 14.0, 101.0, 91.0, 40.0, 101.0, 94.0, 101.0, 101.0, 101.0, 22.0, 99.0, 5.0, 51.0, 101.0, 14.0, 3.0, 101.0, 101.0, 17.0, 101.0, 89.0, 69.0, 101.0, 101.0, 52.0, 101.0, 13.0, 101.0, 101.0, 37.0, 101.0, 101.0, 2.0, 97.0, 101.0, 101.0, 59.0, 27.0, 17.0, 101.0, 101.0, 101.0, 58.0, 70.0, 18.0, 101.0, 72.0, 37.0, 90.0, 79.0, 7.0, 66.0, 101.0, 101.0, 99.0, 101.0, 101.0, 50.0, 101.0, 101.0, 100.0, 101.0, 14.0, 101.0, 101.0, 101.0, 66.0, 94.0, 101.0, 23.0, 101.0, 91.0, 101.0, 100.0, 11.0, 101.0, 101.0, 99.0, 101.0, 101.0, 101.0, 101.0, 2.0, 92.0, 98.0, 101.0, 71.0, 10.0, 101.0, 101.0, 101.0, 9.0, 66.0, 101.0, 101.0, 101.0, 101.0, 5.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 21.0, 101.0, 101.0, 101.0, 101.0, 9.0, 101.0, 101.0, 101.0, 101.0, 101.0, 11.0, 101.0, 32.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 46.0, 101.0, 71.0, 46.0, 76.0, 101.0, 101.0, 94.0, 101.0, 101.0, 101.0, 101.0, 4.0, 101.0, 101.0, 101.0, 15.0, 92.0, 31.0, 61.0, 47.0, 101.0, 50.0, 101.0, 101.0, 43.0, 101.0, 71.0, 101.0, 101.0, 74.0, 101.0, 18.0, 50.0, 101.0, 101.0, 10.0, 101.0, 63.0, 101.0, 16.0, 101.0, 43.0, 44.0, 16.0, 13.0, 83.0, 54.0, 53.0, 101.0, 77.0, 19.0, 101.0, 101.0, 101.0, 58.0, 69.0, 101.0, 101.0, 101.0, 84.0, 101.0, 101.0, 101.0, 101.0, 101.0, 89.0, 101.0, 13.0, 101.0, 101.0, 23.0, 14.0, 101.0, 1.0, 4.0, 77.0, 101.0, 17.0, 9.0, 2.0, 44.0, 101.0, 101.0, 101.0, 101.0, 84.0, 28.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 88.0, 91.0, 94.0, 101.0, 101.0, 101.0, 101.0, 101.0, 12.0, 101.0, 101.0, 8.0, 34.0, 101.0, 101.0, 101.0, 76.0, 101.0, 91.0, 101.0, 77.0, 101.0, 7.0, 101.0, 101.0, 101.0, 101.0, 58.0, 35.0, 101.0, 43.0, 101.0, 101.0, 101.0, 101.0, 101.0, 13.0, 101.0, 26.0, 101.0, 101.0, 101.0, 97.0, 100.0, 47.0, 101.0, 101.0, 34.0, 101.0, 101.0, 101.0, 20.0, 41.0, 101.0, 87.0, 98.0, 12.0, 101.0, 101.0, 21.0, 101.0, 101.0, 101.0, 3.0, 101.0, 101.0, 101.0, 88.0, 83.0, 101.0, 59.0, 71.0, 101.0, 11.0, 74.0, 101.0, 101.0, 101.0, 16.0, 101.0, 101.0, 101.0, 1.0, 101.0, 101.0, 101.0, 64.0, 92.0, 101.0, 6.0, 4.0, 4.0, 101.0, 101.0, 71.0, 101.0, 101.0, 101.0, 10.0, 61.0, 101.0, 83.0, 17.0, 101.0, 101.0, 101.0, 101.0, 101.0, 53.0, 101.0, 9.0, 67.0, 101.0, 101.0, 7.0, 67.0, 101.0, 101.0, 101.0, 101.0, 18.0, 101.0, 47.0, 101.0, 13.0, 15.0, 101.0, 20.0, 19.0, 101.0, 66.0, 54.0, 101.0, 101.0, 56.0, 101.0, 3.0, 101.0, 101.0, 101.0, 101.0, 101.0, 36.0, 101.0, 101.0, 4.0, 88.0, 90.0, 101.0, 21.0, 101.0, 101.0, 87.0, 2.0, 17.0, 88.0, 101.0, 97.0, 78.0, 101.0, 101.0, 101.0, 98.0, 44.0, 101.0, 3.0, 35.0, 17.0, 2.0, 101.0, 27.0, 101.0, 94.0, 90.0, 101.0, 101.0, 101.0, 101.0, 101.0, 86.0, 18.0, 101.0, 88.0, 101.0, 101.0, 33.0, 101.0, 101.0, 59.0, 101.0, 101.0, 35.0, 101.0, 30.0, 101.0, 86.0, 84.0, 101.0, 101.0, 101.0, 101.0, 39.0, 71.0, 101.0, 97.0, 101.0, 101.0, 101.0, 101.0, 101.0, 32.0, 101.0, 101.0, 101.0, 96.0, 101.0, 101.0, 30.0, 101.0, 101.0, 3.0, 59.0, 33.0, 46.0, 1.0, 101.0, 2.0, 101.0, 18.0, 68.0, 101.0, 89.0, 43.0, 95.0, 15.0, 101.0, 101.0, 101.0, 1.0, 101.0, 101.0, 62.0, 101.0, 15.0, 101.0, 101.0, 62.0, 75.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 14.0, 11.0, 101.0, 6.0, 101.0, 101.0, 59.0, 101.0, 90.0, 17.0, 101.0, 52.0, 101.0, 101.0]
        assert list(facRankings["rank"].fillna(101)) == desired_ranks

    def test_factorExperiment_2b(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_1",
        )
        factorExperiment = alpenglow.experiments.FactorExperiment(
            top_k=100,
            seed=254938879,
            dimension=10,
            learning_rate=0.1,
            negative_rate=10
        )
        facRankings = factorExperiment.run(data, verbose=True)
        assert facRankings.top_k == 100
        desired_ranks = [101.0, 101.0, 101.0, 2.0, 1.0, 2.0, 101.0, 101.0, 3.0]
        assert list(facRankings["rank"].fillna(101)) == desired_ranks

    def test_factorExperiment_3(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_4",
            sep=' ',
            header=None,
            names=['time', 'user', 'item', 'id', 'score', 'eval']
        )
        data['eval']=True
        data.loc[data['user'].drop_duplicates().index, 'eval']=False
        data.loc[data['item'].drop_duplicates().index, 'eval']=False
        factorExperiment = alpenglow.experiments.FactorExperiment(
            top_k=100,
            seed=254938879,
            dimension=10,
            learning_rate=0.1,
            negative_rate=10
        )
        facRankings = factorExperiment.run(
            data,
            verbose=True,
            calculate_toplists=data['eval'],
            exclude_known=True
        )
        preds = factorExperiment.get_predictions()
        preds_joined = preds.join(
            data.reset_index().set_index(['index', 'item'])['score'],
            on=['record_id', 'item'],
            how="left"
        )
        preds_hits = (
            preds_joined
            .fillna(0)
            .sort_values('score', ascending=False)
            .drop_duplicates(subset=['record_id'])
            .sort_values('record_id')
            .set_index('record_id')
        )
        preds_hits.loc[preds_hits['score'] == 0, 'rank'] = 101

        desired_ranks = [101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 8.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 2.0, 101.0, 101.0, 1.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 23.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 2.0, 101.0, 101.0, 101.0, 24.0, 14.0, 33.0, 101.0, 101.0, 38.0, 101.0, 41.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 17.0, 101.0, 4.0, 23.0, 5.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 28.0, 101.0, 4.0, 101.0, 41.0, 101.0, 101.0, 101.0, 14.0, 101.0, 101.0, 57.0, 101.0, 46.0, 52.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 53.0, 101.0, 10.0, 7.0, 101.0, 25.0, 33.0, 9.0, 40.0, 101.0, 101.0, 13.0, 101.0, 101.0, 101.0, 27.0, 2.0, 14.0, 51.0, 101.0, 22.0, 1.0, 101.0, 101.0, 24.0, 21.0, 101.0, 101.0, 101.0, 27.0, 55.0, 62.0, 101.0, 42.0, 37.0, 58.0, 47.0, 3.0, 71.0, 7.0, 101.0, 36.0, 101.0, 101.0, 62.0, 71.0, 64.0, 101.0, 75.0, 36.0, 20.0, 11.0, 68.0, 73.0, 101.0, 72.0, 101.0, 101.0, 56.0, 101.0, 47.0, 33.0, 101.0, 3.0, 22.0, 22.0, 4.0, 23.0, 101.0, 20.0, 101.0, 101.0, 54.0, 101.0, 101.0, 101.0, 101.0, 77.0, 101.0, 3.0, 21.0, 101.0, 101.0, 101.0, 101.0, 1.0, 17.0, 78.0, 101.0, 101.0, 61.0, 101.0, 19.0, 101.0, 44.0, 69.0, 37.0, 40.0, 101.0, 101.0, 51.0, 83.0, 101.0, 47.0, 91.0, 19.0, 5.0, 1.0, 9.0, 101.0, 101.0, 101.0, 101.0, 42.0, 101.0, 11.0, 101.0, 12.0, 101.0, 98.0, 87.0, 101.0, 101.0, 39.0, 31.0, 57.0, 57.0, 101.0, 101.0, 62.0, 66.0, 16.0, 101.0, 101.0, 81.0, 101.0, 77.0, 57.0, 25.0, 26.0, 53.0, 29.0, 1.0, 101.0, 101.0, 101.0, 101.0, 101.0, 38.0, 10.0, 101.0, 30.0, 97.0, 101.0, 43.0, 57.0, 101.0, 99.0, 41.0, 1.0, 2.0, 101.0, 101.0, 16.0, 101.0, 73.0, 97.0, 89.0, 101.0, 82.0, 86.0, 4.0, 75.0, 29.0, 8.0, 101.0, 10.0, 4.0, 101.0, 101.0, 101.0, 101.0, 80.0, 60.0, 9.0, 101.0, 101.0, 72.0, 101.0, 78.0, 45.0, 101.0, 78.0, 21.0, 70.0, 22.0, 20.0, 85.0, 101.0, 101.0, 101.0, 6.0, 101.0, 61.0, 1.0, 101.0, 47.0, 66.0, 101.0, 101.0, 101.0, 101.0, 101.0, 33.0, 101.0, 12.0, 2.0, 19.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 85.0, 101.0, 101.0, 101.0, 98.0, 101.0, 101.0, 101.0, 78.0, 15.0, 93.0, 101.0, 88.0, 99.0, 89.0, 101.0, 101.0, 101.0, 2.0, 10.0, 101.0, 91.0, 101.0, 57.0, 83.0, 60.0, 15.0, 20.0, 101.0, 9.0, 101.0, 101.0, 25.0, 101.0, 4.0, 6.0, 20.0, 90.0, 76.0, 99.0, 20.0, 101.0, 9.0, 69.0, 101.0, 101.0, 1.0, 3.0, 10.0, 100.0, 101.0, 101.0, 101.0, 51.0, 14.0, 101.0, 8.0, 101.0, 101.0, 50.0, 89.0, 101.0, 73.0, 21.0, 54.0, 97.0, 79.0, 59.0, 101.0, 12.0, 101.0, 15.0, 101.0, 101.0, 76.0, 8.0, 59.0, 101.0, 101.0, 43.0, 101.0, 101.0, 2.0, 101.0, 23.0, 101.0, 42.0, 21.0, 59.0, 101.0, 101.0, 86.0, 86.0, 101.0, 57.0, 101.0, 101.0, 101.0, 101.0, 101.0, 73.0, 34.0, 101.0, 48.0, 7.0, 101.0, 79.0, 28.0, 47.0, 101.0, 101.0, 101.0, 4.0, 101.0, 33.0, 22.0, 60.0, 101.0, 101.0, 9.0, 101.0, 12.0, 101.0, 53.0, 24.0, 3.0, 101.0, 25.0, 44.0, 78.0, 43.0, 66.0, 101.0, 93.0, 99.0, 101.0, 101.0, 74.0, 11.0, 101.0, 24.0, 90.0, 101.0, 40.0, 22.0, 101.0, 68.0, 21.0, 101.0, 101.0, 93.0, 84.0, 33.0, 68.0, 38.0, 101.0, 15.0, 101.0, 68.0, 101.0, 10.0, 101.0, 101.0, 61.0, 101.0, 101.0, 101.0, 32.0, 101.0, 55.0, 20.0, 29.0, 62.0, 23.0, 101.0, 19.0, 97.0, 52.0, 59.0, 101.0, 101.0, 101.0, 65.0, 101.0, 101.0, 101.0, 101.0, 101.0, 14.0, 101.0, 91.0, 40.0, 101.0, 94.0, 101.0, 101.0, 101.0, 22.0, 99.0, 5.0, 51.0, 101.0, 14.0, 3.0, 101.0, 101.0, 17.0, 101.0, 89.0, 69.0, 101.0, 101.0, 52.0, 101.0, 13.0, 101.0, 101.0, 37.0, 101.0, 101.0, 2.0, 97.0, 101.0, 101.0, 59.0, 27.0, 17.0, 101.0, 101.0, 101.0, 58.0, 70.0, 18.0, 101.0, 72.0, 37.0, 90.0, 79.0, 7.0, 66.0, 101.0, 101.0, 99.0, 101.0, 101.0, 50.0, 101.0, 101.0, 100.0, 101.0, 14.0, 101.0, 101.0, 101.0, 66.0, 94.0, 101.0, 23.0, 101.0, 91.0, 101.0, 100.0, 11.0, 101.0, 101.0, 99.0, 101.0, 101.0, 101.0, 101.0, 2.0, 92.0, 98.0, 101.0, 71.0, 10.0, 101.0, 101.0, 101.0, 9.0, 66.0, 101.0, 101.0, 101.0, 101.0, 5.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 21.0, 101.0, 101.0, 101.0, 101.0, 9.0, 101.0, 101.0, 101.0, 101.0, 101.0, 11.0, 101.0, 32.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 46.0, 101.0, 71.0, 46.0, 76.0, 101.0, 101.0, 94.0, 101.0, 101.0, 101.0, 101.0, 4.0, 101.0, 101.0, 101.0, 15.0, 92.0, 31.0, 61.0, 47.0, 101.0, 50.0, 101.0, 101.0, 43.0, 101.0, 71.0, 101.0, 101.0, 74.0, 101.0, 18.0, 50.0, 101.0, 101.0, 10.0, 101.0, 63.0, 101.0, 16.0, 101.0, 43.0, 44.0, 16.0, 13.0, 83.0, 54.0, 53.0, 101.0, 77.0, 19.0, 101.0, 101.0, 101.0, 58.0, 69.0, 101.0, 101.0, 101.0, 84.0, 101.0, 101.0, 101.0, 101.0, 101.0, 89.0, 101.0, 13.0, 101.0, 101.0, 23.0, 14.0, 101.0, 1.0, 4.0, 77.0, 101.0, 17.0, 9.0, 2.0, 44.0, 101.0, 101.0, 101.0, 101.0, 84.0, 28.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 88.0, 91.0, 94.0, 101.0, 101.0, 101.0, 101.0, 101.0, 12.0, 101.0, 101.0, 8.0, 34.0, 101.0, 101.0, 101.0, 76.0, 101.0, 91.0, 101.0, 77.0, 101.0, 7.0, 101.0, 101.0, 101.0, 101.0, 58.0, 35.0, 101.0, 43.0, 101.0, 101.0, 101.0, 101.0, 101.0, 13.0, 101.0, 26.0, 101.0, 101.0, 101.0, 97.0, 100.0, 47.0, 101.0, 101.0, 34.0, 101.0, 101.0, 101.0, 20.0, 41.0, 101.0, 87.0, 98.0, 12.0, 101.0, 101.0, 21.0, 101.0, 101.0, 101.0, 3.0, 101.0, 101.0, 101.0, 88.0, 83.0, 101.0, 59.0, 71.0, 101.0, 11.0, 74.0, 101.0, 101.0, 101.0, 16.0, 101.0, 101.0, 101.0, 1.0, 101.0, 101.0, 101.0, 64.0, 92.0, 101.0, 6.0, 4.0, 4.0, 101.0, 101.0, 71.0, 101.0, 101.0, 101.0, 10.0, 61.0, 101.0, 83.0, 17.0, 101.0, 101.0, 101.0, 101.0, 101.0, 53.0, 101.0, 9.0, 67.0, 101.0, 101.0, 7.0, 67.0, 101.0, 101.0, 101.0, 101.0, 18.0, 101.0, 47.0, 101.0, 13.0, 15.0, 101.0, 20.0, 19.0, 101.0, 66.0, 54.0, 101.0, 101.0, 56.0, 101.0, 3.0, 101.0, 101.0, 101.0, 101.0, 101.0, 36.0, 101.0, 101.0, 4.0, 88.0, 90.0, 101.0, 21.0, 101.0, 101.0, 87.0, 2.0, 17.0, 88.0, 101.0, 97.0, 78.0, 101.0, 101.0, 101.0, 98.0, 44.0, 101.0, 3.0, 35.0, 17.0, 2.0, 101.0, 27.0, 101.0, 94.0, 90.0, 101.0, 101.0, 101.0, 101.0, 101.0, 86.0, 18.0, 101.0, 88.0, 101.0, 101.0, 33.0, 101.0, 101.0, 59.0, 101.0, 101.0, 35.0, 101.0, 30.0, 101.0, 86.0, 84.0, 101.0, 101.0, 101.0, 101.0, 39.0, 71.0, 101.0, 97.0, 101.0, 101.0, 101.0, 101.0, 101.0, 32.0, 101.0, 101.0, 101.0, 96.0, 101.0, 101.0, 30.0, 101.0, 101.0, 3.0, 59.0, 33.0, 46.0, 1.0, 101.0, 2.0, 101.0, 18.0, 68.0, 101.0, 89.0, 43.0, 95.0, 15.0, 101.0, 101.0, 101.0, 1.0, 101.0, 101.0, 62.0, 101.0, 15.0, 101.0, 101.0, 62.0, 75.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 14.0, 11.0, 101.0, 6.0, 101.0, 101.0, 59.0, 101.0, 90.0, 17.0, 101.0, 52.0, 101.0, 101.0]
        desired_ranks = pd.Series([1]+desired_ranks)[data['eval']].tolist()
        assert list(facRankings["rank"].fillna(101)) == desired_ranks
        assert desired_ranks == list(preds_hits['rank'])
