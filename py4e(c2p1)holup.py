import schedule
import time
import datetime
import discord
from discord.ext import commands
client = commands.Bot(command_prefix=("!"),
                      case_insensitive=True,
                      help_command=None)
@client.event
async def on_ready():
    print("BOT IS READY")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Playing your mother"))


@client.command()
async def orphan(ctx):
    answers = [
        "are you lost? should I call your parents?"
        "i'll call your mum and dad, don't worry,"
        "see  that kid over there? ask him about his parents,"
        "do you want some candy?"
    ]
client.run('ODczMTYzNzU5MDg1MDI3MzM4.YQ0bHg.VTIWZdNSdquNnKTglf-2bRv0Cxc')

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


print('git works on pycharm')
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
