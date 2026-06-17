import random

def game():
    print("You are playing the game..")
    score = random.randint(1 , 100)

    with open("hi_score.txt") as f:
        hiScore = f.read()
        if(hiScore != ""):
            hiScore = int(hiScore)
        else:
            hiScore = 0

        print(f"Your score is {score}")
        if(score > hiScore):
            with open("hi_score.txt", "w") as f:
                f.write(str(score))
        
        return score
    
game()