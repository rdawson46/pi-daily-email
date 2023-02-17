import src.SendEmail as SendEmail
import src.Weather as Weather
import src.Editors as Edit
import subprocess

if __name__ == "__main__":
    # subprocess.check_call("npm start", shell=True ,cwd="./js")
    
    Edit.prepare()
    SendEmail.send_email([""])