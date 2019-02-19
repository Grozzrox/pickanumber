
import random
import time


name = input("Hey! What's your name? ")
print('Well, hello',name,'! Nice to meet you.')

time.sleep(3)

age = int(input("And how old are you? "))

if age > 25:
        print(age,"huh? Well, you're no spring chicken! 😂")
else:
        print("Wow! You're just a kid!")

time.sleep(3)

game = (input("Wanna play a game? "))

yes = True
no = False

if game == "Yes":
        print("Yay! I love a good game.")
elif "No":
        print("Boo! You're no fun.")

time.sleep(3)

print("This one's called magic trick. I'll give you five random numbers, and you pick one as your own. Then, I'll ask three questions and guess which number you picked!")

time.sleep(5)

ans1 = (input("Sound good? "))

if "yes" in ans1:
        print("Okay here we go!")
else:
        print("Whatever.")

time.sleep(3)

for i in range(5):
        print(random.randint(1,25))

time.sleep(3)

ans2 = (input("Got one? "))

num1 = 12

ans3 = (input("So...is your number less than 12? "))

time.sleep(2)

if ans3 == "Yes":
        print("Great!")
        ans4 = input("Is it less than 6? ")
        if ans4 == "Yes":
                ans6 = input(print("Cool! Is it less than 3? "))
                if ans6 == "Yes":
                        print("It's 2!!!")
                else:
                        print("It's 5!!!")
        else:
                ans5 = input(print("Hmm. Is it less than 9? "))
                if ans5 == "Yes":
                        print("It's 7!!!")
                else:
                        print("It's 11!!!")


else:
        ans7 = input(print("Okay no biggie! Is it less than 21? "))
        if ans7 == "Yes":
                ans8 = input(print("Alright-y. Is it less than 17? "))
                if ans8 == "Yes":
                        print("It's 15!!!'")
                elif ans8 == "No":
                        print("Whoops, I have absolutely no idea.")
        elif ans7 == "No":
                ans9 = input(print("Wow okay. Is it less than 23? "))
                if ans9 == "Yes":
                        print("It's 22!!!")
                elif ans9 == "No":
                        print("It's 24!!!")

time.sleep(3)

print("Thanks for playing,",name,"!!")


