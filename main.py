# Author: Jimmy Vang

import gpsd
import time
from gpsdistcalc import calc_dist
from datetime import datetime

DEBUG = True

if __name__ == "__main__":
    try:
        initGPS = True
        # Set Trigger Distance in meters
        triggerDistance = 0.2
        lat0, lon0 = 0, 0

        while(True):
            # Connect to the local gpsd
            gpsd.connect()

            # Get gps position
            packet = gpsd.get_current()

            # Initilize GPS coordinate with first reading as reference to measure from
            if initGPS:
                lat0, lon0 = packet.lat, packet.lon
                initGPS = False

            if DEBUG:
                # Prints GPS's lat, lon
                print("---Reference GPS---")
                print("rLat: " + str(lat0))
                print("rLon: " + str(lon0))
                print("---Current GPS---")
                print("Lat: " + str(packet.lat))
                print("Lon: " + str(packet.lon))

            lat1, lon1 = packet.lat, packet.lon
            distanceTraveled = calc_dist(lon0, lat0, lon1, lat1)
            if DEBUG:
                # Distance in Meters
                print("Dist: ", round(distanceTraveled,3), "m")

            if distanceTraveled >= triggerDistance:
                # Updates new reference point
                lat0, lon0 = lat1, lon1
                if DEBUG:
                    print('*****New reference point*****')
                    print("Lat: " + str(lat0))
                    print("Lon: " + str(lon0))
                    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
                print("Triggered")
                # Insert commands/scripts to execute when triggered

            time.sleep(1)

    except KeyboardInterrupt:
        print('interrupted!')
