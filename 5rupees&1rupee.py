def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    x=rupees_to_make%5
    y=int(rupees_to_make/5)
    no_of_one=x
    no_of_five=y
    l=(y*5)+x
    if(l==rupees_to_make):
        print("No. of Five needed :", y)
        print("No. of One needed  :", x)
    else:
        print(-1)
