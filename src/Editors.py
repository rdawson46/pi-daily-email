import src.Weather as weather

def prepare():
    forecast = weather.getWeather()
    html = """
    <!DOCTYPE html>
    <head>
        <style>
            header{
                font-size:large;
            }
        </style>
    </head>
    """

    body="""
    <body>
        <header id="main">{temp}</header>
    </body>
    """.format(temp=forecast['Temp'])

    with open("page.html", "w") as page:
        page.write(html + body)