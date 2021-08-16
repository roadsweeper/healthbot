import schedule
import time
import datetime
import discord
from discord.ext import commands
import asyncio
import os

client = discord.Client()



'''client = commands.Bot(command_prefix=("!"),
                      case_insensitive=True,
                      help_command=None)'''
'''def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()'''


@client.event
async def on_ready():
    print("BOT IS READY")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="your mother"))

@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")
        myid = '<@&876859196006600774>'
        await message.channel.send("wake up and current time is: " + str(datetime.datetime.now()))
        await message.channel.send(' : %s is the best ' % myid)
    if message.content.find("!time") != -1:
        await message.channel.send(datetime.datetime.now())
    if message.content.find("!start") != -1:
        await message.channel.send(datetime.datetime.now())
        alarmHour = datetime.datetime.now().hour
        alarmMinute = datetime.datetime.now().hour
        stopHour = datetime.datetime.now().hour
        stopMinute = datetime.datetime.now().minute + 3
        myid = '<@&876859196006600774>'
        while True:
            # time period condition
            if datetime.datetime.now().hour < 2 or datetime.datetime.now().hour > 8:
                '''if stopHour == datetime.datetime.now().hour and stopMinute == datetime.datetime.now().minute:
                    print('End' + str(datetime.datetime.now()))
                    await message.channel.send('End' + str(datetime.datetime.now()))'''
                if alarmMinute == datetime.datetime.now().hour:
                    print("Water Parade and Move About Time and current time is: " + str(datetime.datetime.now()))
                    await message.channel.send("wake up and current time is: " + str(datetime.datetime.now()) + ('%s' % myid))
                    alarmMinute = (alarmMinute + 1) % 24
client.run(os.environ['DISCORD_TOKEN'])

'''intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)'''


'''myvar = 'myself'
newline = '\n'  # Avoids SyntaxError: f-string expr cannot include a backslash

with open('token.txt', 'r') as file:
    myfile = f"{file.read().replace(newline, '')}".format(**locals())
'''
'''def read_token():
    with open("token.txt"), "r") as file:
    myfile = file.readlines()
    return myfile[0].strip()'''
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
print('git works on pycharm')
print(datetime.datetime.now())

'''def job():
    print(datetime.datetime.now())
    alarmHour = datetime.datetime.now().hour
    alarmMinute = datetime.datetime.now().minute
    stopHour = datetime.datetime.now().hour
    stopMinute = datetime.datetime.now().minute + 3

    while True:
        if stopHour == datetime.datetime.now().hour and stopMinute == datetime.datetime.now().minute:
            print('End'+ str(datetime.datetime.now()))
            stoptime = ('End'+ str(datetime.datetime.now()))
            break
        elif alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute:
            print("wake up and current time is: " + str(datetime.datetime.now()))
            alarmMinute = alarmMinute + 1'''

#schedule.every(4).minutes.do(job)

