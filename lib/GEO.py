import math


def lat_lon_distance_km(one, two):
    R = 6373.0  # radius of the Earth in km, so results in km

    lat1 = math.radians(one[0])
    lon1 = math.radians(one[1])
    lat2 = math.radians(two[0])
    lon2 = math.radians(two[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2  # Haversine formula

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c
