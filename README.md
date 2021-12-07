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



5. Plot the visualization 
    - move the training results `plotweek55result` into folder `data/result/`
    - cd into notebook folder and run following notebook in sequence
        - ensembleanalysis-residual.ipynb
        - file_generate.ipynb
        - plot_submission_file.ipynb

    - figure will saved in `figures`
