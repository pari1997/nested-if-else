atmcard=input("enter atmcard")
if atmcard=='right side' or atmcard=='Right side':
    language=input("enter any language")
    if language=='english' or language=='hindi':
        pin=int(input("enter four digit number"))
        if pin>=1000 and pin<=9999:
            transection_type=input("enter transection type")
            if transection_type=='withdraw' or transection_type=='Withdraw':
                account_type=input("enter account type")
                if account_type=='savings' or account_type=='current':
                    press_key=input("enter ok")
                    if press_key=='ok' or press_key=='OK':
                        amount=input("enter amount")
                        if amount>=500 or amount<=2000 and amount%500==0:
                            a=amount//2000
                            b=amount%2000
                            c=a//500
                            d=a%500
                            print("notes of 2000=",a,"notes of 500=",c,)
                            pressing=input("enter pressing")
                            if pressing=='cencel' or pressing=='cross':
                                print("your trasection is succesful")
                        else:
                            print("amount is not avalable")
                    else:
                        print("you press not ok")
                else:
                    print("eror")
            elif transection_type=='balance enquiry' or transection_type=='Balance enquiry':
                account_type=input("enter account type")
                if account_type=='saving' or account_type=='current':
                    account_no=int(input("enter account no"))
                    if account_no>=1000000000000 and account_no<=999999999999:
                        key_name=input("enter ok")
                        if key_name=='ok' or key_name=='OK':
                            print("your ballance checcking succesfull")
                        else:
                            print("your press key not ok")
                    else:
                        print("account no not currect")
                else:
                    print("error")
            elif transection_type=='diposite money' or transection_type=='Diposite money':
                account_type=input("enter account type")
                if account_type=='saving' or account_type=='current':
                    account_no=int(input("enter account number"))
                    if account_no>=100000000000 and account_no<=999999999999:
                        bill_amount=int(input("enter bill"))
                        if bill_amount<=1 and bill_amount>=99999999999999:
                            amount=int(input("enter amount"))
                            key_name=int(input("enter ok"))
                            if key_name=='ok' or key_name=='OK':
                                print("succesfull")
                            else:
                                print("invalid key")
                        else:
                            print("money not availavle")
                    else:
                        print("account no not currect")
                else:
                    print("error")
            elif transection_type=='bill_payment' or transection_type=='Bill payment':
                account_type=input("enter account type")
                if account_type=='saving' or account_type=='current':
                    account_no=int(input("enter account no"))
                    if account_no>=10000000000 and account_no<=999999999999:
                        money=int(input("enter money"))
                        if money>=1 and money<=999999999999999999:
                            press_key=input("enter ok")
                            if press_key=='ok' or press_key=='OK':
                                print("bill payment succesfull")
                        else:
                            print("press key invalid")
                    else:
                        print("account no wrong")
                else:
                    print("error")
            else:
                print("account type not currect")
        else:
            print("pin is not currect")
    else:
        print("invalid languge")
else:
    print("wrong side")


