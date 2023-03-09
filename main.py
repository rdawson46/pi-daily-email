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

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.0.0.0', 0))
    ipAddr = s.getsockname()[0]
    s.close()
    return ipAddr

if __name__ == "__main__":
    ip = getIP()
    jsProcess = multiprocessing.Process(target=hosting, args=(status, ip))
    jsProcess.start()
    print(f'JS server is running on process: {jsProcess.pid}')
    

    while True:
        if datetime.now().hour == 9:
            status = Edit.prepare()
            requests.post(f'http://{ip}:8080/', json={'statusCode': status})

        if status == 0:
            sending()

            sleep(86400)
        else:
            sleep(3600)
    jsProcess.join() # insert after while loop