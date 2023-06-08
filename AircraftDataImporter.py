import pymysql, json, requests

aircraftJsonUrl = 'https://192.168.0.230:8080/data/aircraft.json'

aircraftJsonData = json.loads(requests.get(url = aircraftJsonUrl).text)['results']

connection = pymysql.connect(host = 'localhost', user = 'AircraftDataImporter', passwd = 'dataImporter', db = 'AircraftDB')

cursor = connection.cursor()

for i, item in enumerate(aircraftJsonData):
    timestamp = item.get("now", None)
    icao = item.get("aircraft.hex", None)
    category = item.get("aircraft.category", None)
    altitude = item.get("aircraft.alt_baro", None)
    lat = item.get("aircraft.lat", None)
    lon = item.get("aircraft.lon", None)

    cursor.execute("INSERT INTO aircraft_data (timestamp, icao, category, altitude, lat, lon) VALUES (%s, %s, %s, %s, %s, %s)", (timestamp, icao, category, altitude, lat, lon))

connection.commit()
connection.close()