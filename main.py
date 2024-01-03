import mysql.connector
mydb=mysql.connector.connect (host="localhost", user="root", password="tanuj14@sql")

#CREATING DATABASE AND TABLE
mycursor=mydb.cursor()
mycursor.execute("create database if not exists store")
mycursor.execute("use store")
mycursor.execute("create table if not exists signup(username varchar(20) unique key,password varchar(20))")

while True:
    print("\n1:SIGNUP (create new account)\n2:LOGIN (open existing account)")
    ch=int(input("\nEnter your choice(1,2): "))


#SIGNUP
    if ch==1:

        username=input("\nUSERNAME: ")
        pw=input("PASSWORD: ")

        mycursor.execute("insert into signup values('"+username+"','"+pw+"')")
        mydb.commit()
        print("\nSigned up successfully!!!")

#LOGIN
    elif ch==2:

        username=input("\nUSERNAME: ")

        mycursor.execute("select username from signup where username='"+username+"'")
        pot=mycursor.fetchone()

        if pot is not None:
            print("USERNAME VALID!!!")
            pw=input("\nPASSWORD: ")

            mycursor.execute("select password from signup where password='"+pw+"'")
            a=mycursor.fetchone()

            if a is not None:
                print("PASSWORD VALID!!!")
                print("""
+---------------------------+
|     LOGIN SUCCESSFULL     |
+---------------------------+""")

                print("""
                
+-----------------------------------------------------------------------+
|++++++++++++++++++++++    REGULAR BOOK STORE     ++++++++++++++++++++++|
+-----------------------------------------------------------------------+\n\n""")

                mycursor.execute("create table if not exists Available_Books(BookName varchar(30) primary key,Genre varchar(20),Quantity int(3),Author varchar(20),Publication varchar(30),Price int(4))")
                mycursor.execute("create table if not exists Sell_rec(CustomerName varchar(20),PhoneNumber char(10) unique key, BookName varchar(30),Quantity int(100),Price int(4),foreign key (BookName) references Available_Books(BookName))")
                mycursor.execute("create table if not exists Staff_details(Name varchar(30), Gender varchar(10),Age int(3), PhoneNumber char(10) unique key , Address varchar(40))") 
                mydb.commit()

                while(True):
                    print("""1: Add Books
2: Sell Books
3: Search Books
4: Staff Details
5: Sell Records details
6: Available Books
7: Total Income after the Latest Reset 
8: Exit""")

                    a=int(input("\nEnter your choice: "))

    #ADDING BOOKS
                    if a==1:

                        print("\nPlease fill all the information\n")
                    
                        book=str(input("Book Name: "))
                        genre=str(input("Genre: "))
                        quantity=int(input("Quantity: "))        
                        author=str(input("Author name: "))
                        publication=str(input("Publication house: "))
                        price=int(input("Price(1 book only): "))

                        mycursor.execute("select * from Available_Books where bookname='"+book+"'")
                        row=mycursor.fetchone()

                        if row is not None:
                            mycursor.execute("update Available_Books set quantity=quantity+'"+str(quantity)+"' where bookname='"+book+"'")
                            mydb.commit()

                            print("""
+----------------------+
|  SUCCESSFULLY ADDED  |
+----------------------+\n""")
                        
                        
                        else:
                            mycursor.execute("insert into Available_Books(bookname,genre,quantity,author,publication,price) values('"+book+"','"+genre+"','"+str(quantity)+"','"+author+"','"+publication+"','"+str(price)+"')")
                            mydb.commit()

                            print("""
+----------------------+
|  SUCCESSFULLY ADDED  |
+----------------------+\n""") 
                   

    #SELL BOOKS
                    elif a==2:                

                        print("Available books...\n")

                        mycursor.execute("select * from Available_Books ")
                        for x in mycursor:
                            print("\n",x)
                      
                        cusname=str(input("Customer name: "))
                        phno=int(input("Phone number: "))
                        book=str(input("Book Name: "))
                        n=int(input("Quantity: "))
                        price=int(input("Total price: "))

                        mycursor.execute("select quantity from available_books where bookname='"+book+"'")
                        lk=mycursor.fetchone()

                        if max(lk)<n:
                            print(n,"Books are not available!!!\n")

                        else:
                            mycursor.execute("select bookname from available_books where bookname='"+book+"'")
                            log=mycursor.fetchone()

                            if log is not None:
                                mycursor.execute("insert into Sell_rec values('"+cusname+"','"+str(phno)+"','"+book+"','"+str(n)+"','"+str(price)+"')")
                                mycursor.execute("update Available_Books set quantity=quantity-'"+str(n)+"' where BookName='"+book+"'")
                                mydb.commit()

                                print("""
+----------------------+
|  BOOK HAS BEEN SOLD  |
+----------------------+\n""")

                            else:
                                print("Book is not available!!!")

    #SEARCH BOOKS ON THE BASIS OF GIVEN OPTIONS
                    elif a==3:

                        print("""\n1:Search by name
2:Search by genre
3:Search by author\n""")

                        l=int(input("Search by?: "))

        #BY BOOKNAME
                        if l==1:
                            o=input("\nEnter Book name to search: ")

                            mycursor.execute("select bookname from available_books where bookname='"+o+"'")
                            tree=mycursor.fetchone()

                            if tree!=None:
                                print("""
+--------------------+
|  BOOK IS IN STOCK  |
+--------------------+\n""")
                           
                                mycursor.execute("select * from available_books where bookname='"+o+"'")

                                for y in mycursor:
                                    print(y,"\n")
                            else:
                                print("\nA book bearing that title is not available!!!\n")

        #BY GENRE
                        elif l==2:
                            g=input("\nEnter genre to search: ")

                            mycursor.execute("select genre from available_books where genre='"+g+"'")
                            poll=mycursor.fetchall()

                            if poll is not None:
                                print("""
+--------------------+
|  BOOK IS IN STOCK  |
+--------------------+\n""")

                                mycursor.execute("select * from available_books where genre='"+g+"'")
#paste above
                                for y in mycursor:
                                    print(y,"\n")

                            else:
                                print("\nA book having that genre is not available!!!\n")


        #BY AUTHOR NAME
                        elif l==3:
                            au=input("\nEnter author to search: ")

                            mycursor.execute("select author from available_books where author='"+au+"'")
                            home=mycursor.fetchall()

                            if home is not None:
                                print("""
+--------------------+
|  BOOK IS IN STOCK  |
+--------------------+\n""")

                                mycursor.execute("select * from available_books where author='"+au+"'")

                                for z in mycursor:
                                    print(z,"\n")

                            else:
                                print("\nBooks of this author is not available!!!\n")
                        mydb.commit()

    #STAFF DETAILS
                    elif a==4:
                        print("\n1: New staff entry")
                        print("2: Remove staff")
                        print("3: Existing staff details\n")

                        ch=int(input("Enter your choice: "))

        #NEW STAFF ENTRY
                        if ch==1:
                            fname=str(input("\nFullname: "))
                            gender=str(input("Gender(M/F/O): "))
                            age=int(input("Age: "))
                            phno=int(input("Phone no.: "))
                            add=str(input("Address: "))

                            mycursor.execute("insert into Staff_details(name,gender,age,phonenumber,address) values('"+fname+"','"+gender+"','"+str(age)+"','"+str(phno)+"','"+add+"')")
                            print("""
+-----------------------------+
| STAFF IS SUCCESSFULLY ADDED |
+-----------------------------+\n""")
                            mydb.commit()

        #REMOVE STAFF
                        elif ch==2:
                            nm=str(input("\nEnter staff name to remove:"))
                            mycursor.execute("select name from staff_details where name='"+nm+"'")
                            toy=mycursor.fetchone()

                            if toy is not None:
                                mycursor.execute("delete from staff_details where name='"+nm+"'")
                                print("""
+-------------------------------+
| STAFF IS SUCCESSFULLY REMOVED |
+-------------------------------+\n""")
                                mydb.commit()

                            else:
                                print("\nSTAFF DOESNOT EXIST!!!\n")

        #EXISTING STAFF DETAILS
                        elif ch==3:
                            mycursor.execute("select * from Staff_details")
                            run=mycursor.fetchall()
                            
                            if run is not None:
                                print("\nEXISTING STAFF DETAILS...")                        
                                for t in run:
                                    print(t)
                                print("")
                            else:
                                print("\nNO STAFF EXISTS!!!\n")
                            mydb.commit()

    #SELL HISTORY                                
                    elif a==5:
                        print("\n1: Sell history details")
                        print("2: Reset Sell history\n")

                        ty=int(input("Enter your choice: "))

                        if ty==1:
                            mycursor.execute("select * from sell_rec")
                            for u in mycursor:
                                print("\n",u,"\n")

                        if ty==2:
                            bb=input("\nAre you sure(Y/N): ")
                            print("\n")

                            if bb=="Y":
                                mycursor.execute("delete from sell_rec")
                                mydb.commit()

                                print("""
+-----------------------+
|   RESET SUCCESSFULL   |
+-----------------------+\n""")
                            
                            else:
                                pass
    #AVAILABLE BOOKS
                    elif a==6:
                        mycursor.execute("select * from available_books order by bookname")
                        for v in mycursor:
                            print("\n",v)

    #TOTAL INCOME AFTER LATEST UPDATE
                    elif a==7:
                        mycursor.execute("select sum(price) from sell_rec")
                        for x in mycursor:
                            print("\n",x,"\n")
    #EXIT                    
                    elif a==8:
                        leave = True
                        print("""
+-----------+
|   ADIEU   |
+-----------+""")
                        break

#LOGIN ELSE PART
            else:
                print("""
+------------------------+
|   INCORRECT PASSWORD   |
+------------------------+""")


        else:
            print("""
+------------------------+
|   INVALID USERNAME     |
+------------------------+""")

    else:
        break

    # if leave == True:
    #     break