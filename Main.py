import random

pass_length=int(input("Enter the Length Of Password: ")) #length of password from user

#creating lists of chars
num_list=['1','2','3','4','5','6','7','8','9','0']

alpha_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
alpa_upper_list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

#combining all the list
all_set=num_list+alpha_list+alpa_upper_list+symbols
password=""

#inserting random chars in password
for i in range(0,pass_length):
    random_char=random.randint(0,len(all_set)-1)
    password=password+str(all_set[random_char]) #getting char from random index of list
    
print("Password: "+password)
    
    
 

