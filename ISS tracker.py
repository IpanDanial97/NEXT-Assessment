import json  
import urllib.request 
from datetime import timezone
import datetime
import sys
import ssl
import webbrowser
 
# user key-in datetime
my_string = str(input('Enter date(yyyy-mm-dd hh:mm) UTC: '))
my_date = datetime.datetime.strptime(my_string, "%Y-%m-%d %H:%M")
temp = datetime.datetime.timestamp(my_date) 
timestamp = temp + 28800 

# current datetime
dt = datetime.datetime.now(timezone.utc)
utc_time = dt.replace(tzinfo=timezone.utc)
timestamp2 = utc_time.timestamp()
decide = timestamp2 - timestamp

# if condition
if decide<0:
    sys.exit("Date don't match. Datetime entered is in the future")


elif decide <600:
    och1 = (timestamp - 3600) 
    och2 = och1 + 600 
    och3 = och2 + 600
    och4 = och3 + 600
    och5 = och4 + 600
    och6 = och5 + 600
    rch = och6 + 600

    epoch1= str(och1) 
    epoch2=str(och2) 
    epoch3=str(och3) 
    epoch4=str(och4)
    epoch5=str(och5)
    epoch6=str(och6)
    Search=str(rch)
   
  

    url = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps="+ epoch1 + ","+ epoch2 +","+ epoch3 +","+ epoch4 +","+ epoch5 +","+ epoch6 +","+ Search +"&units=miles"
    ssl._create_default_https_context = ssl._create_unverified_context

elif decide <1200:
    och1 = (timestamp - 3600)
    och2 = och1 + 600 
    och3 = och2 + 600
    och4 = och3 + 600
    och5 = och4 + 600
    och6 = och5 + 600
    rch = och6 + 600
    och8 = rch + 600
    

    epoch1= str(och1) 
    epoch2=str(och2) 
    epoch3=str(och3) 
    epoch4=str(och4)
    epoch5=str(och5)
    epoch6=str(och6)
    Search=str(rch)
    epoch8=str(och8)
   

    url = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps="+ epoch1 + ","+ epoch2 +","+ epoch3 +","+ epoch4 +","+ epoch5 +","+ epoch6 +","+ Search +","+ epoch8 +"&units=miles"
    ssl._create_default_https_context = ssl._create_unverified_context
    

elif decide <1800:
    och1 = (timestamp - 3600)
    och2 = och1 + 600 
    och3 = och2 + 600
    och4 = och3 + 600
    och5 = och4 + 600
    och6 = och5 + 600
    rch = och6 + 600
    och8 = rch + 600
    och9 = och8 + 600

    epoch1= str(och1) 
    epoch2=str(och2) 
    epoch3=str(och3) 
    epoch4=str(och4)
    epoch5=str(och5)
    epoch6=str(och6)
    Search=str(rch)
    epoch8=str(och8)
    epoch9=str(och9)
    

    url = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps="+ epoch1 + ","+ epoch2 +","+ epoch3 +","+ epoch4 +","+ epoch5 +","+ epoch6 +","+ Search +","+ epoch8 + ","+ epoch9 +"&units=miles"
    ssl._create_default_https_context = ssl._create_unverified_context
    

elif decide <2400:
    och1 = (timestamp - 3600)
    och2 = och1 + 600 
    och3 = och2 + 600
    och4 = och3 + 600
    och5 = och4 + 600
    och6 = och5 + 600
    rch = och6 + 600
    och8 = rch + 600
    och9 = och8 + 600
    och10 = och9 + 600
   

    epoch1= str(och1) 
    epoch2=str(och2) 
    epoch3=str(och3) 
    epoch4=str(och4)
    epoch5=str(och5)
    epoch6=str(och6)
    Search=str(rch)
    epoch8=str(och8)
    epoch9=str(och9)
    epoch10=str(och10)
    
    

    url = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps="+ epoch1 + ","+ epoch2 +","+ epoch3 +","+ epoch4 +","+ epoch5 +","+ epoch6 +","+ Search +","+ epoch8 + ","+ epoch9 +","+ epoch10 +"&units=miles"
    ssl._create_default_https_context = ssl._create_unverified_context



elif decide <3000:
    och1 = (timestamp - 3600)
    och2 = och1 + 600 
    och3 = och2 + 600
    och4 = och3 + 600
    och5 = och4 + 600
    och6 = och5 + 600
    rch = och6 + 600
    och8 = rch + 600
    och9 = och8 + 600
    och10 = och9 + 600
    och11 = och10 + 600
    

    epoch1= str(och1) 
    epoch2=str(och2) 
    epoch3=str(och3) 
    epoch4=str(och4)
    epoch5=str(och5)
    epoch6=str(och6)
    Search=str(rch)
    epoch8=str(och8)
    epoch9=str(och9)
    epoch10=str(och10)
    epoch11=str(och11)
    
    

    url = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps="+ epoch1 + ","+ epoch2 +","+ epoch3 +","+ epoch4 +","+ epoch5 +","+ epoch6 +","+ Search +","+ epoch8 + ","+ epoch9 +","+ epoch10 +","+ epoch11 +"&units=miles"
    ssl._create_default_https_context = ssl._create_unverified_context

elif decide <3600:
        och1 = (timestamp - 3600)
        och2 = och1 + 600 
        och3 = och2 + 600
        och4 = och3 + 600
        och5 = och4 + 600
        och6 = och5 + 600
        rch = och6 + 600
        och8 = rch + 600
        och9 = och8 + 600
        och10 = och9 + 600
        och11 = och10 + 600
        och12 = och11 + 600
        

        epoch1= str(och1) 
        epoch2=str(och2) 
        epoch3=str(och3) 
        epoch4=str(och4)
        epoch5=str(och5)
        epoch6=str(och6)
        Search=str(rch)
        epoch8=str(och8)
        epoch9=str(och9)
        epoch10=str(och10)
        epoch11=str(och11)
        epoch12=str(och12)
        
        

        url = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps="+ epoch1 + ","+ epoch2 +","+ epoch3 +","+ epoch4 +","+ epoch5 +","+ epoch6 +","+ Search +","+ epoch8 + ","+ epoch9 +","+ epoch10 +","+ epoch11 +","+ epoch12 +"&units=miles"
        ssl._create_default_https_context = ssl._create_unverified_context

else:
    och1 = (timestamp - 3600)
    och2 = och1 + 600 
    och3 = och2 + 600
    och4 = och3 + 600
    och5 = och4 + 600
    och6 = och5 + 600
    rch = och6 + 600
    och8 = rch + 600
    och9 = och8 + 600
    och10 = och9 + 600
    och11 = och10 + 600
    och12 = och11 + 600
    och13 = och12 + 600

    epoch1= str(och1) 
    epoch2=str(och2) 
    epoch3=str(och3) 
    epoch4=str(och4)
    epoch5=str(och5)
    epoch6=str(och6)
    Search=str(rch)
    epoch8=str(och8)
    epoch9=str(och9)
    epoch10=str(och10)
    epoch11=str(och11)
    epoch12=str(och12)
    epoch13=str(och13)
    

    url = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps="+ epoch1 + ","+ epoch2 +","+ epoch3 +","+ epoch4 +","+ epoch5 +","+ epoch6 +","+ Search +","+ epoch8 + ","+ epoch9 +","+ epoch10 +","+ epoch11 +","+ epoch12 +","+ epoch13 +"&units=miles"
    ssl._create_default_https_context = ssl._create_unverified_context




# load the position of the ISS 
response = urllib.request.urlopen(url)
result = json.loads(response.read())
# Print text file
file = open("iss.txt", "w")
file.write("ISS Location:\n\n")
file.write("User entered (UTC) :"+ my_string + "\n\n")
file.write("Date\t" + "                   " + "Latitude\t" + "        " + "longitude\t"+ "\n")
initial = temp - 3600 
for i in result:
    mytimestamp = datetime.datetime.fromtimestamp( initial )
    date_time = mytimestamp.strftime( "%Y - %m - %d  %H : %M")  
    file.write(str(date_time) + "   " + str(i['latitude']) + "   " + str(i['longitude']))
    file.write("\n\n")
    initial += 600

file.close()
webbrowser.open("iss.txt")