import random
print("i am thinking of a number between 1 and 100")
print("can you guess it?")
generate_number=random.randint(1,100)
attempt=0
while True:
    guess=int(input("Enter your guess:"))
    attempt=attempt+1
    if guess<generate_number:
        print("Too low!")
    elif(guess>generate_number):
        print("Too high!")
    else:
        print(f"your guess is right.it is {generate_number}")
        print(f"you won at {attempt} attempt!congrats")
        break

        