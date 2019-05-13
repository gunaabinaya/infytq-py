bill_amount=0
    distance_rate=0 
    if((quantity_ordered>=1) and (distance_in_kms>0)):
        if(food_type=="N" or food_type=="V"):
        
            if(food_type=="N"):
                if((distance_in_kms>=1) and (distance_in_kms<=3)):
                    distance_rate=0
                if((distance_in_kms>=4) and (distance_in_kms<=6)):
                    distance_rate=(distance_in_kms-3)*3
                if(distance_in_kms>6):
                    distance_rate=(9+((distance_in_kms-6)*6))
                bill_amount=((150*quantity_ordered)+distance_rate)
            if(food_type=="V"):
                if((distance_in_kms>=1) and (distance_in_kms<=3)):
                    distance_rate=0
                if((distance_in_kms>3) and (distance_in_kms<=6)):
                    distance_rate=(distance_in_kms-3)*3
                if(distance_in_kms>6):
                    distance_rate=(9+((distance_in_kms-6)*6))
                bill_amount=((120*quantity_ordered)+distance_rate)
        else:
            bill_amount=-1
    else:
        bill_amount=-1
    return bill_amount
