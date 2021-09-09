import pyproj

def calc_dist(lon0, lat0, lon1, lat1):
    geod = pyproj.Geod(ellps='WGS84')
    az1, az2, dist = geod.inv(lon0, lat0, lon1, lat1)
    return dist

if __name__ == "__main__":
    # For Testing  It should give ~45.099 for the distance
    # Can verify using https://www.cqsrg.org/tools/GCDistance/
    gpsTest0 = 64.75769544459295, -147.3538853627688
    gpsTest1 = 64.75787388004592, -147.35473562311543

    lat0, lon0 = gpsTest0
    lat1, lon1 = gpsTest1

    distance = calc_dist(lon0, lat0, lon1, lat1)
    print (f"Distance: %s m" % distance)