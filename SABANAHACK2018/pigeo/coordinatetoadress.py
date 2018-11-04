from geopy.geocoders import GoogleV3

def GL_to_dir(lat, longit):
    pointx = lat
    pointy = longit
    point = str(pointx)+','+str(pointy)
    geolocator = GoogleV3(api_key="AIzaSyC7ptlYha7iHq9yuHKQ09wLJm1kAYtoSm8")
    address = geolocator.reverse(point, exactly_one=True)
    print(address[0])


