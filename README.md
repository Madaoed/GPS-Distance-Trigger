# GPS-DistanceTrigger
Script using GPS via GPSD for determining distance between GPS coordinates and trigger to run script/commands once traversed distance occurs.  Resets the reference and triggers at next set distance.  Uses the WGS84 reference.

It works with GPSD and GPSD python package to pull the data off a serial/USB GPS and GPSD may need to bet setup.

# Install GPSD (for Ubuntu)
sudo apt install gpsd

# Installed python gpsd and py-proj
pip3 install gpsd-py3 py-proj
