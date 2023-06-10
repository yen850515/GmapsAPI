import requests
import configparser
import googlemaps

# 讀config檔案(環境變數)
config = configparser.ConfigParser()
config.read('config.ini')
google_maps_key = config.get('google-maps-api', 'google_maps_api')

# 指定API金鑰和要搜尋的地點
api_key = google_maps_key
location = "24.957848945145425,121.2249924866707" # 台北市政府的座標
radius = "100"
type = "restaurant"
language = "zh-TW"

# 向API發送請求
response = requests.get(f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={type}&language={language}&key={api_key}")

# 處理API回應
if response.status_code == 200:
    results = response.json()["results"]
    print(results[0])
else:
    print("搜尋失敗")


for result in results:
    name = result.get("name")
    address = result.get("vicinity")
    if "rating" not in result.keys():
        continue
    rating = result.get("rating","無資料")
    # price_level = result.get("price_level","無資料")
    if "opening_hours" not in result.keys():
        opening_hours = "無資料"
    elif result["opening_hours"]["open_now"] == True:
        opening_hours = "是"
    else:
        opening_hours = "否"
    print(f"{name}: {address}，現在是否有營業: {opening_hours}，星級: {rating}")
