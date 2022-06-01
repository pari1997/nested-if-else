e_date=int(input("enter e_date"))
e_month=int(input("enter e_month"))
e_year=int(input("enter e_year"))
r_date=int(input("enter r_date"))
r_month=int(input("enter r_month"))
r_year=int(input("enter r_year"))
if e_month==r_month and e_year==r_year:
    if r_date<=e_date:
        print("no fine")
    elif r_date>e_date:
        n_o_d_late=e_date-r_date
        fine=n_o_d_late*15
        print("fine=",fine)
    else:
        print("eror")
elif e_date==r_date and e_year==r_year:
    if r_month>e_month:
        n_o_d_late=e_month-r_month
        fine=n_o_d_late*500
        print("fine=",fine)
    else:
        print("none")
elif e_date==r_date and e_month==r_month:
    if r_year>e_year:
        fixed_fine=10000
        print(fixed_fine)
    else:
        print("no fix")
else:
    print("date not match")