import pymysql as SQL
try:
    conn=SQL.connect(host='localhost',port=3306,user='root',passwd='1234',database='bank',cursorclass=SQL.cursors.DictCursor)
    smt=conn.cursor()
    an=0

    '''

    While running the code for the first time set this 'an' (line 5) to whatever integer value
    that you want your account number to start from. after running once you MUST remove it or 
    set it to ZERO, then it will not show any error
    
    '''


    while(True):
        print("*"*148)
        print("*"*148)
        print("\t\t\t\tBANK MANAGEMENT SYSTEM")
        c=int(input("\n\n1] Open Account \n2] Withdraw Cash \n3] Cash Deposit \n4] Show bank statement \n5] Exit \n\nEnter your choice: "))
        if c==1:
            name=input("Enter name of account holder: ")
            bal=int(input("Enter Opening balance: "))
            mob=int(input("Enter registered mobile number: "))
            q="insert into banker () values({0},'{1}',{2},'{3}')".format(an,name,bal,mob)
            an=an+1
            smt.execute(q)
            conn.commit() 
            print("Account opened succesfully ")


        if c==2:
            acn=int(input("Enter the account number from ehich you want to withdraw: "))
            amt=int(input("Enter the amount you want to Withdraw: "))
            q='select * from banker where acountnum = {}'.format(acn)
            smt.execute(q)
            rec=smt.fetchone()
            if(rec):
                rec['balance']=rec['balance']-amt
                balance=rec['balance']
                q='update banker set balance ={0} where acountnum={1}'.format(balance,acn)
                smt.execute(q)
                conn.commit()
                print("Cash withdrawn ",amt)


        if c==3:
            acno=int(input("Enter the account number from ehich you want to Deposit: "))
            amnt=int(input("Enter the amount you want to Deposit: "))
            q='select * from banker where acountnum = {}'.format(acno)
            smt.execute(q)
            rec=smt.fetchone()
            if(rec):
                rec['balance']=rec['balance']+amnt
                balan=rec['balance']
                q='update banker set balance ={0} where acountnum={1}'.format(balan,acno)
                smt.execute(q)
                conn.commit()
                print("Cash withdrawn ",amnt)


        if c==4:
            an=int(input("Enter account number: "))
            q='select * from banker where acountnum = {}'.format(an)
            smt.execute(q)
            rec=smt.fetchone()
            if(rec):
                print("="*100)
                print("Account details are: \n",rec)
                print("="*65)
            else:
                print("No such account number exists ..... please try again")


        if c==5:
                break


except Exception as err:
    print("Error",err)