import time
rebPrice=2280
bikePrice=2100
scoottyPrice=1850
carPrice=3350
print("---- Welcome to Goa ----")
print("Select your type of vehicle")
time.sleep(2)
print("Press 1.Two wheeler 2.Four wheeler")
vehicle=int(input())
if vehicle==1:
    print("Which one do you want rent for your ride?")
    print("Press 1.Bike 2.Scootty")
    twoWheeler=int(input())
    if twoWheeler==1:
        print("Press \n 1.Royal Enfield Bullet 350\n 2.Royal Enfield Bullet 500\n 3.Ducati Super sport\n 4. Yamaha\n")
        bike=int(input())
        if bike in [1,2,3,4]:
            print("For how many days you want to rent it?")
            days = int(input())
            print("The cost per day is", rebPrice)
            print("The cost for the days is", rebPrice * days)
            print("Press 1.continue 2.cancellation")
            choice = int(input())
            if choice == 1:
                print("-------------------------------------------------------")
                print("Enter your Name:")
                name = input()
                print("Enter Aadhaar Number:")
                aadhaar = int(input())
                print("Enter Driving License Number:")
                dL = int(input())
                print("Rental vehicle",bike )
                print("The total cost for", days, " days is",rebPrice*days )
                print("Please pay the cash during pick up.")
                time.sleep(3)
                print("Your booking is confirmed")
                print("Thank You Happy Journey!!")
                print("-------------------------------------------------------")
            elif choice==2:
                print("Your booking has been cancelled.")
            else:
                print("Please Select the correct option.")
        else:
            print("This vehicle is not available.Please select the correct option")
    elif twoWheeler==2:
        print("Press\n 1.Activa\n 2.Pleasure\n")
        scotty=int(input())
        if scotty in [1,2]:
            print("For how many days you want to rent it?")
            days = int(input())
            print("The cost per day is", scoottyPrice)
            print("The cost for the days is", scoottyPrice * days)
            print("Press 1.continue 2.cancellation")
            choice = int(input())
            if choice == 1:
                print("-------------------------------------------------------")
                print("Enter your Name:")
                name = input()
                print("Enter Aadhaar Number:")
                aadhaar = int(input())
                print("Enter Driving License Number:")
                dL = int(input())
                print("Rental vehicle", )
                print("The total cost for", days, "days is",scoottyPrice*days )
                print("Please pay the cash during pick up.")
                time.sleep(3)
                print("Your booking is confirmed")
                print("-------------------------------------------------------")
            else:
                print("Your booking has been cancelled.")
        else:
            print("Please Select the correct option.")
    else:
        print("Invalid option. Please Select correct option.")
elif vehicle==2:
    print("Press 1. Maruti Suzuki 500\n 2. Duster Car\n")
    car=int(input())
    if car in [1,2]:
        print("For how many days you want to rent it?")
        days = int(input())
        print("The cost per day is", carPrice)
        print("The cost for the days is", carPrice * days)
        time.sleep(2)
        print("Press 1.continue 2.cancellation")
        choice=int(input())
        if choice==1:
            print("-------------------------------------------------------")
            print("Enter your Name:")
            name = input()
            print("Enter Aadhaar Number:")
            aadhaar = int(input())
            print("Enter Driving License Number:")
            dL = int(input())
            print("Rental vehicle", )
            print("The total cost for", days, "days is",carPrice*days )
            print("Please pay the cash during pick up.")
            time.sleep(3)
            print("Your booking is confirmed")
            print("-------------------------------------------------------")
        else:
            print("Your booking has been cancelled.")
    else:
        print("Vehicle not found.")
else:
    print("Invalid option selection.")

