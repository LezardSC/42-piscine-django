import sys
import antigravity

def geohashing():
	if len(sys.argv) == 4:
		try:
			latitude = float(sys.argv[1])
		except:
			return print("Error.\nA float is expected for the latitude.")
		try:
			longitude = float(sys.argv[2])
		except:
			return print("Error.\nA float is expected for the longitude.")
		try:
			datedow = sys.argv[3].encode('utf-8')
		except:
			return print("Error.\nA string is expected for the date.")
		geohash = antigravity.geohash(latitude, longitude, datedow)
	else:
		print("Error.\nThe program need 3 values: latitude, longitude and date.")

if __name__ == "__main__":
	geohashing()