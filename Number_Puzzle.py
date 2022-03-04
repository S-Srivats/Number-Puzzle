import os
import sys
import time
import random
import keyboard

#Checks whether the puzzle created is solvable
def solvable(temp,ideal):
   i=0
   n=m*m-1
   swap=0
   while i<=n-1: 
         if (temp[i]!=ideal[i]):
            ind=temp[i]-1
            temp[i],temp[ind] = temp[ind],temp[i]
            swap+=1
         else:
            i+=1
            
   return swap%2==0
   
#Create a solvable mxm puzzle
def create_mat(m):

   l=[i for i in range(1,m*m)]
   #r=[[random.randrange(1,100) for i in range(3)]for j in range(3)]
   r=[[0 for i in range(m) ] for j in range(m)]

   ideal=l[::]
   temp=[]

   for i in range(m): 
       for j in range(m):

            if(i==j==m-1):
                r[i][j]="  "
                temp.append(r[i][j])

            else:             
                r[i][j]=random.choice(l)                
                temp.append(r[i][j])
                l.remove(r[i][j])          

   #If puzzle is not solvable, exchange elements in first two indices to make it solvable
   if not(solvable(temp,ideal)):
      r[0][0],r[0][1]=r[0][1],r[0][0]

   return r  

#Checks whether the new position to which the user wants to move is a valid location
def pos_verify():

   x=(pos%m==0 and new_pos==pos+1) or (new_pos==pos-1 and new_pos%m==0)
   z=new_pos in [i for i in range(1,m*m+1)]
   return (not(x) and z)

#Print the complete puzzle for every new change  
def print_mat(m):
   
    print('\n',' '*5,'_'*(m*7))

    for i in range(m):
        print()
        for j in range(m):
           print('\t',r[i][j],' ',end='')

        print('\n',' '*5,'_'*(m*7))
        
#Modify the puzzle to the moving the selected number to vacant space 
def modify(n):
    global pos,m
    
    for i in range(m):
       for j in range(m):

           if ideal_mat[i][j]==n:
              x,y=i,j

           if ideal_mat[i][j]==pos:
              p,q=i,j

    r[x][y],r[p][q]=r[p][q],r[x][y]
    pos=ideal_mat[x][y]

#Find the new position corresponding to the key pressed, considering the current location of empty space     
def find_newpos():
    global pos
    return pos+a

#Check whether the puzzle is solved
def check():
     tmp=[]
     chk=1

     for i in range(m):
        for j in range(m):
              tmp.append(r[i][j])

     if tmp[m*m-1]=='  ':
        for i in range(0,m*m-2):
            if(tmp[i]>tmp[i+1]):
                chk=0
        else:

             if chk==1:
                return 1
             else:
                return 0

#Keep doing continuously until the user quits the game
while(True):
    os.system('cls')
    print('''\t\b\b\nPuZzLe GaMe \n\nObjective:

    $ Slide the numbers around until they are in numerical order from least to greatest, left to right and top to bottom.
    $ The white space is the open space that the numbered squares are moved to.
    $ To move a number present above and below the open space, press down arrow and up arrow, respectively.
    $ Similarly, to move a number that is present to the left and to the right of the open space, press right arrow and left arrow, respectively.
    $ Only numbers that are immediately to the left, right, above or below the empty space can be moved.
    $ The open space should end up in the lower right hand corner when the puzzle has been solved.

    Enjoy!


    ''')

    
    #r=[[random.randrange(1,100) for i in range(3)]for j in range(3)]
    r=[[1,2 ,3],[4,5,6],[7,8," "]]

    print_mat(3)
    input("\n\nHit 'enter' key to begin\n")
    os.system('cls')

    m=2+int(input('''\nSelect the dimensions of the puzzle\n1) 3x3\n2) 4x4\n3) 5x5\n4) 6x6\n5) 7x7\n6) 8x8 \n\n Enter Your Choice: '''))
    pos=m*m

    values=[i for i in range(1,m*m+1)]
    ideal_mat=[values[i-m:i:] for i in range(m,m*m+1,m)]
    
    check_dict={'up':m, 'right':-1, 'left':+1,'down':-m}
    checklist=['up', 'right', 'left', 'down']
    r=create_mat(m)

    print("\n"*10)
    print_mat(m)
    print("")

    while(1):
            #read keypress
            a=keyboard.read_key()
            a=keyboard.read_key()
            #print(a)

            #check whether it is a valid key(up, left, down or right)
            if (a in checklist ):
                      a=check_dict[a]
                      new_pos = find_newpos()
                      
            #check whether it is a valid move.
            #If yes, then make the move
            if(pos_verify()):
                modify(new_pos)
                pos=new_pos
            else:
                 continue

            #clear the screen and print the modified puzzle
            os.system('cls')
            print("\n"*10)
            print_mat(m)

            #check whether the puzzle has been solved.
            #If yes, then break from the loop
            if check()==1:
              break

    #congratulate the player and ask whether he wants to play again
    print("\n You Win!!")
    print("\n\n Want to play again? (y/n) ")

    #read player's choice
    a=keyboard.read_key()
    print('\b')

    #if he wants to play again, then continue with the main loop
    #otherwise, don't force him...just say good bye and quit 
    if a=='n' or a=='N':
        print("\n Okay.. We'll see next time.\n Bye Bye!! ")
        time.sleep(2.5)
        break
