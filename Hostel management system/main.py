from external import * 
def main():
    sep()
    print("\n","""                      ****MANSAROVER HOSTEL, NORTH CAMPUS***
                               ***DELHI UNIVERSITY***\n
                                1. Register
                                2. Login
                                3. Facilities
                                4. Location\Contact no.
                                5. About Us
                                6. Queries
                                7. Bye :)""")
    def inputmain():
        sep()
        try:
            x=int(input("\nHow Can I help you? "))
            if x==1:
                print("OK!!")
                register()
            if x==2:
                print("OK!!")
                login()
            if x==3:
                print("OK!!")
                facilities()
            if x==4:
                print("OK!!")
                locate()
            if x==5:
                print("OK!!")
                about()
            if x==6:
                print("OK!!")
                contact()
            if x==7:
                print("Thank You!")
            if x>7:
                print("Task not in option")
                inputmain()
        except ValueError:
            print("\nEnter the No. corresponding to the task.")
            inputmain()
    inputmain()

main()
