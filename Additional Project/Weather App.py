# The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.

# import requests(rq), tkinter(all), pillow and datetime library
import requests as rq
from tkinter import *
from tkinter import messagebox
from datetime import datetime as dt

base_url = 'https://api.openweathermap.org/data/2.5/weather?' # weather site chosen is openweathermap 
api_key = open('key.txt','r').read() #API key saved in a txt file to protect the information

def weather_details(city):
    url = base_url+'appid='+api_key+'&q='+city # complete URL for the API call from openweatherapp(concatenating city(q=) and API key(appid=)
    re = rq.get(url) #using the json function to transmit the data from the url into a dictonary
    if re:
        r = re.json()
        # getting values from dictonary
        long = r['coord']['lon'] 
        lat = r['coord']['lat'] 
        weather = r['weather'][0]['main']
        weather_des = r['weather'][0]['description']
        temp_cel = r['main']['temp'] - 273.15
        humi = r['main']['humidity']
        location = r['name']
        # getting date and time from datetime library
        datetime = dt.now() 
        sunrise = dt.utcfromtimestamp(r['sys']['sunrise']+r['timezone']) 
        sunset = dt.utcfromtimestamp(r['sys']['sunset']+r['timezone'])
        # formatting date and time
        datetime_string = datetime.strftime('%b-%d-%Y %H:%M:%S') 
        sunrise_string = sunrise.strftime('%b-%d-%Y %H:%M:%S') 
        sunset_string = sunset.strftime('%b-%d-%Y %H:%M:%S')
        result = [long,lat,weather,weather_des,temp_cel,humi,location,datetime_string,sunrise_string,sunset_string]
        return result
    else:
        print('Error')

# function to display the weather details
def final_result(col,row,ind,res): 
    lbl2 = Label(app,text=[ind,res])
    lbl2.grid(column=col,row=row,sticky=W)


def slide():
    # syntax to hide a button or label
    but.grid_forget() 
    lbl.grid_forget()
    txt.grid_forget()
    butt.grid(column=2,row=5)
    city = txt.get()
    if city:
        final = weather_details(city)
        if final:
            # calling function to display weather details
            final_result(1,0,'Longitude:',final[0]) 
            final_result(2,0,'Latitue:',final[1])
            final_result(1,1,'General_Weather:',final[2])
            final_result(2,1,'Weather_Description:',final[3])
            final_result(1,2,'Temperature:','%.2f' %final[4])
            final_result(2,2,'Humidity:',final[5])
            final_result(1,3,'Date_and_Time:',final[7])
            final_result(2,3,'Sunrise_Time:',final[8])
            final_result(1,4,'Sunset_Time:',final[9])
            final_result(2,4,'Location:',final[6])
            butt.grid(column=1,row=5)
        else:
            # create an error box
            messagebox.showerror('Error',f'{city} not found')
    else:
        messagebox.showerror('Error','Input a city')

app = Tk()
app.title('Weather App')
app.geometry('450x200')
lbl = Label(app,text='Enter Location')
lbl.grid(column=1,row=0)
txt = Entry(app,width=20)
txt.grid(column=2,row=0)
but = Button(app,text='Continue',fg='green',width=10,command=slide)
but.grid(column=2,row=1)
butt = Button(app,text='Exit',fg='red',width=4,command=lambda: app.quit())
butt.grid(column=2,row=2)

app.mainloop()

# for image, always PNG
# img = PhotoImage(file=)
# img1 = img.subsample(2,2)