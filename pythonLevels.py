import sounddevice as sd
import numpy as np
import requests

peaked = int(0)

url = "http://localhost:8069"

data = {
    "action": "JumpScare",  
    "payload": {
        "key1": "test"
    }
}


def run_mic():
    with sd.Stream(callback=print_sound):
        peaked == 1 or input()

def send_message():
    response = requests.post(url, json=data)
    #timer.sleep(1500)
    peaked = int(0)
    run_mic()
    
     

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    #print ("|" * int(volume_norm))
    if int(volume_norm)>30:
        print("PEAK")
        peaked = int(1)
        send_message()   

run_mic()
