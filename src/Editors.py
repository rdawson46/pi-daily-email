import src.Weather as weather
import src.News as News
from datetime import date

def prepare():
    forecast = weather.getWeather()
    news = News.getNews()

    if news == -1 or forecast == -1:
        return -1

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
        #canvas{
            color: black;
            background-color: navajowhite;
            border-radius: 10px;
            padding: 10px;
            margin: 2.5%;
        }
    </style>
</head>
    """

    body=f"""
<body>
    <div id="top">
        <header>Daily Alerts For {today}</header>
    </div>
    <div class="group">
        <div class="subGroup" id="weather">
            <h3><u>Weather</u></h3>
            <ul>
                <li>Current Temperature: {forecast['Temp']}</li>
                <li>Humidity: {forecast['Humidity']}</li>
                <li>Condition: {forecast['Condition']}</li>
            </ul>
        </div>
        <div class="subGroup" id="news">
            <h3><u>News</u></h3>
            <ul>
                <li>{news[0]}</li>
                <li>{news[1]}</li>
                <li>{news[2]}</li>
            </ul>
        </div>
    </div>
    <div id="canvas">
        <h3><u>Canvas To Do</u></h3>
    </div>
</body>
    """

    with open("page.html", "w") as page:
        page.write(html + body)
    return 0