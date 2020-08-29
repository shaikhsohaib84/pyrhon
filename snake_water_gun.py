import random
global n, userscore, pcscore
n = 10
userscore = 0
pcscore = 0
print("welcome to snake water gun")
flag = True
while flag:

    if n != 0:
        lst = ["snake", "water", "gun"]
        rnd = random.choice(lst)
        print("****Snake / Water / Gun****")
        user = input("enter your choice")
        user = user.lower()
        if user == "snake" and rnd == "water":
            userscore = userscore+1
            print("user won")
            print(f"user score{userscore}\n")
            print(f"pc score{pcscore}\n")
            n = n-1

        elif user == "snake" and rnd == "snake":
            print("same")
            continue

        elif user == "gun" and rnd == "gun":
            print("same")
            continue

        elif user == "water" and rnd == "water":
            print("same")
            continue

        elif user == "water" and rnd == "snake":
            pcscore = pcscore+1
            print("pc win")
            print(f"user score{userscore}\n")
            print(f"pc score{pcscore}\n")
            n = n-1

        elif user == "water" and rnd == "gun":
            userscore = userscore+1
            print("user win")
            print(f"user score{userscore}\n")
            print(f"pc score{pcscore}\n")
            n = n-1

        elif user == "gun" and rnd == "water":
            pcscore = pcscore+1
            print("pc win")
            print(f"user score{userscore}\n")
            print(f"pc score{pcscore}\n")
            n = n-1

        elif user == "snake" and rnd == "gun":
            pcscore = pcscore+1
            print("pc win")
            print(f"user score{userscore}\n")
            print(f"pc score{pcscore}\n")
            n = n-1

        elif user == "gun" and rnd == "snake":
            userscore = userscore+1
            print("user win")
            print(f"user score{userscore}\n")
            print(f"pc score{pcscore}\n")
            n = n-1

        else:
            print("wrong input")
    else:
        print("game over")
        print(f"user won : user score = {userscore}") if userscore > pcscore else print(f"pc won : pc score = {pcscore}")
        flag = False
        break
