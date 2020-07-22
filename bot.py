import discord
import pendulum
from datetime import datetime
#*********************************************************

ist = pendulum.timezone('Asia/Calcutta')

dt_now_str = str(datetime.now(ist))

time_now = dt_now_str[11:16]
hour_now = dt_now_str[11:13]

date = dt_now_str[0:10]
day = datetime.strptime(date, '%Y-%m-%d').weekday()

time_table = [
["C.Sc","PHY","MATHS","ENG","CHEM", "Class End"],
["ENG","CHEM","C.Sc","PHY","MATHS", "Class End"],
["C.Sc","ENG","MATHS","CHEM","PHY", "Class End"],
["CHEM","PHY","MATHS","C.Sc","ENG", "Class End"],
["MATHS","CHEM","ENG","PHY","C.Sc", "Class End"],
["ENG","CHEM","C.Sc","MATHS","PHY", "Class End"],
["It's SUNDAY","It's SUNDAY","It's SUNDAY","It's SUNDAY","It's SUNDAY", "It's SUNDAY"]]

break1 = {'08:40', '08:41', '08:42', '08:43', '08:44', '08:45', '08:46', '08:47', '08:48', '08:49'}
break2 = {'09:30', '09:31', '09:32', '09:33', '09:34', '09:35', '09:36', '09:37', '09:38', '09:39'}
break3 = {'10:20', '10:21', '10:22', '10:23', '10:24', '10:25', '10:26', '10:27', '10:28', '10:29'}
break4 = {'11:10', '11:11', '11:12', '11:13', '11:14', '11:15', '11:16', '11:17', '11:18', '11:19'}

p1 = {'08:00', '08:01', '08:02', '08:03', '08:04', '08:05', '08:06', '08:07', '08:08', '08:09', '08:10', '08:11', '08:12', '08:13', '08:14', '08:15', '08:16', '08:17', '08:18', '08:19', '08:20', '08:21', '08:22', '08:23', '08:24', '08:25', '08:26', '08:27', '08:28', '08:29', '08:30', '08:31', '08:32', '08:33', '08:34', '08:35', '08:36', '08:37', '08:38', '08:39'}
p2 = {'08:50', '08:51', '08:52', '08:53', '08:54', '08:55', '08:56', '08:57', '08:58', '08:59', '09:00', '09:01', '09:02', '09:03', '09:04', '09:05', '09:06', '09:07', '09:08', '09:09', '09:10', '09:11', '09:12', '09:13', '09:14', '09:15', '09:16', '09:17', '09:18', '09:19', '09:20', '09:21', '09:22', '09:23', '09:24', '09:25', '09:26', '09:27', '09:28', '09:29'}
p3 = {'09:40', '09:41', '09:42', '09:43', '09:44', '09:45', '09:46', '09:47', '09:48', '09:49', '09:50', '09:51', '09:52', '09:53', '09:54', '09:55', '09:56', '09:57', '09:58', '09:59', '10:00', '10:01', '10:02', '10:03', '10:04', '10:05', '10:06', '10:07', '10:08', '10:09', '10:10', '10:11', '10:12', '10:13', '10:14', '10:15', '10:16', '10:17', '10:18', '10:19'}
p4 = {'10:30', '10:31', '10:32', '10:33', '10:34', '10:35', '10:36', '10:37', '10:38', '10:39', '10:40', '10:41', '10:42', '10:43', '10:44', '10:45', '10:46', '10:47', '10:48', '10:49', '10:50', '10:51', '10:52', '10:53', '10:54', '10:55', '10:56', '10:57', '10:58', '10:59', '11:00', '11:01', '11:02', '11:03', '11:04', '11:05', '11:06', '11:07', '11:08', '11:09'}
p5 = {'11:20', '11:21', '11:22', '11:23', '11:24', '11:25', '11:26', '11:27', '11:28', '11:29', '11:30', '11:31', '11:32', '11:33', '11:34', '11:35', '11:36', '11:37', '11:38', '11:39', '11:40', '11:41', '11:42', '11:43', '11:44', '11:45', '11:46', '11:47', '11:48', '11:49', '11:50', '11:51', '11:52', '11:53', '11:54', '11:55', '11:56', '11:57', '11:58', '11:59'}


def refresh_time():
	global dt_now_str
	global time_now
	global hour_now
	global date
	global day

	dt_now_str = str(datetime.now(ist))
	date = dt_now_str[0:10]
	day = datetime.strptime(date, '%Y-%m-%d').weekday()	
	time_now = dt_now_str[11:16]
	hour_now = dt_now_str[11:13]


def find_period(current_time):
	if current_time in break1:
		return 6
	elif current_time in break2:
		return 7
	elif current_time in break3:
		return 8
	elif current_time in break4:
		return 9
	elif current_time in p1:
		return 0
	elif current_time in p2:
		return 1
	elif current_time in p3:
		return 2
	elif current_time in p4:
		return 3
	elif current_time in p5:
		return 4
		#No class is going on
		#after class
	elif int(current_time[0:2]) >= 12 and int(current_time[0:2]) <= 24:
		return 5
	else:	
		#morning time
		return 10
		
def class_now(day, time):
	global time_table
	period = find_period(time)
	#Sunday filter
	if day == 6:
		return "It's SUNDAY"

	if period in {6,7,8,9}:
		return "It's break time baby"
	elif period == 5:
		return "Class Ended!!!"		
	elif period == 10:
		return "Class has not started yet !!! , Early Boi"
	else:
		return time_table[day][period]


# print(class_now(0, '19:20'))
def class_next(day, time):
	period = find_period(time)
	if period in {6,7,8,9}:
		if period == 6:
			period = 0
		elif period == 7:
			period = 1
		elif period == 8:
			period = 2
		else:
			period = 3

	elif day == 6:
		return "It's SUNDAY"
	elif period ==5:
		return "Class Ended !!"
	elif period == 10:
		return time_table[day][0] + " class starts at [8:00 AM] "

	return time_table[day][period+1]

def next_period_start(period_num):
	global day
	start_time = ""
	#Sunday filter
	if day == 6:
		return start_time

	if period_num == 0 or period_num==6:
		start_time += "08:50"
	elif period_num == 1 or period_num==7:
		start_time += "09:40"
	elif period_num == 2 or period_num==8:
		start_time += "10:30"
	elif period_num == 3 or period_num==9:
		start_time = "11:20"
	elif period_num == 4:
		start_time = ""		
	elif period_num == 5:
		start_time = ""
	return start_time

def period_end(period_num):
	global day
	end_time = ""
	#Sunday filter
	if day == 6:
		return end_time

	if period_num in {6,7,8,9,5,10}:
		end_time = ""
	if period_num == 0:#First Period
		end_time += " till 08:40"
	elif period_num == 1:#Second Period
		end_time += " till 09:30"
	elif period_num == 2:#Third Period
		end_time += " till 10:20"
	elif period_num == 3:#Fourth Period
		end_time = " till 11:10"
	elif period_num == 4:#Fifth Period
		end_time = " till 12:00"		
	return end_time

#*********************************************************
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('?hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        if message.content.startswith('?classnext'):
        	refresh_time()
        	await message.channel.send('{0.author.mention} '.format(message)+ class_next(day,time_now)+ " " + next_period_start(find_period(time_now)))

        if message.content.startswith('?nextclass'):
        	refresh_time()
        	await message.channel.send('{0.author.mention} '.format(message)+ class_next(day,time_now)+ " " + next_period_start(find_period(time_now)))

        #removebelow
        if message.content.startswith('?timenow'):
        	refresh_time()
        	await message.channel.send('{0.author.mention} '.format(message) + str(time_now))

        if message.content.startswith('?classnow'):
        	refresh_time()
        	await message.channel.send('{0.author.mention} '.format(message)+ class_now(day,time_now) + period_end(find_period(time_now)))

        if message.content.startswith('?classall'):
        	refresh_time()
        	if day != 6:
        		await message.channel.send('{0.author.mention} '.format(message) + str(time_table[day][0:5]))
        	else:
        		await message.channel.send('{0.author.mention} '.format(message) + " It's SUNDAY")

client = MyClient()
client.run('NzM0Njk1MDI1NDg0NzU5MDUx.XxVw8g.nRYpVwQaNkNaJ7yLM-PI6m9R610')
