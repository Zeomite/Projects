import mysql.connector as sql
conn=sql.connect(host = 'localhost',user='root',passwd='varun',database='movie')
c1=conn.cursor()
block=''
k=''
def sep():
    print("_ "*40)
                        

def contact():
    sep()
    print("\n                            *QUERIES*")
    a=input("Name: ")
    b=input("Email: ")
    c=input("Phone: ")
    d=input("Message: ")
    data=(a,b,c,d)
    import csv
    with open('Queries.csv','a',newline="")as dem:
        csv_writer=csv.writer(dem)
        csv_writer.writerow(data)
    dem.close()
    print("\nWe'll try to contact you soon. Thank you")
    sep()
    x=input("\nFor main menu press 1 or press any other key to stop")
    if b=="1":
        main()
    else:
        sep()
        print("Thank You!")
    

def about():
    sep()
    print("\n                                *ABOUT US*")
    print("\nMansarowar Hostel was established in the year 1993. It is a Men's Hall of residence \nfor full -time post-graduate and research students of the University of Delhi. \nThe hostel is centrally located in the North Campus opposite of Khalsa College and \nadjoining International Students' Hostel for Boys. It is half a kilometre from the \nVishwavidyalya Metro Station and the Faculty of Arts & Social ciences.\n\nThe Provost is the administrative head of the Hostel. For the administrative purposes, \nhe is assisted by the Warden, who is in-charge of the day today affairs of the hostel \nand the Resident Tutor, who looks after the extra-curricular activities and general \nwelfare of the residents. The Provost, Warden and the Resident Tutor are appointed \nby the Vice-Chancellor on behalf of the Executive Council of the University.\n\nThe Hostel Managing Committee is constituted by the University which supervises the \nadministration of the Hostel. The policies of the hostel are decided by the Managing \nCommittee under the overall guidelines and policies of the University of Delhi. The \ndecision of the Managing Committee of the hostel regarding duration of stay, allotment \nof seats to different disciplines/subjects/categories, residents and guest status, fees \nand other rules for residents is final and binding.")
    sep()
    b=input("\nFor main menu press 1 or press any other key to stop")
    if b=="1":
        main()
    else:
        sep()
        print("Thank You!")

def locate():
    sep()
    print("\nMansarover (Hostel)\nNear Khalsa College\nUniversity of Delhi\nDelhi-110007.\n\nPhone +91-11-27667272 x 1727 (EPABX)")
    sep()
    b=input("\nFor main menu press 1 or press any other key to stop")
    if b=="1":
        main()
    else:
        sep()
        print("Thank You!")
                            
def facilities():
    sep()
    print("\n                               *FACILITIES*")
    print("\n1.) DINING HALL\nThe Dining Hall serves quality vegetarian and Non-vegetarian food for its \nresident members. Guests and others may have meals after buying coupons for the \npurpose.Reading RoomA well-lit furnished AC room provides good space for \nstudying/reading. The reading room is not meant for the guests of the residents or \nthe outsiders.\n\n2.) COMPUTER/INTERNET ROOM\nThe computer with internet facility is available for all bonafide residents. The \ncomputer connected to the University network can be accessed for academic pursuits. \nThe residents first must sign the register kept by the attendant of computer room. \nThe computer room is not meant for the guests of the residents or the outsiders.\n\n3.) COMMON ROOM\nThe common room is equipped with a big screen TV set with cable connection. \nNewspapers and magazines are available for the residents. The facility provided in the \ncommon room is strictly for the bonafide resident members only, and not their guests \nor outsiders.\n\n4.) GYMNASIUM\nA gymnasium on the top floor is equipped with a number of modern machines, which help \nthe residents to exercise and keep themselves fit & healthy.\n\n5.) GUEST ROOM\nThe hostel has one furnished guest room. The room is available for the parents and \nimmediate family members of the residents, visiting Scholars and researchers. The room \nhas to be booked in advance through the Hostel office on payment of the rent as per \nrules. The check-out timing from the Guest room will be before 12 p.m. (Noon).")
    sep()
    b=input("\nFor main menu press 1 or press any other key to stop")
    if b=="1":
        main()
    else:
        sep()
        print("Thank You!")  

def login():
    sep()
    print("\n                               *LOGIN PAGE*")
    import csv
    with open('database.csv','r')as file:
        reader=csv.reader(file)
        next(reader)
        eml=[]
        pas=[]
        for row in reader:
            eml.append(row[1])
            pas.append(row[2])
        def rep():
            try:
                em=input("\nEmail: ")
                for i in range(len(eml)+1):
                    
                    if em==eml[i]:
                        pa=input("\npassword: ")
                        if pa==pas[i]:
                            print("\nLogin Sucessful")
                            def person():
                                sep()
                                print("\n                          *PERSONAL DETAILS*")
                                import csv
                                with open('database.csv','r')as file:
                                    reader=csv.reader(file)
                                    next(reader)
                                    eml=[]
                                    for row in reader:
                                        eml.append(row[1])
                                    for i in range(len(eml)):
                                            if em==eml[i]:
                                                count=0
                                                import csv
                                                with open('database.csv','r')as file:
                                                    reader=csv.reader(file)
                                                    next(reader)
                                                    for row in reader:
                                                        if count==i:
                                                            print("Name: ",row[0],"\nEmail: ",row[1],"\nCourse: ",row[4],"\nMobile no.: ",row[6],"\nAddmision no.: ",row[8])
                                                            print("\n","""                               WELCOME""",row[0],"""

                                   1. Book Hostel Room
                                   2. Fee Due
                                   3. Last Transactions
                                   4. Change Account Data
                                   5. Log out to main menu
                                   6. Bye :)""")
                                                            def inputmain2():
                                                                sep()
                                                                try:
                                                                    x=int(input("\nHow Can I help you? "))
                                                                    if x==1:
                                                                        print("OK!!")
                                                                        def book_hostel():
                                                                            sep()
                                                                            print("                           *BOOKING PORTAL*")
                                                                            def f():
                                                                                k=input("Type of room Available:-(Advance of Rs.2000 to be submitted)\n1.Non-AC Fee/month=Rs13000        2. Ac Fee/month=Rs18000\n\nWhat do you want?")
                                                                                if k!="1" and k!="2":
                                                                                    print("Not In option")
                                                                                    f()
                                                                                if k=="1":
                                                                                    room="Non AC"
                                                                                    fee="13000"
                                                                                if k=="1":
                                                                                    room="AC"
                                                                                    fee="18000"
                                                                            f()
                                                                            
                                                                            def exl():
                                                                                block=input("Enter the block of hostel (A,B or C): ")
                                                                                block=block.upper()
                                                                                
                                                                                
                                                                                if block not in ['A','B','C']:
                                                                                    print("Not in option")
                                                                                    exl()
                                                                            exl()
                                                                            
                                                                            print(block)
                                                                            
                                                                            with open('database.csv','r')as file:
                                                                                reader=csv.reader(file)
                                                                                next(reader)
                                                                                for row in reader:
                                                                                    eml=[]
                                                                                    for row in reader:
                                                                                        eml.append(row[1])
                                                                                    for i in range(len(eml)):
                                                                                        if em==eml[i]:
                                                                                            count=0
                                                                                            if count==i:
                                                                                                rn=row[1]
                                                                                            else:
                                                                                                count+=1
                                                                                        
                                                                            date=input("Date of arrival: ")
                                                                            def lm():
                                                                                try:
                                                                                    m=int(input("Stay Duration(in Months): "))
                                                                                except ValueError:
                                                                                    print("Invalid")
                                                                                    lm()
                                                                            lm()
                                                                            from datetime import datetime
                                                                            now=datetime.now()
                                                                            
                                                                            import random
                                                                            mi = pow(10, 2)
                                                                            ma = pow(10, 3) - 1
                                                                            n=random.randint(mi, ma)
                                                                            s=input("\npress any key to pay")
                                                                            print("Your room number is: ",n)
                                                                            with open('database.csv','r')as file:
                                                                                reader=csv.reader(file)
                                                                                next(reader)
                                                                                l1=[]
                                                                                l2=[]
                                                                                for row in reader:
                                                                                    if row[1]!=em:
                                                                                        l1.append(row)
                                                                                    if row[1]==em:
                                                                                        l2.append(row)
                                                                                with open('database.csv','w',newline="")as file:         
                                                                                    csv_writer=csv.writer(file)
                                                                                    c=["Name","Email","password","nationality","Course","Father's_Name","Mobile_No.","Address","Admiss_no.","Fee_due","Room_Num","Block"]
                                                                                    csv_writer.writerow(c)
                                                                                    for i in l1:
                                                                                        csv_writer.writerow(i)
                                                                                    l2[0][10]=n
                                                                                    l2[0][11]=block
                                                                                    l2[0][9]=k
                                                                                    for i in l2:
                                                                                        csv_writer.writerow(i)
                                                                                    file.close()
                                                                                with open('Bookings.csv','a',newline="")as sa:
                                                                                    csv_writer2=csv.writer(sa)
                                                                                    with open('trans.csv','a',newline="")as fo:
                                                                                        csv_writer1=csv.writer(fo)
                                                                                        import random
                                                                                        mi = pow(10,4)
                                                                                        ma = pow(10,5)-1
                                                                                        bookid=random.randint(mi, ma)
                                                                                        transid=random.randint(mi, ma)
                                                                                        print("Your Transaction Id: ",transid)
                                                                                        datax=[transid,rn,em,fee,"Hostel booking",now]
                                                                                        csv_writer1.writerow(datax)
                                                                                        datay=[bookid,rn,em,room,n,b,date,m,"2000","Hostel booking",now]
                                                                                        print("Your Transaction Id: ",bookid)
                                                                                        print("\n\nBooking Successful!\n")
                                                                                        s=input("Press any key to go to personal page ")
                                                                                        person()
                                                                                    fo.close()
                                                                                sa.close()

                                            
                                                                            
                                                                            
                                                                        book_hostel()
                                                                    if x==2:
                                                                        print("OK!!")
                                                                        def feepay():
                                                                            from datetime import datetime
                                                                            now=datetime.now()
                                                                            import csv
                                                                            with open('database.csv','r+')as file:
                                                                                reader=csv.reader(file)
                                                                                next(reader)
                                                                                eml=[]
                                                                                for row in reader:
                                                                                    eml.append(row[1])
                                                                                for i in range(len(eml)):
                                                                                        if em==eml[i]:
                                                                                            count=0
                                                                                            import csv
                                                                                            with open('database.csv','r+')as file:
                                                                                                reader=csv.reader(file)
                                                                                                next(reader)
                                                                                                for row in reader:
                                                                                                    if count==i:
                                                                                                        sep()
                                                                                                        print("\n                           *FEE PAYMENT*")
                                                                                                        print("\nFee Due: ",row[9])
                                                                                                        if row[9]=="0":
                                                                                                            print("Paid Already \n\nThank You")
                                                                                                            v=input("\nEnter any key to go back to student page")
                                                                                                            main()   
                                                                                                        else:
                                                                                                            s=int(input("enter 2 for payment and any other key for main menu"))
                                                                                                            if s==2:
                                                                                                                sep()
                                                                                                                a=int(input("\nEnter amount: "))
                                                                                                                b=str(int(row[9])-a)
                                                                                                                rn=row[0]
                                                                                                                with open('database.csv','r+')as file:
                                                                                            
                                                                                                                    reader=csv.reader(file)
                                                                                                                    next(reader)
                                                                                                                    l1=[]
                                                                                                                    l2=[]
                                                                                                                    for row in reader:
                                                                                                                        if row[1]!=em:
                                                                                                                            l1.append(row)
                                                                                                                        if row[1]==em:
                                                                                                                            l2.append(row)
                                                                                                                with open('database.csv','w',newline="")as file:         
                                                                                                                    csv_writer=csv.writer(file)
                                                                                                                    x=["Name","Email","password","nationality","Course","Father's_Name","Mobile_No.","Address","Admiss_no.","Fee_due","Room_Num","Block"]
                                                                                                                    csv_writer.writerow(x)

                                                                                                                    for i in l1:
                                                                                                                        csv_writer.writerow(i)
                                                                                                                    l2[0][9]=b
                                                                                                                    for i in l2:
                                                                                                                        csv_writer.writerow(i)
                                                                                                                file.close()
                                                                                                                print("transaction successful!")
                                                                                                                with open('trans.csv','a',newline="")as fo:
                                                                                                                    csv_writer1=csv.writer(fo)
                                                                                                                    import random
                                                                                                                    mi = pow(10,4)
                                                                                                                    ma = pow(10,5)-1
                                                                                                                    transid=random.randint(mi, ma)
                                                                                                                    
                                                                                                                    print("Your Transaction Id: ",transid)
                                                                                                                    data=[transid,rn,em,a,"Fee payment",now]
                                                                                                                    csv_writer1.writerow(data)
                                                                                                                    s=input("Press any key to go to personal page ")
                                                                                                                    person()
                                                                                                                fo.close()
                                                                                                                    
                                                                                                            else:
                                                                                                                main()
                                                                                                    else:
                                                                                                        count+=1
                                                                            sep()
                                                                            s=input("\nPress any key to go to personal page ")
                                                                            person()     
                                                                        feepay()
                                                                    if x==3:
                                                                        print("OK!!")
                                                                        def trans():
                                                                            import csv
                                                                            with open('trans.csv','r')as file:
                                                                                reader=csv.reader(file)
                                                                                next(reader)
                                                                                eml=[]
                                                                                for row in reader:
                                                                                    eml.append(row[2])
                                                                                    
                                                                                sep()
                                                                                print("\nTransaction Id, Amount, Purpose, Time")
                                                                                for i in range(len(eml)):
                                                                                        if em==eml[i]:
                                                                                            count=0
                                                                                            import csv
                                                                                            with open('trans.csv','r')as file:
                                                                                                reader=csv.reader(file)
                                                                                                next(reader)
                                                                                                for row in reader:
                                                                                                    if count==i:
                                                                                                        print([row[0],row[3],row[4],row[5]])
                                                                                                        break
                                                                                                    else:
                                                                                                        count+=1
                                                                                sep()
                                                                                s=input("\nPress any key to go to personal page ")
                                                                                person()                           
                                                                                        
                                                                                            
                                                                        trans()
                                                                    if x==4:
                                                                        print("OK!!")
                                                                        def change_data():
                                                                            def repe():
                                                                                sep()
                                                                                m=int(input("\nWhat do you wanna change??\n\n1. Email\n2. Password\n3. Mobile number\n4. Address\n\nENTER HERE: "))
                                                                                try:
                                                                                    if m==1:
                                                                                        print("OK!!\n")
                                                                                        sep()
                                                                                        a=input("\nEnter New Email: ")
                                                                                        import re
                                                                                        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
                                                                                        ar=True
                                                                                        while ar==True:
                                                                                            if(re.search(regex,a)):
                                                                                                ar=False
                                                                                                continue
                                                                                            else:
                                                                                                print("  invalid email ")
                                                                                                email=input("\nEnter New Email: ")
                                                                                                a=email
                                                                                                ar=True
                                                                                        with open('database.csv','r')as file:
                                                                                            reader=csv.reader(file)
                                                                                            next(reader)
                                                                                            l1=[]
                                                                                            l2=[]
                                                                                            for row in reader:
                                                                                                if row[1]!=em:
                                                                                                    l1.append(row)
                                                                                                if row[1]==em:
                                                                                                    l2.append(row)
                                                                                            with open('database.csv','w',newline="")as file:         
                                                                                                csv_writer=csv.writer(file)
                                                                                                x=["Name","Email","password","nationality","Course","Father's_Name","Mobile_No.","Address","Admiss_no.","Fee_due","Room_Num","Block"]
                                                                                                csv_writer.writerow(x)
                                                                                                for i in l1:
                                                                                                    csv_writer.writerow(i)
                                                                                                l2[0][1]=a
                                                                                                for i in l2:
                                                                                                    csv_writer.writerow(i)
                                                                                            
                                                                                                print("\nUpdated Successfully")
                                                                                                sep()
                                                                                                s=input("\nPress 1 for change data page, 2 to quit and any other key to o to personal page ")
                                                                                                if s=="1":
                                                                                                    file.close()
                                                                                                    change_data()
                                                                                                if s=="2":
                                                                                                    print("Thank You")
                                                                                                else:
                                                                                                    file.close()
                                                                                                    person()
                                                                                            file.close()
                                                                                    if m==2:
                                                                                        print("OK!!\n")
                                                                                        sep()
                                                                                        a=int(input("\nEnter New Password: "))
                                                                                       
                                                                                        z=input('Re-enter password: ')
                                                                                        while z!=a:
                                                                                            print (" ERROR:password does not match ")
                                                                                            z=input('Re-enter password: ')
                                                                                        with open('database.csv','r')as file:
                                                                                            reader=csv.reader(file)
                                                                                            next(reader)
                                                                                            l1=[]
                                                                                            l2=[]
                                                                                            for row in reader:
                                                                                                if row[1]!=em:
                                                                                                    l1.append(row)
                                                                                                if row[1]==em:
                                                                                                    l2.append(row)
                                                                                            with open('database.csv','w',newline="")as file:         
                                                                                                csv_writer=csv.writer(file)
                                                                                                x=["Name","Email","password","nationality","Course","Father's_Name","Mobile_No.","Address","Admiss_no.","Fee_due","Room_Num","Block"]
                                                                                                csv_writer.writerow(x)
                                                                                                for i in l1:
                                                                                                    csv_writer.writerow(i)
                                                                                                l2[0][2]=a
                                                                                                for i in l2:
                                                                                                    csv_writer.writerow(i)
                                                                                                print("\nUpdated Successfully")
                                                                                                sep()
                                                                                                s=input("\nPress 1 for change data page, 2 to quit and any other key to o to personal page ")
                                                                                                if s=="1":
                                                                                                    file.close()
                                                                                                    change_data()
                                                                                                if s=="2":
                                                                                                    print("Thank You")
                                                                                                else:
                                                                                                    csv_writer.writerow(x)
                                                                                                    person()
                                                                                            file.close()
                                                                                        
                                                                                    if m==3:
                                                                                        
                                                                                        print("OK!!\n")
                                                                                        sep()
                                                                                        def mob():
                                                                                            try:
                                                                                                h=int(input('Mobile No.: '))
                                                                                            except ValueError:
                                                                                                print(" invalid number ")
                                                                                                mob()
                                                                                        mob()
                                                                                        
                                                                                        with open('database.csv','r')as file:
                                                                                            reader=csv.reader(file)
                                                                                            next(reader)
                                                                                            l1=[]
                                                                                            l2=[]
                                                                                            for row in reader:
                                                                                                if row[1]!=em:
                                                                                                    l1.append(row)
                                                                                                if row[1]==em:
                                                                                                    l2.append(row)
                                                                                            with open('database.csv','w',newline="")as file:         
                                                                                                csv_writer=csv.writer(file)
                                                                                                x=["Name","Email","password","nationality","Course","Father's_Name","Mobile_No.","Address","Admiss_no.","Fee_due","Room_Num","Block"]
                                                                                                csv_writer.writerow(x)
                                                                                                for i in l1:
                                                                                                    csv_writer.writerow(i)
                                                                                                l2[0][6]=h
                                                                                                for i in l2:
                                                                                                    csv_writer.writerow(i)
                                                                                                print("\nUpdated Successfully")
                                                                                                sep()
                                                                                                s=input("\nPress 1 for change data page, 2 to quit and any other key to o to personal page ")
                                                                                                if s=="1":
                                                                                                    file.close()
                                                                                                    change_data()
                                                                                                if s=="2":
                                                                                                    print("Thank You")
                                                                                                else:
                                                                                                    file.close()
                                                                                                    person()               
                                                                                            file.close()
                                                                                    if m==4:
                                                                                        print("OK!!\n")
                                                                                        ml=input('New Address: ')
                                                                                        with open('database.csv','r')as file:
                                                                                            reader=csv.reader(file)
                                                                                            next(reader)
                                                                                            l1=[]
                                                                                            l2=[]
                                                                                            for row in reader:
                                                                                                if row[1]!=em:
                                                                                                    l1.append(row)
                                                                                                if row[1]==em:
                                                                                                    l2.append(row)
                                                                                            with open('database.csv','w',newline="")as file:         
                                                                                                csv_writer=csv.writer(file)
                                                                                                x=["Name","Email","password","nationality","Course","Father's_Name","Mobile_No.","Address","Admiss_no.","Fee_due","Room_Num","Block"]
                                                                                                csv_writer.writerow(x)
                                                                                                for i in l1:
                                                                                                    csv_writer.writerow(i)
                                                                                                l2[0][7]=ml
                                                                                                for i in l2:
                                                                                                    csv_writer.writerow(i)
                                                                                                print("\nUpdated Successfully")
                                                                                                sep()
                                                                                                s=input("\nPress 1 for change data page, 2 to quit and any other key to o to personal page ")
                                                                                                if s=="1":
                                                                                                    file.close()
                                                                                                    change_data()
                                                                                                if s=="2":
                                                                                                    print("Thank You")
                                                                                                else:
                                                                                                    file.close()
                                                                                                    person()
                                                                                            file.close()
                                                                                    if m>4:
                                                                                        print("Task not in option")
                                                                                        inputmain()
                                                                                except ValueError:
                                                                                    print("\nEnter the No. corresponding to the task.")
                                                                                    repe()
                                                                            repe()
                                                                        change_data()
                                                                    if x==5:
                                                                        main()
                                                                    if x==6:
                                                                        print("Thank You!!")
                                                                    if x>6:
                                                                        print("Task not in option")
                                                                        inputmain2()
                                                                except ValueError:
                                                                    print("\nEnter the No. corresponding to the task.")
                                                                    inputmain2()
                                                            inputmain2()
                                                            

                                                        else:
                                                            count+=1
                                            
                            person() 
                        else:
                            continue
                        
                    else:
                        continue
            except IndexError:
                print("Invalid email or password")
                s=input("Press 1 for main menu or press any other key to continue login")
                if s=="1":
                    main()
                else:
                    rep()
                
            
                    
    rep()
    
def register():
    import random
    mi = pow(10, 4)
    ma = pow(10, 5) - 1
    n=random.randint(mi, ma)
    sep()
    print("\n                           *REGISTERATION PORTAL*")
    a=input('Name:')
    i=input('Email:')
    import re
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    ar=True
    while ar==True:
        if(re.search(regex,i)):
            ar=False
            continue
        else:
            print("  invalid email ")
            email=input('Email: ')
            i=email
            ar=True
    l=input('password: ')
    z=input('Re-enter password: ')
    while z!=l:
        print (" ERROR:password does not match ")
        z=input('Re-enter password: ')
    c=input('Nationality: ')
    e=input("Course (Section): ")
    f=input("Father's Name: ")
    def mob():
        try:
            h=int(input('Mobile No.: '))
        except ValueError:
            print(" invalid number ")
            mob()
    mob()
    j=input('Address: ')
    data=(a,i,l,c,e,f,z,j,n,"13000",'','')
    c1.execute("insert into excel_table",data,";")
    c1.commit()
    print("Registration sucessful")
    file.close()
    print("Your Admission No. is ",n)
    sep()
    b=input("\nFor main menu press 1 or press any other key to stop")
    if b=="1":
        
        main()
    else:
        sep()
        
        print("Thank You!")
        
    


