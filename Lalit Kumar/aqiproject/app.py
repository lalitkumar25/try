from flask import Flask, request, jsonify, send_from_directory, Response
import requests
import threading
import csv
import io
import os
from dotenv import load_dotenv
from flask_cors import CORS


import database


load_dotenv()
API_KEY = os.getenv("OWM_API_KEY")

app = Flask(__name__, static_folder="public", static_url_path="")
CORS(app)


database.init_db()


temp_cache = {}


def get_api_data(url, params):
    
    key = f"{url}{params}"
    
    
    if key in temp_cache:
        return temp_cache[key]
    
    try:
        res = requests.get(url, params=params)
        data = res.json()
        
        if res.status_code == 200:
            temp_cache[key] = data # Save to cache
            return data, 200
        else:
            return data, res.status_code
    except:
        return {"error": "Network issue"}, 500



@app.route("/")
def home():
    return send_from_directory("public", "index.html")

# @app.route("/<path:filename>")
# def assets(filename):
#     return send_from_directory("public", filename)


@app.route("/api/geocode")
def search_city():
    city = request.args.get("q")
    url = "https://api.openweathermap.org/geo/1.0/direct"
    return jsonify(get_api_data(url, {"q": city, "limit": 1, "appid": API_KEY})[0])

# AQI Data
@app.route("/api/aqi")
def aqi_data():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    name = request.args.get("name")
    
    url = "https://api.openweathermap.org/data/2.5/air_pollution"
    data, status = get_api_data(url, {"lat": lat, "lon": lon, "appid": API_KEY})
    
   
    if status == 200 and name:
        try:
            val = data['list'][0]['main']['aqi']
            t = threading.Thread(target=database.save_search, args=(name, val))
            t.start() # Save history
        except:
            pass
            
    return jsonify(data)


@app.route("/api/forecast")
def forecast_data():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    url = "https://api.openweathermap.org/data/2.5/air_pollution/forecast"
    return jsonify(get_api_data(url, {"lat": lat, "lon": lon, "appid": API_KEY})[0])


@app.route("/api/history")
def history():
    return jsonify(database.get_recent_data())

# Download CSV
@app.route("/api/download_csv")
def download():
    data = database.get_all_data()
    
    
    si = io.StringIO()
    writer = csv.writer(si)# CSV 
    writer.writerow(['City Name', 'AQI Level', 'Time'])
    
    for row in data:
        writer.writerow([row["city"], row["aqi"], row["date_time"]])
        
    return Response(
        si.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=history_report.csv"}
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)