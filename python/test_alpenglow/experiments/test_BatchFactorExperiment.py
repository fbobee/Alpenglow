import alpenglow as prs
import alpenglow.Getter as rs
import alpenglow.experiments
import pandas as pd
import math


class TestBatchFactorExperiment:
    def test_batchFactorExperiment(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_41",
            sep=' ',
            header=None,
            names=['time', 'user', 'item', 'id', 'score', 'eval']
        )
        sbExperiment = alpenglow.experiments.BatchFactorExperiment(
            top_k=100,
            negative_rate=3,
            seed=254938879,
            period_length=1000
        )
        rankings = sbExperiment.run(data, verbose=True)
        assert rankings.top_k == 100
        desired_ranks = [101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 25.0, 64.0, 42.0, 101.0, 101.0, 16.0, 101.0, 101.0, 101.0, 36.0, 63.0, 101.0, 81.0, 101.0, 101.0, 17.0, 10.0, 101.0, 4.0, 5.0, 39.0, 7.0, 13.0, 2.0, 101.0, 101.0, 101.0, 101.0, 83.0, 101.0, 58.0, 101.0, 8.0, 101.0, 64.0, 33.0, 101.0, 101.0, 50.0, 29.0, 32.0, 38.0, 101.0, 101.0, 11.0, 13.0, 4.0, 101.0, 101.0, 14.0, 101.0, 19.0, 2.0, 83.0, 77.0, 78.0, 47.0, 93.0, 101.0, 101.0, 101.0, 101.0, 101.0, 14.0, 4.0, 101.0, 101.0, 101.0, 6.0, 93.0, 7.0, 101.0, 40.0, 5.0, 12.0, 42.0, 101.0, 101.0, 20.0, 101.0, 26.0, 42.0, 37.0, 101.0, 19.0, 30.0, 72.0, 30.0, 92.0, 10.0, 101.0, 101.0, 17.0, 101.0, 101.0, 101.0, 101.0, 24.0, 88.0, 12.0, 101.0, 101.0, 37.0, 101.0, 87.0, 30.0, 101.0, 12.0, 37.0, 42.0, 97.0, 23.0, 88.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 14.0, 101.0, 7.0, 17.0, 101.0, 101.0, 101.0, 101.0, 27.0, 99.0, 101.0, 101.0, 101.0, 89.0, 44.0, 36.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 85.0, 101.0, 96.0, 101.0, 37.0, 101.0, 101.0, 101.0, 6.0, 101.0, 38.0, 97.0, 101.0, 101.0, 86.0, 101.0, 101.0, 37.0, 101.0, 101.0, 20.0, 101.0, 3.0, 46.0, 101.0, 2.0, 101.0, 101.0, 90.0, 101.0, 101.0, 101.0, 10.0, 35.0, 6.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 22.0, 33.0, 43.0, 35.0, 101.0, 101.0, 101.0, 28.0, 101.0, 101.0, 9.0, 101.0, 101.0, 8.0, 5.0, 101.0, 77.0, 101.0, 93.0, 3.0, 66.0, 101.0, 2.0, 5.0, 101.0, 61.0, 17.0, 15.0, 42.0, 23.0, 90.0, 101.0, 101.0, 81.0, 17.0, 101.0, 101.0, 101.0, 40.0, 101.0, 54.0, 96.0, 10.0, 101.0, 101.0, 16.0, 101.0, 101.0, 16.0, 101.0, 101.0, 101.0, 101.0, 101.0, 8.0, 85.0, 41.0, 5.0, 70.0, 101.0, 20.0, 35.0, 6.0, 101.0, 70.0, 101.0, 9.0, 101.0, 8.0, 81.0, 10.0, 101.0, 101.0, 101.0, 101.0, 101.0, 29.0, 19.0, 85.0, 1.0, 3.0, 19.0, 1.0, 5.0, 2.0, 15.0, 11.0, 63.0, 2.0, 26.0, 73.0, 16.0, 83.0, 101.0, 3.0, 89.0, 101.0, 6.0, 33.0, 45.0, 24.0, 101.0, 79.0, 46.0, 21.0, 1.0, 90.0, 1.0, 1.0, 101.0, 1.0, 101.0, 32.0, 101.0, 23.0, 101.0, 84.0, 14.0, 101.0, 101.0, 101.0, 2.0, 101.0, 101.0, 44.0, 55.0, 65.0, 73.0, 101.0, 51.0, 66.0, 31.0, 6.0, 101.0, 101.0, 101.0, 101.0, 101.0, 47.0, 63.0, 101.0, 59.0, 6.0, 2.0, 7.0, 101.0, 101.0, 1.0, 60.0, 13.0, 95.0, 41.0, 1.0, 96.0, 63.0, 2.0, 37.0, 69.0, 101.0, 101.0, 7.0, 3.0, 101.0, 48.0, 101.0, 101.0, 27.0, 101.0, 22.0, 96.0, 101.0, 1.0, 101.0, 101.0, 42.0, 6.0, 101.0, 19.0, 101.0, 75.0, 79.0, 101.0, 101.0, 18.0, 71.0, 30.0, 3.0, 101.0, 1.0, 101.0, 2.0, 5.0, 5.0, 9.0, 101.0, 101.0, 29.0, 22.0, 17.0, 101.0, 90.0, 101.0, 101.0, 101.0, 1.0, 101.0, 19.0, 101.0, 101.0, 1.0, 101.0, 24.0, 101.0, 101.0, 101.0, 34.0, 34.0, 101.0, 101.0, 43.0, 15.0, 31.0, 101.0, 12.0, 13.0, 53.0, 101.0, 101.0, 101.0, 7.0, 101.0, 4.0, 101.0, 16.0, 10.0, 18.0, 8.0, 14.0, 1.0, 15.0, 101.0, 2.0, 101.0, 15.0, 68.0, 26.0, 28.0, 33.0, 5.0, 101.0, 101.0, 101.0, 14.0, 101.0, 101.0, 46.0, 5.0, 20.0, 31.0, 101.0, 19.0, 101.0, 17.0, 5.0, 9.0, 35.0, 34.0, 101.0, 35.0, 101.0, 2.0, 35.0, 8.0, 101.0, 101.0, 4.0, 101.0, 101.0, 9.0, 101.0, 7.0, 19.0, 101.0, 101.0, 101.0, 17.0, 60.0, 16.0, 101.0, 101.0, 17.0, 27.0, 101.0, 1.0, 101.0, 34.0, 35.0, 39.0, 9.0, 31.0, 3.0, 5.0, 6.0, 7.0, 28.0, 101.0, 38.0, 9.0, 2.0, 97.0, 7.0, 33.0, 7.0, 38.0, 9.0, 2.0, 6.0, 101.0, 25.0, 22.0, 101.0, 15.0, 101.0, 101.0, 5.0, 101.0, 13.0, 101.0, 54.0, 3.0, 3.0, 22.0, 33.0, 101.0, 47.0, 101.0, 12.0, 101.0, 101.0, 1.0, 8.0, 101.0, 4.0, 92.0, 13.0, 101.0, 22.0, 28.0, 39.0, 12.0, 101.0, 5.0, 101.0, 101.0, 24.0, 19.0, 101.0, 101.0, 101.0, 2.0, 2.0, 1.0, 101.0, 20.0, 20.0, 22.0, 7.0, 16.0, 26.0, 18.0, 15.0, 18.0, 101.0, 83.0, 23.0, 7.0, 54.0, 3.0, 1.0, 101.0, 101.0, 42.0, 25.0, 12.0, 1.0, 32.0, 101.0, 2.0, 1.0, 98.0, 55.0, 3.0, 40.0, 1.0, 101.0, 101.0, 21.0, 4.0, 31.0, 1.0, 101.0, 16.0, 30.0, 101.0, 101.0, 2.0, 46.0, 30.0, 14.0, 14.0, 7.0, 101.0, 5.0, 8.0, 3.0, 18.0, 101.0, 92.0, 61.0, 49.0, 44.0, 101.0, 6.0, 9.0, 51.0, 101.0, 32.0, 2.0, 7.0, 22.0, 10.0, 101.0, 101.0, 25.0, 15.0, 2.0, 1.0, 13.0, 33.0, 8.0, 4.0, 101.0, 10.0, 3.0, 101.0, 1.0, 1.0, 30.0, 101.0, 1.0, 32.0, 54.0, 4.0, 12.0, 1.0, 101.0, 101.0, 101.0, 101.0, 101.0, 15.0, 22.0, 2.0, 101.0, 7.0, 20.0, 15.0, 12.0, 55.0, 5.0, 101.0, 33.0, 101.0, 61.0, 101.0, 101.0, 101.0, 8.0, 13.0, 4.0, 18.0, 101.0, 101.0, 25.0, 11.0, 38.0, 10.0, 2.0, 51.0, 6.0, 25.0, 101.0, 101.0, 73.0, 101.0, 101.0, 101.0, 23.0, 27.0, 24.0, 26.0, 27.0, 101.0, 5.0, 19.0, 23.0, 101.0, 40.0, 27.0, 2.0, 15.0, 34.0, 12.0, 8.0, 4.0, 32.0, 16.0, 101.0, 101.0, 45.0, 6.0, 15.0, 3.0, 101.0, 10.0, 8.0, 6.0, 101.0, 25.0, 7.0, 4.0, 31.0, 101.0, 33.0, 101.0, 11.0, 11.0, 21.0, 101.0, 37.0, 101.0, 101.0, 11.0, 10.0, 26.0, 12.0, 19.0, 101.0, 10.0, 101.0, 101.0, 101.0, 101.0, 101.0, 27.0, 24.0, 10.0, 101.0, 40.0, 1.0, 101.0, 8.0, 101.0, 20.0, 2.0, 10.0, 18.0, 101.0, 101.0, 101.0, 34.0, 101.0, 101.0, 13.0, 101.0, 22.0, 101.0, 8.0, 12.0, 1.0, 5.0, 3.0, 31.0, 1.0, 101.0, 101.0, 3.0, 33.0, 13.0, 101.0, 101.0, 25.0, 34.0, 101.0, 12.0, 11.0, 28.0, 1.0, 39.0, 101.0, 21.0, 5.0, 25.0, 45.0, 6.0, 36.0, 23.0, 1.0, 101.0, 1.0, 7.0, 35.0, 17.0, 101.0, 2.0, 9.0, 10.0, 73.0, 17.0, 1.0, 101.0, 1.0, 4.0, 65.0, 101.0, 12.0, 25.0, 34.0, 25.0, 101.0, 95.0, 101.0]
        assert list(rankings["rank"].fillna(101)) == desired_ranks

    def test_batchFactorExperiment_timeframe(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_41",
            sep=' ',
            header=None,
            names=['time', 'user', 'item', 'id', 'score', 'eval']
        )
        sbExperiment = alpenglow.experiments.BatchFactorExperiment(
            top_k=100,
            negative_rate=3,
            seed=254938879,
            period_length=1000,
            timeframe_length=2000
        )
        rankings = sbExperiment.run(data, verbose=True)
        assert rankings.top_k == 100
        desired_ranks=[101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 25.0, 64.0, 42.0, 101.0, 101.0, 16.0, 101.0, 101.0, 101.0, 36.0, 63.0, 101.0, 81.0, 101.0, 101.0, 17.0, 10.0, 101.0, 4.0, 5.0, 39.0, 7.0, 13.0, 2.0, 101.0, 101.0, 101.0, 101.0, 83.0, 101.0, 58.0, 101.0, 8.0, 101.0, 64.0, 33.0, 101.0, 101.0, 50.0, 29.0, 32.0, 38.0, 101.0, 101.0, 11.0, 13.0, 4.0, 101.0, 101.0, 14.0, 101.0, 19.0, 2.0, 83.0, 77.0, 78.0, 47.0, 93.0, 101.0, 101.0, 101.0, 101.0, 101.0, 14.0, 4.0, 101.0, 101.0, 101.0, 6.0, 93.0, 7.0, 101.0, 40.0, 5.0, 12.0, 42.0, 101.0, 101.0, 20.0, 101.0, 26.0, 42.0, 37.0, 101.0, 19.0, 30.0, 72.0, 30.0, 92.0, 10.0, 101.0, 101.0, 17.0, 101.0, 101.0, 101.0, 101.0, 24.0, 88.0, 12.0, 101.0, 101.0, 37.0, 101.0, 87.0, 30.0, 101.0, 12.0, 37.0, 42.0, 97.0, 23.0, 88.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 14.0, 101.0, 7.0, 17.0, 101.0, 101.0, 101.0, 101.0, 27.0, 99.0, 101.0, 101.0, 101.0, 89.0, 44.0, 36.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 85.0, 101.0, 96.0, 101.0, 37.0, 101.0, 101.0, 101.0, 6.0, 101.0, 38.0, 97.0, 101.0, 101.0, 86.0, 101.0, 101.0, 37.0, 101.0, 101.0, 20.0, 101.0, 3.0, 46.0, 101.0, 2.0, 101.0, 101.0, 90.0, 101.0, 101.0, 101.0, 10.0, 35.0, 6.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 22.0, 33.0, 43.0, 35.0, 101.0, 101.0, 101.0, 28.0, 101.0, 101.0, 9.0, 101.0, 101.0, 8.0, 5.0, 101.0, 77.0, 101.0, 93.0, 3.0, 66.0, 101.0, 2.0, 5.0, 101.0, 61.0, 17.0, 15.0, 42.0, 23.0, 90.0, 101.0, 101.0, 81.0, 17.0, 101.0, 101.0, 101.0, 40.0, 101.0, 54.0, 96.0, 10.0, 101.0, 101.0, 16.0, 101.0, 101.0, 16.0, 101.0, 101.0, 101.0, 101.0, 101.0, 8.0, 85.0, 41.0, 5.0, 70.0, 101.0, 20.0, 35.0, 6.0, 101.0, 70.0, 101.0, 9.0, 101.0, 8.0, 81.0, 10.0, 101.0, 101.0, 101.0, 101.0, 101.0, 29.0, 19.0, 85.0, 1.0, 3.0, 19.0, 1.0, 5.0, 2.0, 15.0, 11.0, 63.0, 2.0, 26.0, 73.0, 16.0, 83.0, 101.0, 3.0, 89.0, 101.0, 6.0, 33.0, 45.0, 24.0, 101.0, 79.0, 46.0, 21.0, 1.0, 90.0, 1.0, 1.0, 101.0, 1.0, 101.0, 32.0, 101.0, 23.0, 101.0, 84.0, 14.0, 101.0, 101.0, 101.0, 2.0, 101.0, 101.0, 44.0, 55.0, 65.0, 73.0, 101.0, 51.0, 66.0, 31.0, 6.0, 101.0, 101.0, 101.0, 101.0, 101.0, 47.0, 63.0, 101.0, 59.0, 6.0, 2.0, 7.0, 101.0, 101.0, 1.0, 60.0, 13.0, 95.0, 41.0, 1.0, 96.0, 63.0, 2.0, 37.0, 69.0, 101.0, 101.0, 7.0, 3.0, 101.0, 48.0, 101.0, 101.0, 27.0, 101.0, 22.0, 96.0, 101.0, 1.0, 101.0, 101.0, 42.0, 6.0, 101.0, 19.0, 101.0, 75.0, 79.0, 101.0, 101.0, 18.0, 71.0, 30.0, 3.0, 101.0, 1.0, 101.0, 2.0, 5.0, 5.0, 9.0, 101.0, 101.0, 29.0, 22.0, 17.0, 101.0, 90.0, 101.0, 101.0, 101.0, 1.0, 101.0, 19.0, 101.0, 101.0, 1.0, 101.0, 24.0, 101.0, 101.0, 101.0, 37.0, 11.0, 101.0, 101.0, 63.0, 10.0, 32.0, 101.0, 12.0, 40.0, 42.0, 101.0, 101.0, 45.0, 14.0, 101.0, 3.0, 101.0, 15.0, 1.0, 101.0, 66.0, 14.0, 4.0, 11.0, 101.0, 2.0, 101.0, 15.0, 23.0, 76.0, 81.0, 25.0, 9.0, 101.0, 70.0, 101.0, 37.0, 101.0, 101.0, 41.0, 64.0, 18.0, 11.0, 101.0, 94.0, 101.0, 98.0, 1.0, 4.0, 101.0, 76.0, 46.0, 101.0, 101.0, 5.0, 24.0, 5.0, 101.0, 101.0, 18.0, 101.0, 101.0, 89.0, 101.0, 52.0, 84.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 15.0, 12.0, 101.0, 3.0, 101.0, 100.0, 44.0, 17.0, 63.0, 68.0, 1.0, 53.0, 8.0, 1.0, 9.0, 101.0, 21.0, 22.0, 4.0, 56.0, 1.0, 78.0, 4.0, 101.0, 3.0, 5.0, 46.0, 101.0, 101.0, 92.0, 101.0, 21.0, 101.0, 58.0, 2.0, 101.0, 12.0, 101.0, 101.0, 2.0, 2.0, 66.0, 101.0, 68.0, 50.0, 101.0, 19.0, 101.0, 101.0, 1.0, 8.0, 101.0, 7.0, 101.0, 14.0, 101.0, 17.0, 96.0, 91.0, 11.0, 101.0, 9.0, 101.0, 101.0, 25.0, 36.0, 101.0, 101.0, 101.0, 3.0, 12.0, 4.0, 101.0, 39.0, 72.0, 18.0, 40.0, 87.0, 68.0, 16.0, 68.0, 86.0, 101.0, 30.0, 101.0, 12.0, 57.0, 8.0, 3.0, 101.0, 101.0, 15.0, 69.0, 23.0, 2.0, 101.0, 101.0, 25.0, 1.0, 81.0, 65.0, 46.0, 16.0, 2.0, 101.0, 101.0, 9.0, 14.0, 18.0, 1.0, 101.0, 88.0, 11.0, 101.0, 101.0, 5.0, 47.0, 22.0, 99.0, 20.0, 12.0, 101.0, 2.0, 34.0, 3.0, 26.0, 101.0, 77.0, 101.0, 87.0, 62.0, 101.0, 28.0, 3.0, 101.0, 43.0, 17.0, 10.0, 42.0, 31.0, 9.0, 101.0, 101.0, 77.0, 18.0, 2.0, 6.0, 17.0, 63.0, 26.0, 34.0, 101.0, 6.0, 4.0, 101.0, 1.0, 7.0, 19.0, 101.0, 2.0, 87.0, 101.0, 7.0, 24.0, 4.0, 101.0, 101.0, 101.0, 101.0, 101.0, 8.0, 37.0, 23.0, 101.0, 8.0, 15.0, 15.0, 13.0, 101.0, 36.0, 86.0, 67.0, 101.0, 98.0, 101.0, 101.0, 101.0, 12.0, 12.0, 27.0, 27.0, 101.0, 101.0, 48.0, 16.0, 55.0, 37.0, 9.0, 101.0, 29.0, 13.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 6.0, 27.0, 33.0, 2.0, 34.0, 101.0, 6.0, 4.0, 28.0, 101.0, 14.0, 12.0, 5.0, 19.0, 21.0, 11.0, 3.0, 5.0, 101.0, 4.0, 101.0, 101.0, 83.0, 35.0, 17.0, 2.0, 101.0, 64.0, 13.0, 10.0, 101.0, 11.0, 12.0, 8.0, 17.0, 101.0, 33.0, 101.0, 13.0, 16.0, 24.0, 101.0, 84.0, 101.0, 101.0, 11.0, 16.0, 43.0, 18.0, 97.0, 101.0, 2.0, 101.0, 101.0, 101.0, 101.0, 101.0, 41.0, 31.0, 16.0, 101.0, 101.0, 12.0, 101.0, 11.0, 101.0, 49.0, 1.0, 11.0, 22.0, 75.0, 101.0, 101.0, 101.0, 101.0, 101.0, 18.0, 101.0, 54.0, 101.0, 13.0, 23.0, 3.0, 1.0, 1.0, 85.0, 1.0, 101.0, 54.0, 6.0, 69.0, 3.0, 101.0, 101.0, 37.0, 101.0, 101.0, 2.0, 11.0, 57.0, 8.0, 101.0, 101.0, 29.0, 8.0, 25.0, 101.0, 72.0, 69.0, 24.0, 7.0, 101.0, 2.0, 5.0, 101.0, 33.0, 101.0, 9.0, 25.0, 20.0, 101.0, 20.0, 6.0, 101.0, 4.0, 2.0, 95.0, 101.0, 2.0, 19.0, 62.0, 40.0, 101.0, 101.0, 101.0]
        assert list(rankings["rank"].fillna(101)) == desired_ranks
