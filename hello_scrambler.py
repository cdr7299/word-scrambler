import os
import random
os.system("clear")

def ScrambleEverything(our_list):
	answer=[]
	main = our_list
	#print("Hello World")
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
			if (temp[(len(temp)-1)] == "," or "!" or "?" or "."):
				randlist=random.sample(range(1,len(temp)-2),len(temp)-3)
				flag_punc=1
			else:	
				randlist=random.sample(range(1,len(temp)-1),len(temp)-2)
			#print(randlist)
			number=0
			list_new=[]

			if (temp[(len(temp)-1)] == "," or "!" or "?" or "."):
				
				#maslkmclsamc
				for j in range(1,len(temp)-2):
					#print(temp[j])
					temp1=j
					j=randlist[number]
					number+=1
					list_new.append(temp[j])
					j=temp1    	

				

			else :				
					for j in range(1,len(temp)-1):
						#print(temp[j])
						temp1=j
						j=randlist[number]
						number+=1
						list_new.append(temp[j])
						j=temp1    	

			#print(list[i][0])
			#print(list[i][len(temp)-1])
			if (flag_punc == 1):
				list_new.insert(0,list[i][0])
				list_new.insert(len(list_new)+1,list[i][len(temp)-2])
				list_new.insert(len(list_new)+2,list[i][len(temp)-1])
				flag_punc = 0

			
			else :

				list_new.insert(0,list[i][0])
				list_new.insert(len(list_new)+1,list[i][len(temp)-1])
			
			abc = str(''.join(list_new))
			answer.append(abc)
		#print(abc)

		answer = str(' '.join(answer))
		#print(answer)
		return answer



print("Welcome to word scrambler\n")
print("1. Read from standard input")
print("2. Read from file")
print("   \nEnter your choice :")
flag=0

if(int(input()) == 2):
	print("Opening file...")
	print("File Contents : \n")
	flag=1
	f = open("data.txt", "r")
	f.seek(0)
	data = f.read().strip()
	print(data + "\n")
	temp=ScrambleEverything(data)
	print("Shuffled Words : \n")
	print(temp)
	print("Check the new file!")
	temp=temp.split()
	output_file = open("output_file.txt", "w")
	for item in temp:
		output_file.write("%s " % item)


else :

	main = input("\nPlease enter your input : ").strip()
	print(main)
	ans=ScrambleEverything(main)
	print("\nShuffled Words : \n")
	print(ans)
