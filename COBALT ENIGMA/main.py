c
#COBALT ENIGMA
#Adapted from Original Version [2020, C++]

#By Madhan Selvaraj, 2F

#Library Declarations
import sys 
import time
from os import system, name 


#Typing Animation Function Declaration
def mprint(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.10)
    print


#Slow Typing Animation Function Declaration
def mslowprint(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)
    print


#Fast Typing Animation Function Declaration
def mfastprint(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)
    print


#Searching Function Declaration
book=1
def search():
  if n=="s":
    print


#Screen Clearing Function Declaration
def clear():  
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')


#Game Intro
clear()
mprint("Welcome to Cobalt Enigma!\n\a")
time.sleep(1)
#Useful Links
print("Before we start our game, here are some useful links that you may need later. \n\n")
time.sleep(2)
print("For Multi-lingual Translations : \n")
mfastprint("      - translate.google.com \n\n")
time.sleep(1)
print("For Encoding/Decrypting : \n")
mfastprint("      - cryptii.com \n\n")
time.sleep(1)
print("For The Periodic Table of Elements : \n")
mfastprint("      - ptable.com \n\n")
time.sleep(2)
clear()


#Final Tips
print("You might also need a notepad, or documenting application. \n")
print("Using headphones for sounds is recommended to provide the best experience.\n")
time.sleep(5)


#Start Confirmation
n=input("Input c to begin, once you are ready! \n\a")



#******************************************
#*****THE GAME HAS OFFICIALLY STARTED *****
#******************************************



#Scene 1 - Waking Up
if n=="c" or n=="C":
  mfastprint("\n\n\n\n\n\nYou wake up abruptly.\n Once the brightness of the area sets in, you begin to feel conscious.\n You squint your eyes, and realise that you are trapped inside some sort of pod.\n Wires connect the chamber to a metallic box, with flashing lights and buttons.\n Noting these surroundings, you push on the door of the pod instinctively.\n It opens, and you climb out.\n Your knees buckle, and you fall to the floor.\n Weakness and nausea spread throughout your entire being.\n You stagger to the end of the room, where a computer is stationed.\n")
else:
  print(n=input("Input c to continue, once you are ready to begin! "))
mfastprint("\n\n\nYou pull a chair under you and peer into the dusty monitor. You instintively power the computer on. Text fills the screen.\n")
time.sleep(3)
clear()


#Recording User Data
time.sleep (1);
username = input("Account Login\a\n Username: ")
print("Password\a: \n\n\n")
time.sleep (1);
mfastprint("Somehow, the passcode is in your memory right now. It could be anything, but you are sure that you should know it. You reach into your memory and pull out an answer. How did you know it? You have never seen this place in your life. But still, you type it in\n\n\n");
time.sleep(2)
clear()
print("Logging in...")
time.sleep(2)
clear()
print("Welcome, "+username+"\a")
time.sleep(2)
print("Welcome to the Chemical Laborotary Research Database.\n")
print("Please Enter Your Key\n\n\n")


#Scene 2 - What Key Does It Want?
mprint("Huh? Key?\n")
mfastprint("You have no idea where you are and your only hope just died. You slump your head on the desk and try to stop your throbbing headache. You try to recall why you are in this strange place but nothing comes to your mind. That's when something finally dawns on you, you don't even remember your name...\n\n\n")
mprint("Something catches your eye. A post-it note under the table. You carefully pick it up.")
time.sleep(2)
clear()


#Losing Sequence
def gameover():
  mfastprint("You have lost.")
  mfastprint("Through your desperate attempts to find an explanation, an answer for this madness, you let go and now you are eternally lost.\n Fated to oblivion without being physically bound.\n The world shall move on, but at the cost of what?\n")
  mfastprint("If you wish to play again, there may be another chance. If you wish not to, however, \n\n\n\n you are but a speck in the vast tragedy of the Universe.")
  mfastprint("Game Over")
  exit()


#Obtaining Floorplan
def postit():
  print("-----------------------------")
  print("|  The KEy is     fOunD     |")
  print("|   in tHe Chem Lab journal |")
  print("| -987                      |")
  print("-----------------------------")
postit()
time.sleep(3)
print("\n\n You flip it over to find a floorplan\n\n")
def floorplan():
  print("-----------------------------" )
  print("|   [Room 986]===[Room 987] |" )
  print("|      ||            ||     |" )
  print("|   [Crypod]======[Library] |" )
  print("|      ||                   |" )
  print("|   [Study]=====[Cafeteria] |" )
  print("-----------------------------")
floorplan()
mprint("You realise that you are in the crypod chamber. You decide to head out and get that key in room 987 and possibly get some help.")
time.sleep(3)
clear()
print("(You have obtained the floorplan and it has been added to your items to ever view it again, enter floorplan.)\n")
print("Now use w,a,s,d to move to other rooms")
time.sleep(8)
clear()
mprint("Could the 987 mean the room number? Go check.\n")
level=0
room=0


#Room Movement [R0, L0]
while room==0 and level==0:
  n=input("Where do you want to go?")
  if n == "floorplan" or n == "Floorplan":
    floorplan()
  elif n=="w" and level==0:
    print("You have entered room 986")
    room+=1
  else:
    print("You can't go there now")


#Room Movement [R1, L0]
while room==1 and level==0:
 n=input("Where do you want to go now?")
 if n == "floorplan" or n == "Floorplan":
    floorplan()
 elif n=="d" and level==0:
    print("You have entered room 987")
    room+=1
 else:
    print("You can't go there now") 

h=0
#Room Searching
while h==0:
  if room==2 and level==0:
    n=input("Press s to search a room")
    if n=="s" or n=="S":
      mprint("ITEMS\n1.Pen\n2.Encyclopedia\n3.A set of journals\n4.A piece of tissue paper\n5.A book entitled jnjfy7g\n" )
      h+=1
    else:
      print(".")
    

#Examine Pen
def pen():
  mprint("Pen: A black fountain pen with the words \"I love chemistry\" engraved at the top\n" )


#Examine Encyclopedia
def encyc():
  mprint("Encyclopedia: A thick book which is the revised version of the Encyclopedia\n")


#Examine Tissue Paper
def tp():
  mprint("A piece of tissue paper: A piece of tissue paper on the floor with some thing on it\n")


#Examine Book
def jnj():
  mprint("A book entitled jnjfy7g: A book with random gibberish\n")


#Examine Journals
def journals():
  global book
  global level
  mprint("A set of Journals: Three journals piled up on top of each other without labels. One has pencil graphs and drawings, another has cursive writing in black ink and the last one has wierd symbols in blue ink\n")
  m=input("Which one of these three books (1, 2 or 3) would you like to take? If you are unsure go explore the other items for clues first by pressing s")


 #Examine Journal 2
  if m=="s" or m=="S":
    print(".")
  elif m=="2": 
    book+=1
    print("You pick up the book and two pieces of paper fall out")
    time.sleep(2)
    print("--------------------------------")
    print("| Dear Mr Steven, \n ;Firstly, |")
    print("|we congratulate you on your   |")
    print("|success in getting into the   |")
    print("|  royal association.\n        |")
    print("|        Your key:  COBALT     |")
    print("--------------------------------")
    mfastprint("Congragulations! You have found the key and it has been added to your items ")
    mfastprint("You also find a piece of a diary entry read it later once you have entered the key")
    level=1

    
 #Examine Journal 1, Journal 3
  elif m=="1" or m=="3":
    print("You have chosen the wrong book. If you are unsure go explore the other items first to get clues")
book=0


#Further Investigation Menu
while book==0:
  s=input("Which one of these items in this room would you like to pick up and investigate further.")
  if s=="a set of journals" or s=="A set of journals":
    journals()


 #Trigger the pen description
  if s=="Pen" or s=="pen":
    pen()
 

 #Trigger the encyclopedia description
  elif s=="encyclopedia" or s=="Encyclopedia":
    encyc()
       

 #Trigger the tissue description
  elif s=="A piece of tissue paper" or s=="a piece of tissue paper":
    tp()


 #Trigger the book description
  elif s=="A book entitled jnjfy7g" or s=="a book entitled jnjfy7g":
    jnj()

 
 #Trigger Item Suggestion Rejection Sequence
  else:
    print("Item not in this room")


#Enter Lab Key
time.sleep(3)
clear()
mfastprint("You rush back to the crypod chamber to enter the key")
time.sleep(1)
clear()
r=input("Please enter your key:\n")
if r=="COBALT":
  print ("loading...") 
elif r=="key" or r=="Key": 
  print("--------------------------------")
  print("| Dear Mr Steven, \n ;Firstly, |")
  print("|we congratulate you on your   |")
  print("|success in getting into the   |")
  print("|  royal association.\n        |")
  print("|        Your key:  COBALT     |")
  print("--------------------------------")
else:
  print("The key is incorrect. All files self destructing in -5- seconds\n")
  gameover ()
clear()


#Diary Entry
mprint("You take out the diary entry you found previously while the computer loads...\n\n\n")
mfastprint("It is late at night when I am writing this.\n The neuro-virus, The Enigma,  has started to spread in exponential amounts across the globe.\n Today I have studied its general effects.\n The results have alarmed me.\n Many symptoms include pontentially permanent memory loss and extreme weakness.\n As I am writing this, many more thousands globally are getting affected.\n So far, all the treatments we have tried have worked to no avail.\n Hospitals and medical wards around the world are getting flooded with occupants.\n What is this enigmatic virus, and where did it come from?\n\n\n")
print("you are perplexed by this but get distracted by the computer beeping")
time.sleep(3)
print("\a\a\a\a\a\a\a\a\a\a\a\a")


#Scene 3 - File of Existential Answers
print("The computer boots up")
mprint("You are shocked and terrified to find that the only file pinned on the computer was named \"why you are here (Library)\". With trembling hands you click on it")
clear()
print("\a\a\a LOCKED FILE \n ENTER PASSCODE TO VIEW:")
time.sleep(1)
mprint("What kind of sick game was someone playing with you? You were out of your mind with exhaustion yet you trudge on to the library to find a way chance to escape or at survive(objective-Find the password in the library to enter the locked file\n")

room=0
level=1
#Room Movement [R0]
while room==0 and level==1:
  n=input("Where do you want to go?")
  if n == "floorplan" or n == "Floorplan":
    floorplan()
  elif n=="w" and level==1:
    print("You have entered room 986")
    room+=1
  elif n=="d" and level==1:
    print("You have entered the library")
    room+=3
  else:
    print("You can't go there now")


#Room Movement [R1]
while room==1 and level==1:
  n=input("Where do you want to go?")
  if n == "floorplan" or n == "Floorplan":
    floorplan()
  elif n=="d" and level==1:
    print("You have entered room 987")
    room+=1
  elif n=="s" and level==1:
    print("You have returned to the crypod chamber ")
    room-=1
  else:
    print("You can't go there now")


#Room Movement [R2]
while room==2 and level==1:
  n=input("Where do you want to go?")
  if n == "floorplan" or n == "Floorplan":
    floorplan()
  elif n=="s" and level==1:
    print("You have entered the library")
    room+=1
  elif n=="a" and level==1:
    print("You have returned to room 986")
    room+=3
  else:
    print("You can't go there now")
clear()


#Room Movement [R3]
if room==3 and level==1:
 #Scene 4 - The Library
  mfastprint("How odd, the library has absolutely no books in it. Chairs are upturned and papers are strewn across the floor. There is a singular safe in the center of the room. You assume the password was in the safe. Muttering under your breath, you approach it to find that it is locked. You try forcing it open but it does not work. You notice that the safe has no markings on it except for one in the corner\n ")
  mfastprint(" - .- -. - .- .-.. ..- -- \n This is your only chance at opening the safe, enter the code. Type h for a hint\n")
y=0


#Safe found and Unlocked
while y==0:

  d=input("CODE:")

  if d=="tantalum" or d=="Tantalum":
    mprint("Correct! The safe unlocks with a click and you retrive note with the passcode and along with it another diary entry...")
    print("--------------------------")
    print("|The  passcode is        |")
    print("|       EDOCSSAP         |")
    print("--------------------------")
    mprint("Congrats you have obtained the passcode (which has been added to your items) and another diary entry. To ever view the passcode again, enter passcode")
    y+=1
  elif d=="h" or d=="H":
    print("Popularised in the 1830, this was based purely on binary. It was used to transmit messages over distances (especially on ships), but can only by transmitted letter by letter.\n")
  else:
    
    mprint("That is incorrect. The safe starts beeping and goes into lockdown. \n")
    gameover()


#New File Passcode found
time.sleep(5)
clear()
mprint("You rush back to the crypod to enter the passcode you just got into the computer.")
time.sleep(1)
clear()
t=input("\a\a\a LOCKED FILE \n ENTER PASSCODE TO VIEW:")
h=0


#New Passcode Verification
while h==0:
  if t=="EDOCSSAP":
    print("ENTRY PERMITTED\n\a Opening text file...")
    clear()


   #Diary Entry
    mprint("You decide to read the diary entry you found in the safe while waiting for the file to open...\n\n")
    mfastprint("I just finished my shift at the laboratory.\n I have been working overtime on some Antidotes in the quarantine zone. Like I predicted the virus is spreading like wildfire. Entire nations are going into lockdown and populations are dropping like flies\n We have made some discoveries on cell deconstruction and have developed an incubation/cryostasis chamber that can house a single person.\n The chamber can release and replace particles constantly so as to preserve a body during its recovery.\n It cannot cure the virus.\n However, it can numb the effects of the Enigma. We only have a few at the laboratory which is good as all the prolonged exposure to the virus during research is sure to infect someone. However we are unable to mass produce these as the cost of making these is extreme.\n\n\n\n")
    mfastprint("You start wondering about these diary entries. What are these... \"viruses\". Your brain hurts too much to think you just look up to see that the file has opened")
    h+=1
    clear()
  elif t=="passcode":


   #Passcode
    print("--------------------------")
    print("|The  passcode is        |")
    print("|       EDOCSSAP         |")
    print("--------------------------")
  else:
     print("The key is incorrect. All files self destructing in -5- seconds\n")
     time.sleep(1)
     print("The key is incorrect. All files self destructing in -4- seconds\n")
     time.sleep(1)
     print("The key is incorrect. All files self destructing in -3- seconds\n")
     time.sleep(1)
     print("The key is incorrect. All files self destructing in -2- seconds\n")
     time.sleep(1)
     print("The key is incorrect. All files self destructing in -1- seconds\n")
     time.sleep(1)
     gameover()


#Scene 5 - The Cafeteria
print("Only you can save the world. You have come this far. Don't give up. Go to the cafeteria.\n\n")  
mfastprint("GOD DAMN IT! You scream as you kick the chair you were seated on. You could barely remember your name and this thing is telling you that only you can save the world. But you realise your only chance of busting out of this place is to do what the computer tells you to do. You storm off to the cafeteria...")
clear()
level=2


#Room Movement [R0]
while room==0 and level==2:
  n=input("Where do you want to go?")
  if n == "floorplan" or n == "Floorplan":
    floorplan()
  elif n=="s" and level==2:
    print("You have entered the study")
    room+=4
  elif n=="d" and level==2:
    print("You have returned to the library")
    room+=3
  elif n=="w" and level==2:
    print("You have returned to room 986")
    room+=3
  else:
    print("You can't go there now")


#Room Movement [R4]
while room==4 and level==2:
  n=input("Where do you want to go?")
  if n == "floorplan" or n == "Floorplan":
    floorplan()
  elif n=="w" and level==2:
    print("You have returned to the crypod chamber")
    room+=4
  elif n=="d" and level==2:
    print("You have entered the cafeteria")
    room+=1
  else:
    print("You can't go there now")


#Room Movement [R5]
if level==2 and room==5:
  mprint("The cafeteria also looked post-apocalyptic wasteland. There was a tattered cardboard box on one of the few upright tables. You approach it and open it with much anticipation to be dissapointed by two pieces of paper and a syringe.\n\n You unfold one of the papers to read it. It was another diary entry\n\n\n\n")


#Diary Entry
mfastprint("I just got sick.\n My temperature has risen to around 42 degrees celsius.\n This is not normal.\n I could not move today, and I feel weak.\n I did not really do much today.\n I just took rest.\n I called my co-worker Jack today.\n He told me that no other discoveries were made.\n I felt better at around 4, and reported to work for a while.\n I did some research and discovered something peculiar.\n Certain elements reacted to the infected cells differently.\n I will go and research more on this tomorrow.\n Most of my colleagues got infected yesterday, and have been put in their respective crytosis chambers.\n We need to come up with something swiftly or this could be the end.\n\n\n")


#Nato Found
mprint("What was up with all these diary entries??? They made no sense and why were they left here for you? You toss it aside and open the other piece of paper...")
print("-------------------------------------")
print("| cUrE In brIEf CAsE                |")
print("|                       in stUdy    |")
print("|                                   |")
print("|                                   |")
print("|   OscAr                           |")
print("|           x-rAy            yAnkEE |")
print("|     gOlf               EchO       |")
print("|             nOvEmbEr              |")
print("-------------------------------------")
mprint("Congrats you have obtained the breif case clue (which has been added to your items) and a syringe. To ever view the clue again, enter clue\n")


#Room Movement [R5]
level=3
while room==5 and level==3:
  n=input("Where do you want to go?")
  if n == "floorplan" or n == "Floorplan":
    floorplan()
  elif n=="a" and level==3:
    print("You have returned to the study")
    room-=1
  else:
    print("You can't go there now")


#Dustbin description
def dustbin():
  print("Dustbin: Just a regular dustbin (You must be very desperate to attempt to investigate this )")


#Drawer description
def drawer():
  print("Drawer: A locked Drawer")
  
  
#Key description
def key():
  print("Key: A key lies on the table\n ")
  t=input("would you like to use it on the locked drawer (yes or no)?")
  if t=="yes" or t=="Yes":
    mprint ("You slowly insert the key into the drawer's lock and turn it and to your amazement it works! You open the drawer excitedly with a flourish... Only to discover it to be empty. Keep searching. ")
  else:
    print("continue searching")


#Closet description
def closet():
  global raghav
  print("Closet: A closet in the corner of the room\n")
  o=input("Would you like to open the closet(yes or no)?")
  if o=="yes" or o=="Yes":
    mprint ("YES! You found it you found the breif case")
    time.sleep(3)
    raghav+=1
  else:
    print("continue searching")

def WHO():
  print("A research update to WHO: A research update to WHO explaining the severity of the situation (**This could be the very end of the human kind as we know it**)")


#Searching a room

if room==6 and level==3:
  n=input("Press s to search the room")
  if n=="s" or n=="S":
    mprint("ITEMS\n1.Dustbin\n2.Drawer\n3.key\n4.Closet\n5.A research update to WHO\n" )


#Further Further Investigations
raghav=0
while raghav==0:
  s=input("Which one of these items in this room would you like to pick up and investigate further:")
  if s=="dustbin" or s=="Dustbin":
    dustbin()
  elif s=="Drawer" or s=="drawer": 
    drawer()
  elif s=="Key" or s=="key":
    key()
  elif s=="Closet" or s=="closet":
    closet()
  elif s=="A research update to WHO" or s=="a research update to WHO":
    WHO()


#Opening the briefcase
clear()
mprint("You grasp the breif case by the handle and take it out of the closet. It is locked with a letter-lock passcode (All caps). Use the clue you found at the cafeteria to open it. Enter H for help and clue to view it again.")
p=0
i=input("Enter passcode:")
while p==0:
  if i=="OXYGEN":
    print("The lock opens with a click and you open it...")
    p+=1
  elif i=="case" or i=="Case":
    print("-------------------------------------")
    print("| cUrE In brIEf CAsE                |")
    print("|                       in stUdy    |")
    print("|                                   |")
    print("|-----------------------------------|")
    print("|   OscAr                           |")
    print("|           x-rAy            yAnkEE |")
    print("|     gOlf               EchO       |")
    print("|             nOvEmbEr              |")
    print("-------------------------------------")
  elif i=="h" or i=="H":
    print("Nato code")
  else:
    print("Incorrect.\n You have lost")
    gameover()
mfastprint("Inside the brief case are vial, a id card and two piece of paper a final diary entry and a instruction manual. You sit at the desk and start readind the diary entry...\n\n\n\n\n")


#Diary Entry
mfastprint("\aThe day has finally come.\n I am writing this in pure shock.\n All my colleagues are now unwell.\n  I looked at some of our experimental set-ups, and have located several of the previously mentioned elements.\n This diary that I am writing will serve to restore my memory on these events after I climb into my cryptosis chamber.\n I helped some of my colleagues into their chambers, and I looked through some papers.\n With this knowledge, I formulated a chemical equation.\n This could mean the life or death of our species.\n I do not think I will be strong enough to create this compound. I have only concocted a small vial.\n I need to go into cryptosis chamber quick.\n`I made multiple obstacles for myself to reach the cure's instructions and a vial of it for myself, for safety measures. If I find this, please use the syringe and vial to cure yourself and with the chemical formula and instructions, go out and save the world(There is a emergency exit behind the food stall)  This might be my last message to the world.\n If I or anyone else finds this in the future I want you to remeber that there was a beautiful world we used to have.")
time.sleep(1)
clear()


#Final Scene ~ All comes together
mfastprint("You sit back, eyes tearing up from the strain. You were him and he was you all along, Dr Steven. You look up to the dim lights of the room, confusion and messy thoughts flowing everywhere in your mind.  You stagger over to the edge of the room. There is a huge assortment of elements in cupboards on the wall. Many doubts plague your mind. Did the elements have to be at a certain state? Was there an order to it? There was no time to care about the specific details. You grappled at the containers. The chemical chamber of silver caught your eye. The letters Ar seemed to be calling out to you. Your breathing is shallow, due to the unfriendly environment. In a matter of minutes, you have grabbed all the elements and ripped them out of the capsules. You put a small sample of each in a test-tube. Sparks light up and electrical pulses dance through the tube. You grasp it with frail fingers and put it in a chemical centrifuge. You watch its perform its hypnotic swirl that adds to your throbbing headache. You pull out the tube, which now glowed a lucid bright blue. It reminded you of something special. Of something always there when you were growing up. The great magnificent void above everyones heads. Was it the sky? You snap back to reality. Your mind thinks of so many possibilities. Your spirit soars. Maybe, just maybe there is a happy ending.\n")
time.sleep(1)
clear()


#End sequence
mfastprint("***********************************\n")
mfastprint("C  O  B  A  L  T   E  N  I  G  M  A\n")
mfastprint("***********************************\n")
time.sleep(2)
clear()