import random
game=["rock","paper","scissor"]
x=input("Enter start to start game")
if x=="start":
    print("Starting game....")
else:print("Enter a valid option")
b=input("Enter what you want scissor,rock or paper: ")
game2=random.choice(game)
if game2==b:
    print(f"It's a tie,as bot entered {game2}")
elif game2=="rock":
    if b=="scissor":
        print(f"As bot entered {game2}, Rock has smashed your scissor!")
    else:print(f"As bot entered {game2}, your paper covers rock!")
elif game2=="scissor":
    if b=="paper":
        print(f"As bot entered {game2}, Scissor cuts you!")
    else:print(f"As bot entered {game2}, your Rock smashes scissor!")
elif game2=="paper":
    if b=="rock":
        print(f"As bot entered {game2}, paper covers your rock!")
    else:print(f"As bot entered {game2}, your scissor cuts paper")
