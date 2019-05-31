#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)
x=len(list_of_marks)
avg=sum(list_of_marks)/x
c=0
def find_more_than_average():
    c=0
    for i in list_of_marks:
        if i>avg:
            c=c+1
    y=(c/x)*100
    return y
    
    #Remove pass and write your logic here

def sort_marks():
    k=list_of_marks.sort()
    return k#Remove pass and write your logic here

def generate_frequency():
    for i in range(0,26):
        P=[]
        l=0
        for j in range(0,len(list_of_marks)):
            if(list_of_marks[j]==i):
                l+=1 
        P.append(l)
    return(P)

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
