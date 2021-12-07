# Get Started

1. create a virtual environment

```bash
>>> python3 -m venv venv
>>> source venv/bin/activate
```

2. install dependencies

```bash
>>> pip install -r requirements.txt
```

3. run the pipeline

- train models

```bash
python -m src.analysis.train_model --config_filename=configs/model/dcrnn_cov.yaml
python run.py train
```

- inference

```bash
python run.py test
```
