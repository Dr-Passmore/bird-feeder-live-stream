import subprocess
import datetime
#from googleapiclient.discovery import build
#from google.oauth2 import service_account
import logging

logging.basicConfig(filename='YouTubeStreaming.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logging.info("Start Stream Script Activated")
current_date = datetime.date.today().strftime("%d-%m-%Y")

print(current_date)
STREAM_KEY = ""

raspivid_process = subprocess.Popen([
    "raspivid",
    "-o", "-", "-t", "0", "-vf", "-hf", "-fps", "15", "-b", "4500000",
    "-a", "12", "-ae", "32,0x0,0x0,0x0",
    "|",
    "ffmpeg",
    "-i", "-", "-vcodec", "copy", "-an", "-r", "30", "-g", "30",
    "-f", "flv", f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
])



