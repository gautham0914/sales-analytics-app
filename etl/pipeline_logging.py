import logging
from etl.transform import transform_data
from etl.load_to_db import load_to_db



# ✅ Logging config for Day 11
logging.basicConfig(
    filename="log/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline_safe():
    try:
        logging.info("🚀 Pipeline started")

        df = transform_data()
        logging.info(f"✅ Data loaded — {df.shape[0]} rows")

        load_to_db(df)
        logging.info("✅ load_to_db() completed")

        logging.info("🎉 Pipeline finished successfully")

    except Exception as e:
        logging.error(f"❌ Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline_safe()

