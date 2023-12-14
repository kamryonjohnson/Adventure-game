while True:
  Answer = input ("Would you like to play ? (yes/no)")
  if Answer. lower().strip() == "yes":
    print ( "Welcome to the game! You are now the king of a small village in the middle of the forest. You have been tasked with protecting the village from the evil wizard. your first task is to find weapons. You have been given a map, Good luck King !")
    Answer = input ("You have reached a crossroad, would you like to go left or right?").lower().strip()
    if Answer == "left":
      Answer = input ("You encounter two of the evil wizard guards, would you like to run or attack?")
      if Answer == "attack":
        print ("That was not the greatest idea, you lost!")
      else:
        print("good choice, you made it away safely.")
        print("As you continue walking, you see a cavern. You hear a loud noise coming from the inside")
        Answer= input ("Do ` you want to go inside or continue walking? (go inside/continue walking)")
        if Answer == "go inside":
          print ("You have made it to the secret weapon cave")
          Answer = input ("You see a wall of weapons, would you like a sword or a bow?")
          if Answer == "sword":
            print ("You have chosen the sword, you can now fight the evil wizard")
            Answer= input("You decide to fight the wizard, would you like to fight in the woods or the village? (woods/village)")
            if Answer == "woods":
              print("you have chosen to fight in the woods, you have been ambushed by the wizards and his guards, you lose!")
            else:
              print("You have chosen to fight in the village, you have defeated the wizard and saved the village, you win!")
            
          else:
             print ("You have chosen the bow, you can now fight the evil wizard")
             Answer= input("You decide to fight the wizard, would you like to fight in the woods or the village?")
             if Answer == "woods":
              print("you have chosen to fight in the woods, you have climbed a tree and shot the wizard, you have defeated him and saved the village, you win!")
             else:
              print("You have chosen to fight in the village,you have been ambushed by the wizards and his guards, you lose!")
        else:
          if Answer == "continue walking":
            print ("You have chosen to continue walking, you have been attacked by the evil wizard, you lost!")
    elif Answer == "right":
        print ("You have ran into the evil wizard with no weapons to defend yourself, you lose!")
    else:
      print ("Invalid choice, you lost!")
    
  else:
    print ("Ok see you next time!")
    break