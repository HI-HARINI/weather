from tkinter import *
import requests
import json

root=Tk()
root.overrideredirect(False)
root.geometry("600x600")
root.title("My Weather APP")

cityname=Label(root, text="City Name")
cityname.place(relx=0.5, rely=0.1,anchor=CENTER)

inputbox1=Entry(root)
inputbox1.place(relx=0.5,rely=0.2,anchor=CENTER)

country=Label(root)
country.place(relx=0.5, rely=0.4,anchor=CENTER)

region=Label(root)
region.place(relx=0.5, rely=0.5,anchor=CENTER)

language=Label(root)
language.place(relx=0.5, rely=0.6,anchor=CENTER)

population=Label(root)
population.place(relx=0.5, rely=0.7,anchor=CENTER)

area=Label(root)
area.place(relx=0.5, rely=0.8,anchor=CENTER)

def city_name():
    apirequest=requests.get("https://restcountries.com/v2/capital/" + inputbox1.get())
    
    apioutputjson=json.loads(apirequest.content)
    
    countryinfo=apioutputjson[0]['name']
    print(countryinfo)
    
    regioninfo=apioutputjson[0]['region']
    print(regioninfo)
    
    languageinfo=apioutputjson[0]['demonym']
    print(languageinfo)
    
    populationinfo=apioutputjson[0]['population']
    print(populationinfo)
    
    areainfo=apioutputjson[0]['area']
    print(areainfo)

    
    country["text"]="Country:"+countryinfo
    
    population["text"]="Population:"+str(populationinfo)
    
    region["text"]="Region:"+regioninfo
    
    area["text"]="Area:"+str(areainfo)

    language["text"]="language:"+languageinfo
    

button1=Button(root,text="Show Weather", command=city_name)
button1.place(relx=0.5, rely=0.3,anchor=CENTER)

root.mainloop()
