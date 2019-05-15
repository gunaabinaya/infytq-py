ef calculate(distance,no_of_passengers):
    x=distance*10
    p=x*70
    nop=no_of_passengers*80
    if(p>nop):
        return p-nop
    else:
        return -1
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
