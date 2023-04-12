# pi-daily-email
Used to send daily emails with helpful information, such as weather, news, and assignments due. This project uses the Weather API, stock API, and a News API.

This is just to get practice writting in with python and Javascript.
Python is used to get API data, and the write and send an email formatted with html.
Javascript is used to host a website that will display data about system status.

This isn't the most efficient system or the best way to go about writting this program.
I chose to wrote everything this way just to get some practice.

## Frameworks and Libraries
The Python side of the project used used multiprocessing, socket, requests, subprocess, time, and datetime libraries.

The Javascript files used the path, express, and morgan modules

## How to Run
Files can be easily be run after installing the required imports. This can be done with:
```
pip install -r requirements.txt
cd js
npm i
cd ..
```
After everything is installed, run with:
```
python main.py
```
Will run until stopped manually.