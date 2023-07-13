#create config file with current date, start flag, and end flag 

import datetime
import configparser
from astral import LocationInfo
from astral.sun import sun
import pytz
import logging
import os

class AutomatedStartStop:
    
    def __init__(self) -> None:
        currentDate = datetime.date.today()
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        config_file = configparser.ConfigParser()
        sunrise, sunset = AutomatedStartStop.sun_data(self)
        if os.path.exists("config.ini"):
            #update config file if time is different
            print("config exists")
        else:
            AutomatedStartStop.create_config(self, config_file, currentDate, sunrise, sunset)    
        storedDate = config_file.get("YouTube LiveStream", "date")
        print(storedDate)
        print(sunrise)
        print(sunset)
        return 
    
    def create_config(self, config_file, currentDate, sunrise, sunset):
        print(sunrise)
        # ADD SECTION
        config_file.add_section("YouTube LiveStream")

        Youtube_livetream_code = input("Please enter required code")
        # ADD SETTINGS TO SECTION
        config_file.set("YouTube LiveStream", "date", str(currentDate))
        config_file.set("YouTube LiveStream", "Started", "0")
        config_file.set("YouTube LiveStream", "Ended","0")
        config_file.set("YouTube LiveStream", "Code", Youtube_livetream_code)

        self.save_config(config_file)

    def save_config(self, config_file):
        with open(r"config.ini", 'w') as configfileObj:
            config_file.write(configfileObj)
            configfileObj.flush()
            configfileObj.close()
        
    def sun_data(self):
        city = LocationInfo("Falmouth", "England", "Europe/London", 50.15, -5.066)
        timezone = pytz.timezone(city.timezone)
        s = sun(city.observer)
        sunrise = s["sunrise"].astimezone(timezone).strftime("%H:%M:%S")
        sunset = s["sunset"].astimezone(timezone).strftime("%H:%M:%S")
        return sunrise, sunset
    

    '''

    # ADD SECTION
    config_file.add_section("YouTube LiveStream")

    # ADD SETTINGS TO SECTION
    config_file.set("YouTube LiveStream", "date", f"{currentDate}")
    config_file.set("YouTube LiveStream", "Started", "0")
    config_file.set("YouTube LiveStream", "Ended","0")

    # SAVE CONFIG FILE
    
        
    # PRINT FILE CONTENT


    date = config_file.get('YouTube LiveStream', 'date')


    print (date)
    #date = datetime.date(2023, 4, 22)
    city = LocationInfo("Falmouth", "England", "Europe/London", 50.15, -5.066)
    timezone = pytz.timezone(city.timezone)
    s = sun(city.observer)


    print(
        f'Dawn:    {s["dawn"].astimezone(timezone)}\n'
        f'Sunrise: {s["sunrise"].astimezone(timezone)}\n'
        f'Noon:    {s["noon"].astimezone(timezone)}\n'
        f'Sunset:  {s["sunset"].astimezone(timezone)}\n'
        f'Dusk:    {s["dusk"].astimezone(timezone)}\n'
    )

    
    '''
# Logging
logging.basicConfig(filename='BirdFeederLiveStream.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

AutomatedStartStop()

