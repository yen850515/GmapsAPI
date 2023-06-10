import googlemaps
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
# 讀config檔案(環境變數)

# 設定 Google Maps API key
google_maps_key = config.get('google-maps-api', 'google_maps_api')
gmaps = googlemaps.Client(key=google_maps_key)

# 設定起點和終點的經緯度座標
origin = '25.0329694,121.5654177'  # 台北101
destination = '24.7938079,120.9674791'  # 台中火車站

# 設定路線搜尋參數
now = datetime.now()
directions_result_driving = gmaps.directions(origin,
                                     destination,
                                     mode="driving",
                                     departure_time=now)

directions_result_TRANSIT = gmaps.directions(origin,
                                     destination,
                                     mode="transit",
                                     departure_time=now)

directions_result_WALKING = gmaps.directions(origin,
                                     destination,
                                     mode="walking",
                                     departure_time=now)
# 輸出路線距離和預計時間
# print("總距離：", directions_result_driving[0]['legs'][0]['distance']['text'])
# print("開車預計時間：", directions_result_driving[0]['legs'][0]['duration']['text'])
# print("大眾運輸預計時間：", directions_result_TRANSIT[0]['legs'][0]['duration']['text'])
# print("走路預計時間：", directions_result_WALKING[0]['legs'][0]['duration']['text'])

# 輸出每個步驟的路線指示
# for step in directions_result[0]['legs'][0]['steps']:
#     print(step['html_instructions'])
#     print(step['distance']['text'])
