sticks = 21

print("There are 21 sticks. you can take 1-4 number of sticks at a time")
print("Whoever take the last sticks will lose")

while True:
    sticks_taken = int(input("Take sticks(1-4):"))
    if sticks_taken >4 or sticks <1:
        print("Wrong choice")
        continue
    else:
        print("You take {} number of sticks".format(sticks_taken))
        print("Computer took {} number of sticks".format(5 - sticks_taken))
        sticks -= 5
        print("Sticks left", sticks)
        if sticks==1:
            print("Yout took the last stick, you loose")
            break
