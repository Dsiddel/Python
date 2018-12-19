import schedule
import time

def job():
    print("working")

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)