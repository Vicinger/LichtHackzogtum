import urllib
import time

def blink():
	for i in range(0, 5):
		urllib.urlopen('http://hackzog:8880/RGB?R=255&G=0&B=0')
		time.sleep(1)
		urllib.urlopen('http://hackzog:8880/RGB?R=0&G=0&B=0')
		time.sleep(1)
	return 0	
def blaulicht():
	for i in range(0, 5):
		urllib.urlopen('http://hackzog:8880/RGB?R=0&G=0&B=255')
		time.sleep(1)
		urllib.urlopen('http://hackzog:8880/RGB?R=0&G=0&B=0')
		time.sleep(1)
	return 0

auswahl = 0

while True:
	print("Hauptmenue")
	print("1:Blink")
	print("2:Blaulicht")
	auswahl = input("Ihre Auswahl:")
	if auswahl == 1:
		blink()
	if auswahl == 2:
		blaulicht()
		
