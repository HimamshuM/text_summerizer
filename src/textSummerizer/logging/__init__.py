import sys
import os 
import logging

# creating log directory 
log_dir = "logs"

# creating file 
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

## mentioned path so that log file should create under log directory
log_filepath = os.path.join(log_dir,"logging_str")

## making directory named "log"
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger("summarizer logger")
