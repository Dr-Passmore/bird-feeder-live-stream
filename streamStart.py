import subprocess
import datetime
import logging

import secretsFile

logging.basicConfig(filename='YouTubeStreaming.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logging.info("Start Stream Script Activated")
current_date = datetime.date.today().strftime("%d-%m-%Y")

print(current_date)
STREAM_KEY = secretsFile.stream_id
try:
    '''raspivid_process = subprocess.Popen([
        "raspivid",
        "-o", "-", "-t", "0", "-vf", "-hf", "-fps", "24", "-b", "14500000",
        "-a", "12", "-ae", "32,0x0,0x0,0x0",
        "|",
        "ffmpeg",
        "-i", "-", "-vcodec", "copy", "-an", "-r", "30", "-g", "60",
        "-vf", "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='%d-%m-%Y %X':fontcolor=white:fontsize=20:x=10:y=10",
        "-f", "flv", "rtmp://a.rtmp.youtube.com/live2/{}".format(STREAM_KEY)
    ])
    
    '''
    raspivid_command = [
    "raspivid", "-o", "-", "-t", "0", "-vf", "-hf", "-fps", "24", "-b", "14500000",
    "-a", "12", "-ae", "32,0x0,0x0,0x0"
    ]
    ffmpeg_command = [
        "ffmpeg", "-i", "-", "-vf",
        "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='%d-%m-%Y %X':fontcolor=white:fontsize=20:x=10:y=10",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "20", "-r", "30", "-g", "60",
        "-f", "flv", "rtmp://a.rtmp.youtube.com/live2/{}".format(STREAM_KEY)
    ]

    raspivid_process = subprocess.Popen(raspivid_command, stdout=subprocess.PIPE)
    ffmpeg_process = subprocess.Popen(ffmpeg_command, stdin=raspivid_process.stdout)

    raspivid_process.stdout.close()
    ffmpeg_process.wait()
    
    logging.info("Stream has completed")
except Exception as e:
    error_message = str(e)
    logging.error("Error: %s", error_message)



