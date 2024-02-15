import requests
import json
import time
import datetime
import random
import math
# suffix 1 is for personal info
# suffix 2 is for info for other person
# suffix 3 is for trying to send message to other person 
access_token = 'NjNlN2RjNTYtMjdhZC00ZjZlLWJlMGQtNGVlMTE0ODhkOTYzZWJhNjU1NjItNTUz_PF84_0d882151-70b4-4264-a09c-4a599e4494b1' # https://developer.webex.com/docs/getting-started sign in using this link and get access token
url1 = 'https://webexapis.com/v1/people/me'
url2 = 'https://webexapis.com/v1/people'
headers1 = {'Authorization' : 'Bearer {}'.format(access_token) }
headers2 =  {'Authorization' : 'Bearer {}'.format(access_token) , 'Content-Type' : 'application/json'}
headers3 = headers2
Friend_email = 'asad.javed@afiniti.com'
params2 = { 'email' : Friend_email}

URL3 = 'https://webexapis.com/v1/messages'
message = 'Hello Asad, how are you :D '
params3 = {'toPersonEmail' : Friend_email , 'markdown' : message}

#random wait
snooze = random.randint(1,15) # minutes 
#snooze = 12 
numbers_of_hours_to_work = 12 # can't be more than 12 at a time 
cycles = math.floor((numbers_of_hours_to_work*60)/snooze) # value is 108 at the moment 
ii = 0 



current_time = time.time()

"""
headers = {

    ‘Authorization’: ‘Bearer {}‘.format(access_token)

}
"""
response1 = requests.get(url1,headers=headers1)
Personal_info1 = json.dumps(response1.json(),indent=4)
Personal_info1_1 = response1.text
Personal_info1_1= json.loads(Personal_info1_1)



response2 = requests.get(url2,headers = headers2 , params = params2)
Friend_info1 =  json.dumps(response2.json(),indent=4)


#print(Personal_info1)
#print(type(Personal_info1))

#print(Personal_info1_1)
#print(type(Personal_info1_1))

#print (Friend_info1)
while ii < cycles:
	response3 = requests.post(URL3,headers=headers3 , json = params3)
	now = datetime.datetime.now()
	ii = ii + 1
	#print ("repsonse of post request is ", response3.json())
	print(" Current time at which  message is sent is " , now.strftime("%Y-%m-%d %H:%M:%S") , "waiting for " , snooze , " minutes before sending next message ")
	time.sleep(snooze*60)
	snooze = random.randint(1,15) # minutes 
	current_time_in_loop = time.time()
	hours = math.floor((current_time_in_loop - current_time)/(60*60))
	minutes = round((((current_time_in_loop - current_time)/(60*60)) - hours)*60)
	print("Time passed since code ran (in hours and minutes)", hours , " hours and" , minutes , " minutes " )
print('All messages sent to Asad')
