import time

import schedule
from app import etl

if __name__ == "__main__":
    etl.run_etl()
    schedule.every(1).seconds.do(etl.run_etl)

    while True:
        schedule.run_pending()
        time.sleep(1)
