import pandas as pd
import random
import itertools
import numpy as np
import mysql.connector
from random import randint
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(host="localhost", user ="root",passwd ="12345678", database ="appdata")
mycursor=mydb.cursor()

#For conversion in 1D array
def oneDArray(x):                                                          
    return list(itertools.chain(*x))

def login():
    print("Hello! \n >Enter 1 to Sign Up \n >Enter 2 to Sign In")
    log=int(input("Enter your choice : "))
    if log==1:
        no=int(input("Enter your Phone Number : "))
        p=int(input("Enter your Password : "))
        pw=pd.read_sql("select password from login where Phone_number='%s';"%(no),mydb)
        ps=pw.iloc[0]["Password"]
        
def StudentData():
    l=[]
    print("Questions marked with * are optional to fill")
    name=input("Enter Your Name: ")
    l.append(name)
    curclass=int(input("Enter class in integer form(eg 10,12): "))
    l.append(curclass)
    gender=int(input("""Enter Your Gender*
    1 for Male, 2 for Female, 3 for Other => """))
    if gender==1:
        gender="Male"
    elif gender==2:
        gender="Female"
    elif gender==3:
        gender="Other"
    l.append(gender)
    phone_number=int(input("Enter your phone number *: "))
    l.append(phone_number)
    address=input("Enter your address*: ")
    l.append(address)
    dob=input("Enter your Date of Birth (IN YYYY-MM-DD FORMAT)*: ")
    l.append(dob)
    stu=(l)
    sql="insert into students(name,curclass,gender,phone_number,address,dob)values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,stu)
    mydb.commit()
def teacherdata():
    k=[]
    print("Questions marked with * are optional to fill")
    name=input("Enter name: ")
    k.append(name)
    degree=input("Enter degree: ")
    k.append(degree)
    subject=input("Enter Subject: ")
    k.append(subject)
    gender=int(input("""Enter Your Gender*
    1 for Male, 2 for Female, 3 for Other =>"""))
    if gender==1:
        gender="Male"
    elif gender==2:
        gender="Female"
    elif gender==3:
        gender="Other"
    k.append(gender)
    phone_number=int(input("Enter your phone number : "))
    k.append(phone_number)
    CBSE_number=input("Enter your teaching ID*: ")
    k.append(CBSE_number)
    address=input("Enter your address*: ")
    k.append(address)
    dob=input("Enter your Date of Birth (IN YYYY-MM-DD FORMAT): ")
    k.append(dob)
    teacher=(k)
    sql="insert into teachers(name,degree,subject,gender,phone_number,CBSE_number,address,dob)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,teacher)
    mydb.commit()

def Updatedata():
    x=int(input("Enter what to update : \n 1)For student =>1  \n 2) For teacher =>2 \n For going Back to Menu =>9 \n "))
    if x==1:
        n=input("Enter the Phone number of student ")
        print("1. Name")
        print("2. Current Class")
        print("3. Gender")
        print("4. Address")
        print("5. DOB")
        y=int(input("Enter the detail no. to update "))
        if y==1:
            s=input("Enter Name : ")
            sql="update students set name='%s' where phone_number='%s';"%(s,n)
            mycursor.execute(sql)
            mydb.commit()
            print("\nDetail Updated")
        elif y==2:
            s=input("Enter Class : ")
            sql="update students set Curclass='%s' where phone_number='%s';"%(s,n)
            mycursor.execute(sql)
            mydb.commit()
            print("\nDetail Updated")
        elif y==3:
            s=input("Enter Gender : ")
            sql="update students set Gender='%s' where phone_number='%s';"%(s,n)
            mycursor.execute(sql)
            mydb.commit()
            print("\nDetail Updated")
        elif y==4:
            s=input("Enter Address : ")
            sql="update students set address='%s' where phone_number='%s';"%(s,n)
            mycursor.execute(sql)
            mydb.commit()
            print("\nDetail Updated")
        elif y==5:
            s=input("Enter DOB : ")
            sql="update students set DOB='%s' where phone_number='%s';"%(s,n)
            mycursor.execute(sql)
            mydb.commit()
            print("\nDetail Updated")
        else:
            print("\nPlease enter a valid number")
    elif x==2:
        n=input("Enter the Phone number of teacher ")
        print("1. Name")
        print("2. Degree")
        print("3. Subject")
        print("4. Gender")
        print("5. CBSE Number")
        print("6. Address")
        print("7. DOB")
        y=int(input("Enter the detail no. to update "))
        if y==1:
            s=input("Enter Name : ")
            sql="update teachers set name='%s' where phone_number='%s';"%(s,n)
            mycursor.execute(sql)
            mydb.commit()
            print("\nDetail Updated")
        elif y==2:
            s=input("Enter Degree : ")
            sql="update teachers set degree='%s' where phone_number='%s';"%(s,n)
            mycursor.execute(sql)
            mydb.commit()
            print("\nDetail Updated")
        elif y==3:
            s=input("Enter Subject : ")
            sql="update teachers set subject='%s' where phone_number='%s';"%(s,n)
            mycursor.execute(sql)
            mydb.commit()
            print("\nDetail Updated")
        elif y==4:
            s=input("Enter Gender : ")
            sql="update teachers set Gender='%s' where phone_number='%s';"%(s,n)
            mycursor.execute(sql)
            mydb.commit()
            print("\nDetail Updated")
        elif y==5:
            s=input("Enter CBSE Number : ")
            sql="update teachers set CBSE_Number='%s' where phone_number='%s';"%(s,n)
            mycursor.execute(sql)
            mydb.commit()
            print("\nDetail Updated")
        elif y==6:
            s=input("Enter Address : ")
            sql="update teachers set address='%s' where phone_number='%s';"%(s,n)
            mycursor.execute(sql)
            mydb.commit()
            print("\nDetail Updated")
        elif y==7:
            s=input("Enter DOB (YYYY-MM-DD): ")
            sql="update teachers set dob='%s' where phone_number='%s';"%(s,n)
            mycursor.execute(sql)
            mydb.commit()
            print("\nDetail Updated")
        else:
            print("\nPlease enter a valid number")
def deldata():
    x=int(input("Enter what to Delete : \n 1)For student =>1  \n 2) For teacher =>2 \n For going Back to Menu =>9 \n "))
    if x==1:
         d=int(input("Enter Phone number of student: "))
         qry="delete from students where Phone_number='%s';"%(d)
         mycursor.execute(qry)
         mydb.commit()
         print("\nDetails deleted ")
    elif x==2:
        d=int(input("Enter Phone number of teacher: "))
        qry="delete from teachers where Phone_number='%s';"%(d)
        mycursor.execute(qry)
        mydb.commit()
        print("\nDetails deleted ")
    else:
        print("\nPlease enter a valid number")

 # For pyplot
def plot(m,fin):
    n=5
    
    sub=("English","Maths","Physics","Chemistry","Optional")
    y_pos=np.arange(len(sub))
    ind=np.arange(n)
    width=0.3
    plt.figure(figsize=(10,5))
    plt.bar(ind,m,width,color='r',label='Your marks')
    plt.bar(ind+width,fin,width,color='b',label='Average marks')
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.xticks(ind + width / 2, sub)
    plt.title("Marks Comparision")
    plt.legend()
    plt.show()
    
def marks():
    print("Enter your marks for comparision (Out of 100)")
    m=[]
    eng=int(input("Enter English marks : "))
    m.append(eng)
    math=int(input("Enter Maths marks : "))
    m.append(math)
    phy=int(input("Enter Physics marks : "))
    m.append(phy)
    chem=int(input("Enter Chemistry marks : "))
    m.append(chem)
    opt=int(input("Enter Optional marks : "))
    m.append(opt)
    marks=(m)
    sql="insert into marks(english,maths,physics,chemistry,optional)values(%s,%s,%s,%s,%s);"
    mycursor.execute(sql,marks)
    mydb.commit()
    avg=pd.read_sql("select avg(english),avg(maths),avg(physics),avg(chemistry),avg(optional)from marks;",mydb)
    ab=avg.values.tolist()        #gives nested list
    #For converting to 1D list
    
    fin=oneDArray(ab)
    grph=plot(marks,fin)
    
    

    
    
    
    
         
    
        
        
        
    
    
