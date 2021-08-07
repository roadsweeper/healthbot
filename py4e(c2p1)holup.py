import schedule
import time
import datetime
'''def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)'''

def task():
    print("Water Parade and Move About Time")



print(datetime.datetime.now())

def job():
    print(datetime.datetime.now())
    alarmHour = datetime.datetime.now().hour
    alarmMinute = datetime.datetime.now().minute
    stopHour = datetime.datetime.now().hour
    stopMinute = datetime.datetime.now().minute + 3

    while True:
        if stopHour == datetime.datetime.now().hour and stopMinute == datetime.datetime.now().minute:
            print('End'+ str(datetime.datetime.now()))
            break
        elif alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute:
            print("wake up and current time is: " + str(datetime.datetime.now()))
            alarmMinute = alarmMinute + 1

schedule.every(4).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)