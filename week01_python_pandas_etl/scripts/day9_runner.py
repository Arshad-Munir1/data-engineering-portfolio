import time
import logging
import subprocess

# Setup logging
logging.basicConfig(
    filename="../data/logs/pipeline_runner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_script(script_name):
    """Runs a Python script and logs execution"""
    
    logging.info(f"Starting: {script_name}")
    start_time = time.time()

    try:
        subprocess.run(["python", script_name], check=True)
        duration = round(time.time() - start_time, 2)

        logging.info(f"Completed: {script_name} in {duration} seconds")

    except subprocess.CalledProcessError:
        logging.error(f"FAILED: {script_name}")
        raise

def main():
    logging.info("===== PIPELINE RUN STARTED =====")

    pipeline_steps = [
        "day3_transform.py",
        "day4_aggregate.py",
        "day5_validate.py"
    ]

    for step in pipeline_steps:
        run_script(step)

    logging.info("===== PIPELINE RUN COMPLETED SUCCESSFULLY =====")

if __name__ == "__main__":
    main()