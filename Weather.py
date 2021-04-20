import tkinter as tk
from tkinter import font
import requests


def test_function(entry):
    print("This is the entry: ", entry)

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        c = (temp-32)*5/9

        final_str = 'City: %s \nCondition: %s \nTemperature(c): %s' % (name,desc,c)
    except:
        final_str = 'There Was A\nProblem Retrieving\nThat Information'

    return final_str


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = { 'APPID': 'a5ca07d445a2987056811d679e9bbfa9', 'q': city, 'unit': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    print(weather)

    label['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

background_image = tk.PhotoImage(file='weather.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)

frame = tk.Frame(root, bd=10, bg='Tomato')
frame.place(relx=0.1, rely=0.1, relheight=0.14, relwidth=0.8,)

button = tk.Button(frame, text="Get Weather", font=('sans', 10), bd=8, bg='DodgerBlue', command=lambda: get_weather(entry.get()))
button.place(relx=0.79, rely=0.1, relheight=0.8, relwidth=0.2)

entry = tk.Entry(frame, font=('courier', 16), bd=10, bg='white',)
entry.place(relx=0.02, rely=0.1, relheight=0.8, relwidth=0.74)

lower_frame = tk.Frame(root, bg='Tomato')
lower_frame.place(relx=0.1, rely=0.26, relheight=0.6, relwidth=0.8)

label = tk.Label(lower_frame, font=('Rockwell', 18), anchor='nw', justify='left', bd=5)
label.place(relx=0.03, rely=0.05, relheight=0.9, relwidth=0.95)

#print(tk.font.families())

root.mainloop()
