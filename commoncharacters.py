def find_common_characters(msg1,msg2):
    a=msg1.replace(" ", "")
    b=msg2.replace(" ", "")
    s=''
    for i in a:
        if i in b:
            s=s+i
    if s=='':
        return -1
    else:
        return s

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
