#create config file with current date, start flag, and end flag 

import datetime
import configparser
from astral import Astral



currentDate = datetime.date.today()

print(currentDate)

config_file = configparser.ConfigParser()

# ADD SECTION
config_file.add_section("YouTube LiveStream")

# ADD SETTINGS TO SECTION
config_file.set("YouTube LiveStream", "date", f"{currentDate}")
config_file.set("YouTube LiveStream", "Started", "0")
config_file.set("YouTube LiveStream", "Ended","0")

# SAVE CONFIG FILE
with open(r"config.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()
    
# PRINT FILE CONTENT


date = config_file.get('YouTube LiveStream', 'date')


print (date)