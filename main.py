import src.SendEmail as SendEmail
import src.Editors as Edit
import subprocess
import multiprocessing
from datetime import datetime
from time import sleep
import socket
import requests


status = 1      # status > 0 is an error code and 0 on success


def hosting(code, ipAddr):
    subprocess.check_call(f'npm start {code} {ipAddr}', shell=True, cwd='./js')

def sending():
    SendEmail.send_email(["dawson4623@gmail.com"])
    

if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())

    # while True:
    # if datetime.now().hour == 9:
    status = Edit.prepare()

    jsProcess = multiprocessing.Process(target=hosting, args=(status, ip))

    if not jsProcess.is_alive():
        jsProcess.start()
        print(f'JS server is running on process: {jsProcess.pid}')
    
    else:
        requests.post(f'http:{ip}:8080/', json={'statusCode': status})

    if status == 0: 
        sending()

    # sleep(86400)
    # else:
    # sleep(3600)
    jsProcess.join() # insert after while loop