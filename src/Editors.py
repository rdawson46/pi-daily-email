import src.Weather as weather
from datetime import date

def prepare():
    forecast = weather.getWeather()

    today = date.today()
    today = today.strftime("%B %d, %Y")
    html = """
<!DOCTYPE html>
<head>
    <style>
        body{
            background-color: #161b22;
        }
        header{
            font-size: 18px;
            text-align: center;
        }
        #top{
            border-bottom: solid gray 5px;
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
            margin-bottom: 1.5%;
        }
        .group{
            display: flex;
            justify-content: center;
        }
        .subGroup{
            width: 50%;
            margin: 2.5%;
            padding: 10px;
            border-radius: 10px;
        }
        h3{
            padding:0;
            margin:0;
            font-size: large;
        }
        ul{
            font-size: medium;
            margin-top: 0;
        }
        #weather{
            background-color: lightblue;
            color: black;
        }
        #news{
            background-color: aliceblue;
            color: black;
        }
    </style>
</head>
    """

    body="""
<body>
    <div id="top">
        <header>Daily Alerts For {date}</header>
    </div>
    <div class="group">
        <div class="subGroup" id="weather">
            <h3><u>Weather</u></h3>
            <ul>
                <li>Current Temperature: {temp}</li>
                <li>Humidity: {humid}</li>
                <li>Condition: {condition}</li>
            </ul>
        </div>
        <div class="subGroup" id="news">
            asdfasdfasdfasdf
        </div>
    </div>
</body>
    """.format(date=today, temp=forecast['Temp'], humid=forecast['Humidity'], condition=forecast["Condition"])

    with open("page.html", "w") as page:
        page.write(html + body)