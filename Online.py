print("importing...")
import random
import time

print("setting vars...")
global air
air = 5

print("defining functions...")
def die():
  print("You died")
  PA = input("Would you like to play again? (y/n)\n")
  if PA == "y" or PA == "Y":
    start()
  else:
    print("Thanks for playing!")
    time.sleep(3)
    exit()

def start():
  global air
  air = 5
  print("This is air gambling. You have 5 air. You can gamble the air to get more. If you run out of air, you die.")
  game()

def game():
  global air
  amt = input("how much air would you like to gamble\n")
  if int(amt) > air:
    print("You do not have enough air for that bet!")
    time.sleep(.5)
  else:
    if random.randint(1, 2) == 1:
      if random.randint(1, 4) == 1:
          if random.randint(1, 6) == 1:
              if random.randint(1, 8) == 1:
                air = air + int(amt) + int(amt) + int(amt) + int(amt) + int(amt) + int(amt) + int(amt) + int(amt) + int(amt) + int(amt)
                print("JACKPOT!!! 10x your air! You now have " + str(air) + " air")
                time.sleep(.5)
              else:
                air = air + int(amt) + int(amt) + int(amt)
                print("you QUADRUPLED your air! You now have " + str(air) + " air!")
                time.sleep(.5)
          else:
            air = air + int(amt) + int(amt)
            print("you TRIPLED your air! You now have " + str(air) + " air!")
            time.sleep(.5)
      else:
        air = air + int(amt)
        print("You doubled your air! You now have " + str(air) + " air.")
        time.sleep(.5)
    else:
      if random.randint(1, 5) == 1:
        air = air - int(amt) - int(amt)
        print("You lost " + str(int(amt) * 2) + " air (twice as much as you put in). You now have " + str(air) + " air.")
      else:
        air = air - int(amt)
        print("You lost " + amt + " air. You now have " + str(air) + " air.")
      time.sleep(.5)
      if air <= 0:
        die()
  game()

start()
