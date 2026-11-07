import csv
import os

def CREATE_ACCOUNT():
    F=open("bank.csv","w",newline='')
    w=csv.writer(F)
    N=int(input("Enter the number of customers:"))
    for i in range(0,N,1):
        account_no=int(input("Enter the Account Number:"))
        name=input("Enter the Account Holder name:")
        account_type=input("Enter the Account Type:")
        Bal=int(input("Enter the initial balance in Rs/-:"))
        Age=int(input("Enter the age of the account holder:"))
        mobno=int(input("Enter the mobile number:"))
        Rec=[account_no,name,account_type,Bal,Age,mobno]
        w.writerow(Rec)
    print("ACCOUNT SUCCESSFULLY CREATED")
    F.close
    
def SHOW_ACCOUNT():
    f=open("bank.csv","r",newline='')
    R=csv.reader(f)
    for i in R:
        print(i)
    f.close()

def ADD_ACCOUNT():
    F=open("bank.csv","a",newline='')
    w=csv.writer(F)
    R=int(input("Enter the Account number:"))
    Nam=input("Enter the Account holder name:")
    actype=input("Enter the account type:")
    bal=int(input("Enter the initial balance Rs/- :"))
    age=int(input("Enter the age of the account holder:"))
    mobileno=int(input("Enter the mobile number:"))
    Rec=[R,Nam,actype,bal,age,mobileno]
    w.writerow(Rec)
    print("ACCOUNT ADDED SUCCESSFULLY")
    F.close()


def BALANCE(P):
    flag=0
    f=open("bank.csv","r",newline='')
    R=csv.reader(f)
    for i in R:
        if int(i[0])==P:
            flag=1
            print("The account balance is:")
            print(i[3])
        if flag==0:
            print("ACCOUNT NOT FOUND")
    f.close()

def MODIFY_ACCOUNT_TYPE_AGE_MOBILENUMBER(NT):
    flag=0
    fr=open("bank.csv","r",newline='')
    R=csv.reader(fr)
    fw=open("temp_bank.csv","w",newline='')
    W=csv.writer(fw)
    for i in R:
        if int(i[0])==NT:
            flag=1
            print("The account in the file going to be modify is:")
            print(i)
            print("Please Enter the new account type of the account")
            i[2]=input("Enter the new account type:")
            i[3]=int(input("Enter the new age:"))
            i[4]=int(input("Enter the new mobile number:"))
            print("ACCOUNT MODIFIED SUCCESSFULLY.......")
            W.writerow(i)
        else:
            W.writerow(i)
    if flag==0:
        print("ACOOUNT NOT MATCHED")
    fr.close()
    fw.close()
    os.remove("bank.csv")
    os.rename("temp_bank.csv","bank.csv")


def DEPOSIT_AMOUNT(account_number, amount):
    accounts = []  
    with open("bank.csv", "r", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            accounts.append(row)

    found = False
    for account in accounts:
        if account[0] == str(account_number):
            found = True
            balance = float(account[3])
            balance += amount  
            account[3] = str(balance)
            print("Deposit successful. Current balance is:", balance)
            break

    if not found:
        print("ACCOUNT NOT FOUND......")


    with open("bank.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(accounts)


def WITHDRAW_AMOUNT(account_number, amount):
    accounts = []  
    with open("bank.csv", "r", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            accounts.append(row)

    found = False
    for account in accounts:
        if account[0] == str(account_number):
            found = True
            balance = float(account[3])
            if amount <= balance:
                balance -= amount
                account[3] = str(balance) 
                print("Withdrawal successful!!!!. Current balance is:", balance)
            else:
                print("Insufficient balance for withdrawal.")
            break

    if not found:
        print("ACCOUNT NOT FOUND.......")

    
    with open("bank.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(accounts)


def SEARCH_ACCOUNT(M):
    flag=0
    f=open("bank.csv","r",newline='')
    R=csv.reader(f)
    for i in R:
        if int(i[0])==M:
            flag=1
            print("The account details to be searched by the account number is:")
            print(i)
    if flag==0:
        print("ACCOUNT NOT FOUND......")
    f.close()

def CLOSE_ACCOUNT(C):
    flag=0
    fr=open("bank.csv","r",newline='')
    R=csv.reader(fr)
    fw=open("temp_bank.csv","w",newline='')
    W=csv.writer(fw)
    for i in R:
        if int(i[0])==C:
            flag=1
            print("The account in the file going to be modify is:")
            print(i)
            
        else:
            W.writerow(i)
    if flag==0:
        print("ACOOUNT NOT FOUND......")
    fr.close()
    fw.close()
    os.remove("bank.csv")
    os.rename("temp_bank.csv","bank.csv")
    
print("===========================================================================================================")
print("-----------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\tBANK MANAGEMENT SYSTEM")
print("-----------------------------------------------------------------------------------------------------------")
print("===========================================================================================================")

input("PRESS ENTER TO CONTINUE")

while True:
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. ADD AN ACCOUNT")
    print("\t7. CLOSE AN ACCOUNT")
    print("\t8. MODIFY AN ACCOUNT-(TYPE AND ACCOUNT HOLDER AGE)")
    print("\t9. SEARCH ACCOUNT")
    print("\t10. EXIT")
    ch=int(input("Enter the choice(1-10):"))

    if ch==1:
        CREATE_ACCOUNT()
    elif ch==2:
        NJ=int(input("Enter the account number to deposit amount:"))            
        Balance=float(input("Enter the deposit amount:"))
        DEPOSIT_AMOUNT(NJ,Balance)


    elif ch==3:
        account_no=int(input("Enter the account number to withdraw the balance:"))
        Balance=float(input("Enter the amount to be withdrawl:"))
        WITHDRAW_AMOUNT(account_no,Balance)

    elif ch==4:
        H=int(input("Enter the account number whose balance need to be displayed:")) 
        BALANCE(H)

    elif ch==5:
        SHOW_ACCOUNT()

    elif ch==6:
        ADD_ACCOUNT()

    elif ch==7:
        G=int(input("Enter the account number which need to be closed:"))
        CLOSE_ACCOUNT(G)

    elif ch==8:
       S=int(input("Enter the account number to be modified by type,age and mobile number:"))
       MODIFY_ACCOUNT_TYPE_AGE_MOBILENUMBER(S) 

    elif ch==9:
        J=int(input("Enter the account number to search account:"))            
        SEARCH_ACCOUNT(J)

    elif ch==10:
        break
        print("\n.THANK YOU....")




