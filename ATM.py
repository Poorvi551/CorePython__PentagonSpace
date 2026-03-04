import time
Balance=12000
password=5678
print("Welcome to ATM")
time.sleep(2)
print("Insert your ATM card")
time.sleep(2)
print("press 1.yes 2.no")
card=int(input())
if card==1:
    print("Please select your language:")
    print("press 1.English 2.Kannada 3.Telugu")
    language=int(input())
    if language==1:
        print("Enter pin:")
        pin=int(input())
        if pin==password:
            print("Select an option")
            print("press 1.Bank Enquiry 2.Withdrawal")
            choice=int(input())
            if choice==1:
                print("Your available balance is",Balance)
            elif choice==2:
                print("Enter the Amount: ")
                Amount=int(input())
                if Amount<Balance and Amount%100==0:
                        print("Transaction is Processing")
                        time.sleep(5)
                        print("Collect Your Cash")
                        time.sleep(5)
                        print("Do you Want to check your balance")
                        print("press 1.yes 2.no")
                        check=int(input())
                        if check==1:
                            print("Your Current Balance is",Balance-Amount)
                            print("Thank You visit Again.")
                        else:
                            print("Thank you Visit Again.")
                elif Amount>Balance:
                    print("Insufficient Balance for transaction.")
                else:
                    print("Invalid amount entered.")
            else:
                print("Incorrect Choice")
        else:
            print("Incorrect pin.")
    else:
        print("Please select your language as english.")
else:
    print("Card is not inserted properly.")
