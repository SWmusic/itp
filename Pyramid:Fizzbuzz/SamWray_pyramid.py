stacks = int(input("How tall do you want your the pyramid be? (pick a number between 1 and 8): "))
if stacks < 1 or stacks > 8:
    print("YOU SHALL NOT PASS.")
    exit(1)
for i in range(0,stacks):
    for j in range(0, stacks-i):
        print(" ", end=' ')
    for k in range(stacks-i, stacks+1):
        print("#", end=' ')
    print()