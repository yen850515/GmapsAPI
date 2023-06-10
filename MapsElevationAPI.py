import configparser
import googlemaps

config = configparser.ConfigParser()
config.read('config.ini')
# 讀config檔案(環境變數)

google_maps_key = config.get('google-maps-api', 'google_maps_api')
gmaps = googlemaps.Client(key=google_maps_key)

# Define the coordinates for which to obtain elevation data
locations = [(25.0329694,121.5654177), (25.05,121.666)]

# Call the Elevation API to get elevation data for the specified coordinates
# 海拔高度
elevation = gmaps.elevation(locations)

# Print the elevation data for each location
for i in range(len(locations)):
    print("Elevation at location {}: {} meters".format(i+1, elevation[i]['elevation']))


# from usegoogle import directions,near_shop_opening,near_shop
# print(near_shop())