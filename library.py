age=int(input("enter age"))
gender=input("enter gender")
marital_status=input("enter marital status")
if gender=='f':
    print("he will work only in urban area")
if gender=='m':
    if age>=20 and age<=40:
        print("he may work anywhere")
    elif age>=40 and age<=60:
        print("he will work urban area")
    else:
        print("error")
else:
    print("gender not match")