import signal
import logging

logging.basicConfig(filename='YouTubeStreaming.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def kill_raspivid(process):
    process.send_signal(signal.SIGINT)
    process.wait()

logging.info("Killing raspivid process")

try:
    kill_raspivid(raspivid_process)
    logging.info("YouTube Live Stream has ended")

except Exception as e:
    error_message = str(e)
    logging.error("Error: %s", error_message)

