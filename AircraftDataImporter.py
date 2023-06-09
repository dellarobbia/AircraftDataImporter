import pymysql, json, requests

aircraftJsonUrl = 'http://192.168.0.230:8080/data/aircraft.json'

aircraftJsonData = json.loads(requests.get(url = aircraftJsonUrl).text)

connection = pymysql.connect(host = 'localhost', user = 'AircraftDataImporter', passwd = 'dataImporter', db = 'aircraftdb')

cursor = connection.cursor()



for item in aircraftJsonData['aircraft']:
    timestamp = aircraftJsonData['now']
    icao = item.get("hex", 0)
    category = item.get("category", 0)
    altitude = item.get("alt_baro", 0)
    lat = item.get("lat", 0)
    lon = item.get("lon", 0)

    cursor.execute("INSERT INTO aircraft_data (timestamp, icao, category, altitude, lat, lon) VALUES (%s, %s, %s, %s, %s, %s)", (timestamp, icao, category, altitude, lat, lon))

connection.commit()
connection.close()