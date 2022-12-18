from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root=Tk()
root.title("Hari's Air quality detector")
root.geometry("800x40")
root.configure(background='green')

try:
	api_request= requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=10&API_KEY=1415D85E-FB89-40EF-B8F0-63F99A595BC8")
 #As of now there are limited number of API's available. 
 #So only limited cities are available.Here I have used zip code 20002 (Washington). 
 #You can get the required API for your zip code from AirnowAPI.com.
	api=json.loads(api_request.content)
	city=api[0]['ReportingArea']
	quality=api[0]['AQI']
	category=api[0]['Category']['Name']
except Exception as e:
	api="Error..."

myLabel= Label(root, text=city + " Air Quality" + str(quality) + " "+ category, font=("Helvetica", 20), background="green")
myLabel.pack()


root.mainloop()

#https://www.youtube.com/watch?v=vJCjDevYDt8