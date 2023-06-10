import signal
import logging

def kill_raspivid(process):
    process.send_signal(signal.SIGINT)
    process.wait()

kill_raspivid(raspivid_process)

logging.basicConfig(filename='YouTubeStreaming.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')