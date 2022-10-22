print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("Which direction do you want to go? (left or right) ").lower()
if direction == "left":
  print("You ended up in front of a gay club")
  direction = input ("Go inside? (yes or no) ").lower()
  if direction == "no":
    print("Game over, you got robbed and shanked by a homless man :(")
  elif direction == "yes":
    print("A gay man approches you and hands you a drink.")
    drink = input("Do you drink it? (yes or no) ").lower()
    if drink == "yes":
      print("Game over, the drink had posinous seman")
    elif drink == "no":
      print("You threw away the drink and now have 3 doors you can enter.")
      doors = input("pink door? green door? blue door? ").lower()
      if doors == "pink door":
        print("Congrats, you are greeted by straight people and have beat the game")
      elif doors == "green door":
        print("Game Over, you are greeted by goblins who try to take your soul")
      elif doors == "blue door":
        print("Game over, you are greeted by a shark that try to eat you")
elif direction == "right":
  print("GAME OVER, you have walked on a IED and have been blown up!")
else:
  print("Please type exactly how it is shown!")
  





