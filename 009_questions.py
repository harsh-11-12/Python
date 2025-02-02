import random

def game(): 
    print("You are playing the game..")
    score = random.randint(1, 1000)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()

#####################################################
def generatetable(n):
    table=""
    for i in range(1,11):
        table+= f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}", "w") as f:
        f.write(table)


for i in range(2,21):
    generatetable(i)

line=1
with open("fiile.txt") as f:
    line=f.readline()