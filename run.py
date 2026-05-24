from app.core.logging_config import setup_logging
from app.core.pipeline import run_pipeline

setup_logging()

if __name__ == "__main__":
    run_pipeline()
