

from megapi import *

def onRead(v):

    if v < 15:
        bot.motorRun(M1, 0)
        bot.motorRun(M2, 0)
    else:
        bot.motorRun(M1, -100)
        bot.motorRun(M2, 100)



bot = MegaPi()
bot.start()

if __name__ == '__main__':
    bot.motorRun(M1, 0)
    bot.motorRun(M2, 0)
	while 1:
        sleep(0.1)
        bot.ultrasonicSensorRead(3,onRead)






