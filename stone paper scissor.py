from getpass import getpass as input
#-------------------------------------#
print("rock paper scissors")
print("moves are limited to R P and S")
#-------------------------------------#
move_list = ['R','P','S']
#-------------------------------------#
counter_1 = 0
counter_3 = 0
player1 = ''
player2 = ''
#-------------------------------------#
while counter_3 != 3:
  player1 = input("choose your move player 1 ")
  player2 = input("choose your move player 2 ")
  if player1 == player2 and counter_3 == 0:
    print("looks like you both picked ", player1,"wich are the same thing so it dosent count")
  elif player1 == 'R' and player2 ==  'S':
    print("player 1 wins this round")
    counter_1 +=1
    counter_3 +=1
  elif player1 == 'P' and player2 == 'R':
    print("player1 wins this round")
    counter_1 +=1
    counter_3 +=1
  elif player1 == 'S' and player2 == 'P':
    print("player1 wins this round")
    counter_1 +=1
    counter_3 +=1
  else:
    print("player 2 wins this round")
    counter_3 +=1
#-------------------------------------#
if counter_1 == 2 or counter_1 == 3:
  print("player 1 wins the game")
else:
  print("player 2 wins the game")
      
      