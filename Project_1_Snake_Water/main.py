'''
1 for snake
-1 for water
0 for gun
'''

myDict = {
          "s" : 1,
          "w" : -1,
          "g" : 0
        }

player1 = input("Player 1 Enter your Input: ").lower()
player2 = input("Player 2 Enter your Input: ").lower()

print(f"Player 1 choose: {player1}")
print(f"Player 2 choose: {player2}")


p1 = myDict[player1]
p2 = myDict[player2]



if(p1 == p2):
    print("It's a draw!")

else:
    if(p1 == 1 and p2 == -1):
        print("Player 1 Wins!")

    elif(p1 == 1 and p2 == 0):
        print("Player 2 Wins!")

    elif(p1 == -1 and p2 == 1):
        print("Player 2 Wins!")

    elif(p1 == 0 and p2 == 1):
        print("Player 1 Wins!")

    elif(p1 == 0 and p2 == -1):
        print("Player 2 Wins!")

    elif(p1 == -1 and p2 == 0):
        print("Player 1 Wins!")