#Write a script to create a list with 5 string and count total number of string with even number of length with string using UDF
#Eg: ["OM","SAI","RAMA"}
#Total string of even number of character : 2
#OM
#RAMA


#Two Lists Are Defined Here

A = ['Om','sai','rama','krishna','radhe']
B = []

#Functions are Defined Here

def countSt(list):
    v = len(list)
    print("Length of String is : {}".format(v))

def checkAdd(list):
    for i in list:
        chk=0
        for j in i:
            c = len(i)
            if((c%2)==0):
                chk=1
            else:
                pass
        if(chk==1):
            B.append(i)
    print("Total Strings With Even Number's Length = {}".format(len(B)))
    print(B)


#Execution Starts From Here
    
countSt(A)
checkAdd(A)
