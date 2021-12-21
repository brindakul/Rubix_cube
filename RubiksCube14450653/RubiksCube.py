import random
import sys
import time


# different moves
# https://ruwix.com/online-puzzle-simulators/2x2x2-pocket-cube-simulator.php

MOVES = {
    "U": [2,  0,  3,  1, 20, 21,  6,  7,  4,  5, 10, 11, 12, 13, 14, 15,  8,  9, 18, 19, 16, 17, 22, 23],
    "U'": [1,  3,  0,  2,  8,  9,  6,  7, 16, 17, 10, 11, 12, 13, 14, 15, 20, 21, 18, 19,  4,  5, 22, 23],
    "R": [0,  9,  2, 11,  6,  4,  7,  5,  8, 13, 10, 15, 12, 22, 14, 20, 16, 17, 18, 19,  3, 21,  1, 23],
    "R'": [0, 22,  2, 20,  5,  7,  4,  6,  8,  1, 10,  3, 12, 9, 14, 11, 16, 17, 18, 19, 15, 21, 13, 23],
    "F": [0,  1, 19, 17,  2,  5,  3,  7, 10,  8, 11,  9, 6,  4, 14, 15, 16, 12, 18, 13, 20, 21, 22, 23],
    "F'": [0,  1,  4,  6, 13,  5, 12,  7,  9, 11,  8, 10, 17, 19, 14, 15, 16,  3, 18,  2, 20, 21, 22, 23],
    "D": [0,  1,  2,  3,  4,  5, 10, 11,  8,  9, 18, 19, 14, 12, 15, 13, 16, 17, 22, 23, 20, 21,  6,  7],
    "D'": [0,  1,  2,  3,  4,  5, 22, 23,  8,  9,  6,  7, 13, 15, 12, 14, 16, 17, 10, 11, 20, 21, 18, 19],
    "L": [23,  1, 21,  3,  4,  5,  6,  7,  0,  9,  2, 11, 8, 13, 10, 15, 18, 16, 19, 17, 20, 14, 22, 12],
    "L'": [8,  1, 10,  3,  4,  5,  6,  7, 12,  9, 14, 11, 23, 13, 21, 15, 17, 19, 16, 18, 20,  2, 22,  0],
    "B": [5,  7,  2,  3,  4, 15,  6, 14,  8,  9, 10, 11, 12, 13, 16, 18,  1, 17,  0, 19, 22, 20, 23, 21],
    "B'": [18, 16,  2,  3,  4,  0,  6,  1,  8,  9, 10, 11, 12, 13,  7,  5, 14, 17, 15, 19, 21, 23, 20, 22],
} 
       
#u=__init__(self,"abc")

'''
sticker indices:

      0  1
      2  3
16 17  8  9   4  5  20 21
18 19  10 11  6  7  22 23
      12 13
      14 15

face colors:

    0
  4 2 1 5
    3

moves:
[ U , U', R , R', F , F', D , D', L , L', B , B']
'''
"WGGY OWRY WGBG RYBO ORRW OBBY"

class cube:

   def __init__(self, string="WWWW RRRR GGGG YYYY OOOO BBBB"):
       self.string=string.replace(" ","")
       self.dict={0:self.string[0],1:self.string[1],2:self.string[2],3:self.string[3],4:self.string[4],5:self.string[5],6:self.string[6],7:self.string[7],8:self.string[8],9:self.string[9],10:self.string[10],11:self.string[11],12:self.string[12],13:self.string[13],14:self.string[14],15:self.string[15],16:self.string[16],17:self.string[17],18:self.string[18],19:self.string[19],20:self.string[20],21:self.string[21],22:self.string[22],23:self.string[23]}
       return
   
   def norm(self):
       self.print()
       self.one=self.string[10]
       self.two=self.string[12]
       self.three=self.string[19]
       print(self.string[10],self.string[12],self.string[19])
       if self.one!="G" or self.two!="Y"or self.three!="O":
           old_str=self.string
           str_list=list(old_str)
           #str_list[i]=self.c
           
           for k in range(0,24):
               self.p=self.string[k]
               if self.string[k]=="G":
                   self.p=self.one
                   self.one1="G"
                   self.one=self.one1
                   str_list[k]=self.one
               if self.string[k]=="Y":
                   self.p1=self.two
                   self.one2="Y"
                   self.two=self.one2
                   str_list[k]=self.two
               if self.string[k]=="O":
                   self.p3=self.three
                   self.one3="G"
                   self.three=self.one3
                   str_list[k]=self.three
               new_string = "".join(str_list)
               self.string=new_string
           self.print()    
           '''self.temp=self.one
           self.one="G"
           
           self.string=self.string.replace(self.string[10],"G")
           self.print()'''
       '''if self.two!="Y":
           self.temp1=self.two
           self.one="Y"
           print(self.string.replace(self.temp1,"Y"))
           #self.string=self.string.replace(self.two,"Y")
           #self.print()
       if self.three!="O":
           self.temp2=self.three
           self.one="O"
           print(self.string.replace(self.temp2,"O"))
           #self.string=self.string.replace(self.three,"O")
           #self.print()
       #self.print()'''
           
       
       
       return

   def equals(self, cube):
       cube=cube.replace(" ","")
       print(cube==self.string)
       
    # your code
       return

   def clone(self):
    # your code
    return

    # apply a move to a state
   def applyMove(self, move):
       self.a=MOVES[move]
       self.len1=len(self.a)
       for i in range(0,self.len1):
           self.b=self.a[i]
           self.c=self.dict[self.b]
           old_str=self.string
           str_list=list(old_str)
           str_list[i]=self.c
           new_string = "".join(str_list)
           self.string=new_string
           
       for i1 in range(0,self.len1):
           self.dict[i1]=self.string[i1]
         
       return self.string

    # apply a string sequence of moves to a state
   def applyMovesStr(self, alg):
       alg1=alg.split()
       self.len2=len(alg1)
       for i in range(0,self.len2):
           self.move1=alg1[i]
           self.applyMove(self.move1)
       self.print()
       return self.string

    # check if state is solved
   def isSolved(self):
       self.i1=0
       self.flag=0
       self.flag1=0
       while self.i1<24:   
           self.sub=self.string[self.i1:self.i1+4]
           old_str=self.sub
           str_list=list(old_str)
           self.i3=0
           if str_list[self.i3]==str_list[self.i3+1]:
               if str_list[self.i3+1]==str_list[self.i3+2]:
                   if str_list[self.i3+2]==str_list[self.i3+3]:
                       self.flag=self.flag+1
           if self.flag == 1:
               self.flag1=self.flag1+1
           self.flag=0  
           self.i1=self.i1+4
       if self.flag1==6:
           self.ans="true"
       else:
           self.ans="false"
       return self.ans

    # print state of the cube
   def print(self):
       print("   ",self.string[0],self.string[1])
       print("   ",self.string[2],self.string[3])
       print(self.string[16],self.string[17],self.string[8],self.string[9],self.string[4],self.string[5],self.string[20],self.string[21])
       print(self.string[18],self.string[19],self.string[10],self.string[11],self.string[6],self.string[7],self.string[22],self.string[23])
       print("   ",self.string[12],self.string[13])
       print("   ",self.string[14],self.string[15])
       return
   
   def shuffle(self, n):
       self.string3=""
       for i2 in range(0,n):
           self.list1=random.choices(list(MOVES.keys()))
           self.string3=self.string3 + self.listToString(self.list1)+" "
           print(self.list1)
       print(self.string3)
       self.applyMovesStr(self.string3)
       return
   
   def random1(self,str2,n):
       self.string20=self.applyMovesStr(str2)  
       start_time = time.time()
       num=0
       while n>0:
           self.string3=""
           self.string=self.string20
           for i2 in range(0,n):
               self.list1=random.choices(list(MOVES.keys()))
               self.string3=self.listToString(self.list1)
               self.applyMove(self.string3)
               num=num+1
               if self.isSolved()=="true":
                   self.print()
                   print("The sequence responsiblefor goal state",self.string3)
                   print("number of cycles ",num) 
                   print("Time taken to reach the goal state ",time.time() - start_time)
                   return 
       return
   
   
   def listToString(self,s): 
       str1 = "" 
       for ele in s: 
        str1 += ele  
    
    # return string  
       return str1 
num = sys.argv[1:]
length=len(num)
a1=cube()

if num[0] == "print":
    if length > 1:
        num[1]=num[1].replace(" ","")
        a1.string=num[1]
        a1.print() 
    else:
        a1.print()
    
elif num[0] == "shuffle":
    number=int(num[1])
    a1.shuffle(number)

elif num[0] == "goal":
    input_str=num[1]
    print(input_str)
    a1.equals(input_str)

elif num[0] == "applyMovesStr":
    input_str1=num[1]
    a1.string=num[2]
    a1.applyMovesStr(input_str1)

else :
    ip1=num[1]
    ip2=int(num[2])    
    a1.random1(ip1,ip2)
               
 