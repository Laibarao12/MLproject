import logging
import os
from datetime import datetime

# Step 1: Create log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Create logs directory
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Step 3: Full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Step 4: Setup logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s- %(levelname)s - %(message)s",
    level=logging.INFO
)


if __name__=="__main__":
    logging.info("Logging has started")


# Step 5: Write logs
"""logging.info("Program started")
logging.warning("This is just a warning")
logging.error("Oops! An error happened")"""
