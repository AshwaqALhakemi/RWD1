import random
guess_limit = 0
number = random.randint(10, 20)
print("Please Enter a number between 1 and 20.")
while guess_limit< 6 :
      guess = input("Enter a number: ")
      guess = int(guess)
      guess_limit = guess_limit + 1
      if guess < number:
            print ("Your number is too low.")
      elif guess > number:
            print ("Your numberis too high.")
      elif guess == number:
          guess_limit= str(guess_limit)
print ("Thank You")
