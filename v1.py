import os
import random
os.system("clear")

def ScrambleEverything():
    print("Hello World")





answer=[]
print("Welcome to word scrambler\n")
print("1. Read from standard input")
print("2. Read from file")
print("   \nEnter your choice :")
flag=0

if(int(input()) == 2):

    print("Opening file...")
    flag=1
    f = open("data", "r")
    f.seek(0)
    f.read()
    #output_file = open("output_data.txt", "w")

else :

    main = input("\nPlease enter your input : ").strip()


if (flag == 0):
    if(len(main) < 3):
        print("No need to scramble")
        print("Bye")

    else :
        list = main.split(" ")
        #print(list)

        for i in range(len(list)):
            temp= list[i]
            #print(temp)
            #print(len(temp))
            randlist=random.sample(range(1,len(temp)-1),len(temp)-2)
            #print(randlist)
            number=0
            list_new=[]

            for j in range(1,len(temp)-1):
                #print(temp[j])
                temp1=j
                j=randlist[number]
                number+=1
                list_new.append(temp[j])
                j=temp1     

            #print(list[i][0])
            #print(list[i][len(temp)-1])
            list_new.insert(0,list[i][0])
            list_new.insert(len(list_new)+1,list[i][len(temp)-1])
            abc = str(''.join(list_new))
            answer.append(abc)
        #print(abc)
        print(answer)       






if (flag == 1) :
    print("Here are the contents :")
    print(f.read())

    

