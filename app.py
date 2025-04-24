from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        api_key = "387e2fa91b95188cfd0c40d467c1bc0a"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            weather_data = {
                "city": city.title(),
                "temperature": main["temp"],
                "humidity": main["humidity"],
                "description": weather["description"].capitalize()
            }
        else:
            weather_data = "not_found"
    
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    print("Flask app is starting...")

    app.run(debug=True)
