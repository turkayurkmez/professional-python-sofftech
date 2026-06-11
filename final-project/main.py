import csv
import json
import os
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
    handlers=[
        logging.FileHandler("project.log")
        logging.StreamHandler()
    ] 
)
logger = logging.getLogger(__name__)

DATA_FOLDER = Path("data")
TASKS_CSV = DATA_FOLDER / "tasks.csv"
REPORT_JSON = DATA_FOLDER/"report.json"
CSV_HEADERS = ["id","title","status","created_date"]

def setup():
    """Data klasörünü ve CSV dosyasını oluşturur."""
    try:
        DATA_FOLDER.mkdir(exist_ok=True)
        logger.info("Data klasörü oluşturuldu")

        if not TASKS_CSV.exists():
            # TODO 1: Dosya yoksa oluşturulacak!
            pass
    except OSError as e:
        raise