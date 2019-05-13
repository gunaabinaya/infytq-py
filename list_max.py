def find_max(num1, num2):
    l=[]
    s=0
    max_num=-1
    if(num1<num2):
        for n in range(num1,num2+1):
            temp=n
            while(temp>0):
                r=temp%10
                s=s+r
                temp=temp//2
            if(s%3==0 and n%5==0 and n>=10 and n<=99):
                l.append(n)
            else:
                max_num=-1
            if(l!=[]):
                max_num=max(l)
    
    # Write your logic here
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(3,30)
print(max_num)
