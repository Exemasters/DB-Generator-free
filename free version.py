import random
import time
import colorama
import os 
import sys
from colorama import Fore 
from colorama import init 

os.system('title made by exemaster')
time.sleep(1)

file = open ("DB.txt", "w", encoding="utf-8")

print(Fore.YELLOW)

print('''


    //    ) ) //   ) ) 
   //    / / //___/ /  
  //    / / / __  (    
 //    / / //    ) )   
//____/ / //____/ /    
                                                        
                                                        
    //   ) )                                            
   //         ___       __      ___      __      ___    
  //  ____  //___) ) //   ) ) //___) ) //  ) ) //   ) ) 
 //    / / //       //   / / //       //      //   / /  
((____/ / ((____   //   / / ((____   //      ((___( (   
                         
                         
                         
 __  ___  ___      __    
  / /   //   ) ) //  ) ) 
 / /   //   / / //       
/ /   ((___/ / //        

'''

)

print('press Enter')
input()

print(Fore.GREEN)
print('загрузка')
print('-')
time.sleep(1)
os.system('CLS')
print('----')
time.sleep(1)
os.system('CLS')
print('--------')
time.sleep(1)
os.system('CLS')
print('------------')
time.sleep(1)
os.system('CLS')
print('------------------')
time.sleep(1)
os.system('CLS')
print('---------------------')
time.sleep(1)
os.system('CLS')
print('--------------------------')
time.sleep(1)
os.system('CLS')
print('готово!')
time.sleep(1)
os.system('CLS')

print(Fore.BLUE)


pet = input('pet:')
year = input('year:')
name = input('name:')
country = input('country:')
sport = input('sport:')
friend = input('friend:')
phone_num  = input('prhone num:')

lis = [pet ,year ,name ,country ,sport ,friend ,phone_num ]
ammount = int(input('ammount:'))
lenght = int(input('lenght:'))
print(lis)

for x in range( ammount ):
	password = ''

	for i in range( lenght ):
		password += random.choice(lis)

	print(password)

	file.write(  password + '\n')
print(Fore.RED)
print('Job well done! Press enter!')

input()



