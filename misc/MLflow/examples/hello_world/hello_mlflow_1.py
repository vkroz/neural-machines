import os

import mlflow
import dotenv

dotenv.load_dotenv()

# Set MLflow tracking URI
mlflow.set_tracking_uri(os.getenv('MLFLOW_TRACKING_URL'))

# Ensure OpenAI API key is set
assert "OPENAI_API_KEY" in os.environ, "Please set the OPENAI_API_KEY environment variable to run this example."


def main():
    """
    This is a simple example of how to use MLflow in a Python file.
    """

    with mlflow.start_run(experiment_id='700148984668900630') as run:
        mlflow.log_param("my", "param")
        mlflow.log_metric("score", 100)


if __name__ == "__main__":
    main()
