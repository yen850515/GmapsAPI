import googlemaps
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
# 讀config檔案(環境變數)

# 設定API金鑰和地圖客戶端
google_maps_key = config.get('google-maps-api', 'google_maps_api')
gmaps = googlemaps.Client(api_key=google_maps_key)

# 定義兩個位置
origins = ['Taipei Main Station, Taiwan']
destinations = ['Taipei 101, Taiwan']

# 呼叫Distance Matrix API
result = gmaps.distance_matrix(origins, destinations, mode='driving', language='zh-TW', units='metric')

# 解析回傳結果
distance = result['rows'][0]['elements'][0]['distance']['text']
duration = result['rows'][0]['elements'][0]['duration']['text']

# 輸出計算結果
print('距離:', distance)
print('時間:', duration)
