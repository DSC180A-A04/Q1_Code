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
python -m src.pipeline.train_model --config_filename=configs/model/dcrnn_cov.yaml
```

- inference

```bash
source src/pipeline/test.sh
```

- visualization

  - move the training results `plotweek55result` into folder `data/result/`
  - cd into `notebooks` folder and run following notebook in sequence

    - ensembleanalysis-residual.ipynb
    - file_generate.ipynb
    - plot_submission_file.ipynb

  - figure will saved in `figures`

- clean the repo

```bash
python run.py clean
```

## Docker

```bash
>>> docker build -f ./Dockerfile -t dsc-180-q1-code .
>>> docker run --rm -it dsc-180-q1-code /bin/bash
```
