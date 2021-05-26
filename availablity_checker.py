import cowin
import time

state = input("Enter your state: ")

STATE_ID = cowin.id_catcher(state, 'state', None)

dist = input("Enter your district: ")
DIST_ID = cowin.id_catcher(dist, 'district', STATE_ID)

age = int(input("Enter your age: "))

# print(cowin.available)

while True:
#     print(cowin.available)
    print()
    print(time.strftime("%H:%M:%S"), "Fetchig data")
    cowin.main(DIST_ID, age)
    if cowin.available:
        break
    time.sleep(30)
