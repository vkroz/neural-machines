# Getting starting with MLFLow

Managing MLflow in docker container

### Run MLflow server in docker container
(run from MLflow module directory)
```bash
docker run -d \
-p 5001:5001 \
-v $(pwd)/mlflow_data:/mlflow \
-e MLFLOW_SERVER_FILE_STORE=/mlflow \
ghcr.io/mlflow/mlflow:latest \
mlflow server \
--host 0.0.0.0 \
--port 5001
```

### Using MLflow in python

```python
import mlflow
mlflow.set_tracking_uri("http://localhost:5000")
```

### Example of MLFlow experiment

```python
import mlflow

# Set the experiment name
mlflow.set_experiment("my_experiment")

# Start a new run
with mlflow.start_run():
    # Log a parameter
    mlflow.log_param("param1", 5)

    # Log a metric
    mlflow.log_metric("accuracy", 0.9)

    # Log an artifact
    with open("output.txt", "w") as f:
        f.write("Hello MLflow")
    mlflow.log_artifact("output.txt")

print("Experiment completed.")
```

### Accessing MLflow UI

Open in browser: http://localhost:5000


### Stop MLflow server
```bash
docker stop $(docker ps -q --filter ancestor=ghcr.io/mlflow/mlflow:latest)
```

- Tutorial: https://mlflow.org/docs/latest/
- Local server: http://127.0.0.1:5000
- 
