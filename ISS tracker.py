import json  
import urllib.request 
from datetime import datetime, timezone
import sys
import ssl
import webbrowser
import turtle
import time
import os 

# User key-in datetime
my_string = str(input('Enter date(yyyy-mm-dd hh:mm) UTC: '))
my_date = datetime.strptime(my_string, "%Y-%m-%d %H:%M")
temp = my_date.timestamp()                                     
timestamp = temp + 28800 

# Current datetime
dt = datetime.now(timezone.utc)
utc_time = dt.replace(tzinfo=timezone.utc)
timestamp2 = utc_time.timestamp()

# Difference between current datetime and key-in datetime 
decide = timestamp2 - timestamp

# To decide the amount of location to plot after an hour of the datetime entered

c=0
och = (timestamp - 3600)
init_list = [str(och)]
while c < 12:
    och += 600
    epoch = str(och)
    init_list+= [epoch]
    c+=1

if decide<0:
    print("Date cannot be in the future, this program will terminate in 5 seconds")
    time.sleep(5)
    sys.exit()
elif decide <600:
    list = init_list[:-6 or None]
    url = 'https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps={dt}&units=miles'.format(dt=','.join(map(str,list)))
elif decide <1200:
    list = init_list[:-5 or None]
    url = 'https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps={dt}&units=miles'.format(dt=','.join(map(str,list)))
elif decide <1800:
    list = init_list[:-4 or None]
    url = 'https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps={dt}&units=miles'.format(dt=','.join(map(str,list)))
elif decide <2400:
    list = init_list[:-3 or None]
    url = 'https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps={dt}&units=miles'.format(dt=','.join(map(str,list)))
elif decide <3000:
    list = init_list[:-2 or None]
    url = 'https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps={dt}&units=miles'.format(dt=','.join(map(str,list)))
elif decide <3600:
    list = init_list[:-1 or None]
    url = 'https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps={dt}&units=miles'.format(dt=','.join(map(str,list)))
else:
    url = 'https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps={dt}&units=miles'.format(dt=','.join(map(str,init_list)))

# Additional Information
ssl._create_default_https_context = ssl._create_unverified_context 
url2 = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps="+str(timestamp)+"&units=miles"
response2 = urllib.request.urlopen(url2) 
result2 = json.loads(response2.read())
for i in result2:
    latz=i["latitude"]
    lon=i["longitude"]
    velo=i["velocity"]

url3 = "https://api.openweathermap.org/data/2.5/weather?lat="+str(latz)+"&lon="+str(lon)+"&appid=a4f2e10b344c69d3fb3b15ab9046c869"
response3 = urllib.request.urlopen(url3) 
result3 = json.loads(response3.read())
wea=result3["weather"]
for a in wea:
 weather=a["description"]
city = result3["name"]

# Print additional information
file = open("Additional Information.txt", "w")
file.write("Additional Information \n\n") 
file.write("Datetime entered: "+ my_string+"\n")
file.write("Coordinates of ISS based on the datetime entered (lat,long): ("+ str(latz) +","+str(lon)+") \n")
if(not city):
    file.write("There's no city where ISS located based on datetime entered \n")
else:
 file.write("Name of the City where ISS located based on datetime entered: "+ city +"\n")
file.write("Current Weather:  "+str(weather)+"\n")
file.write("Velocity of ISS during the datetime entered: "+str(velo)+" KM/H"+"\n")
file.close()
webbrowser.open("Additional Information.txt")

# load the position of the ISS 
response = urllib.request.urlopen(url)  
result = json.loads(response.read()) 

# plotting map
# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)
  
# load the world map image
screen.bgpic("map/map.gif")
screen.register_shape("map/iss.gif")
iss = turtle.Turtle()
iss.shape("map/iss.gif")
iss.setheading(45)
iss.penup()

# Plot the coordinates
for z in result:
    lat=z["latitude"]
    long=z["longitude"]

    lat = float(lat)
    long = float(long)
    
    iss.goto(lon, lat)
  
    time.sleep(5)

cur_file = "Additional Information.txt"
os.remove(cur_file)