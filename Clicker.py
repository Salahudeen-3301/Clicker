import pyautogui
from time import sleep

repeats = -1
time_interval = -1
know_cords = -1
confirm = "False"
coordinates = "m"


while repeats < 1:
    repeats = int(input("1. Enter the number of repeats for the Autoclicker: "))
while time_interval < 0:
    time_interval = float(input("2. Enter the time interval between each click for the Autoclicker: "))
while know_cords not in ["A", "B"]:
    know_cords = input(
        "3. If you are aware of the co-ordinates you wish to click at - press A\nIf you do not know them, and wish to "
        "be quided through it- press B\nEnter your answer here:  ")

while know_cords == "A" and confirm == "False":
    x = int(input("\nEnter the X co-ordinates for the click: "))
    y = int(input("Enter the Y co-ordinates for the click: "))
    coordinates = (x, y)
    print("\nThe co-ordinates you wish to repeat are: ", coordinates,
          ". The mouse will now move to this position, please let go of the mouse.")
    sleep(3)
    pyautogui.moveTo(coordinates)
    confirm = input("\nAre these co-ordinates correct? (True/False): ")

while know_cords == "B" and confirm == "False":
    print("\nYou have 10 seconds to place the mouse in the location you wish to Autoclick at")
    sleep(10)
    coordinates = pyautogui.position()
    print("\nThe co-ordinates you wish to repeat are: ", coordinates,
          ". The mouse will now move to this position, please let go of the mouse.")
    sleep(3)
    pyautogui.moveTo(coordinates)
    confirm = input("\nIs this location correct? (True/False): ")

print("\nClicking will start in 5 seconds, then proceed with the set time interval")
sleep(5)
if coordinates == "m":
    print("Your program has an error")
    exit()
for i in range(repeats):
    pyautogui.click(coordinates)
    sleep(time_interval)
