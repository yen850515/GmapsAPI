import googlemaps
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
# 讀config檔案(環境變數)

# 設定API金鑰和地圖客戶端
google_maps_key = config.get('google-maps-api', 'google_maps_api')
gmaps = googlemaps.Client(api_key=google_maps_key)

# 定義要轉換的地址
address = '台灣台北市大安區復興南路一段390號'

# 呼叫Geocoding API
result = gmaps.geocode(address)

# 解析回傳結果
location = result[0]['geometry']['location']
lat = location['lat']
lng = location['lng']

# 輸出計算結果
print('經度:', lng)
print('緯度:', lat)
