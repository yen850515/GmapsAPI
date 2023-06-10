import googlemaps
from datetime import datetime
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
# 讀config檔案(環境變數)

# 設定 Google Maps API key
google_maps_key = config.get('google-maps-api', 'google_maps_api')
gmaps = googlemaps.Client(key=google_maps_key)

# 設定起點和終點的經緯度座標
origin = '25.0329694,121.5654177'  # 台北101
destination = '24.957848945145425,121.2249924866707'
now = datetime.now()
def directions():
# 設定路線搜尋參數
    directions_result = gmaps.directions(origin,
                                     destination,
                                     mode="driving",
                                     departure_time=now)
    distance = directions_result[0]['legs'][0]['distance']['text']
    times = directions_result[0]['legs'][0]['duration']['text']
    return f"總距離：{distance}\n開車預計時間:{times}"

# print(directions())
# =============================================================                              
# mode="transit",mode="walking"                                 
# 輸出路線距離和預計時間
# print("大眾運輸預計時間：", directions_result_TRANSIT[0]['legs'][0]['duration']['text'])
# print("走路預計時間：", directions_result_WALKING[0]['legs'][0]['duration']['text'])


# 指定API金鑰和要搜尋的地點
api_key = google_maps_key
location = "24.957848945145425,121.2249924866707" 
radius = "100"
type = "restaurant"
language = "zh-TW"

def near_shop_opening(place_id):
    response = requests.get(f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&language={language}&key={api_key}")
    opening_hours = response.json()['result']['current_opening_hours']
    opening_hr = []
    # 擷取營業時間
    for opening_hour in opening_hours.get('weekday_text',''):        
        opening_hr.append(opening_hour)
    return '\n'.join(opening_hr)


def near_shop():
    response = requests.get(f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={type}&language={language}&key={api_key}")
    # 向API發送請求
    if response.status_code == 200:
        results = response.json()["results"]
        # print(results[0])
    else:
        print("搜尋失敗")

    place_id_list = []
    near_shop_list = []

    for result in results[0:5]:
        place_id_list.append(result["place_id"])
        for place_id in place_id_list:
            opening_hours = near_shop_opening(place_id)
        if "rating" not in result.keys():
            continue    
        name = result.get("name")
        address = result.get("vicinity")
        rating = result.get("rating")
        near_shop = f"名稱:{name}\n地址:{address}\n營業時間:\n{opening_hours}\n星級:{rating}"
        near_shop_list.append(near_shop)
    
    return '\n'.join(near_shop_list)

# print(near_shop())

