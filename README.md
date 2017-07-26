![Alpenglow](./misc/alpenglow.png)


# Alpenglow

- Alpenglow is a free and open source C++ framework with easy-to-use Python API.
- Alpenglow is capable of training and evaluating industry standard recommendation algorithms including variants of popularity, nearest neighbor, and factorization models.
- Besides batch training and evaluation, Alpenglow supports online training of recommendation models capable of adapting to concept drift in non-stationary environments.

### Requirements:
- Anaconda + python3 environment

### Installation:
- `cd Alpenglow`
- `conda install libgcc`
- `pip install .`

### Development:
- For faster recompilation, use `export CC="ccache cc"`
- To enable compilation on 4 threads for example, use `echo 4 > .parallel`
- Reinstall modified version using `pip install --upgrade --force-reinstall --no-deps .`
- To build and use in the current folder, use `pip install --upgrade --force-reinstall --no-deps -e .` and `export PYTHONPATH="$(pwd)/python:$PYTHONPATH"`

### Example usage:
- Sample dataset: http://info.ilab.sztaki.hu/~fbobee/alpenglow/alpenglow_sample_dataset

```python
from alpenglow.experiments import FactorModelExperiment
from alpenglow.evaluation import DcgScore
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = pd.read_csv("/path/to/sample_dataset")

factor_model_experiment = FactorModelExperiment(
    top_k=100,
    seed=254938879,
    dimension=10,
    learning_rate=0.14,
    negative_rate=100
)
fac_rankings = factor_model_experiment.run(data, verbose=True)
fac_rankings['dcg'] = DcgScore(fac_rankings)
fac_rankings['dcg'].groupby((fac_rankings['time']-fac_rankings['time'].min())//86400).mean().plot()
plt.savefig("factor.png")
```
