import random
import sys
import time
from colored import fg
import time
import msvcrt



blue = fg('blue')
red = fg('red')
normal = fg('orchid_2')
white = fg('white')
magenta = fg('magenta')
gold = fg("gold_1")
green = fg("green")


def slowprint(s, speed=0.01):
     for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(random.random() * speed)

def gameover():
    slowprint(""" 
  _____                         ____                 
 / ____|                       / __ \                
| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
    """)

def what():
    print(red +"===========================")
    slowprint(red + "||----What do you do?----||")
    print(red + "===========================" + white)

def br():
    print("===========================")

print("""
                                    |
                                    |
                                  .-'-.
                                 ' ___ '
                       ---------'  .-.  '---------
       _________________________'  '-'  '_________________________
        ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''
                      \    /  ||/   H   \||  \    /
                       '--'   OO   O|O   OO   '--'
""")

br()
slowprint("||You are on a falling plane!")
slowprint("||You dont remember anything that happened...")
what()
time.sleep(0.3)
slowprint("> 1. Try to open an emergency exit")
time.sleep(0.3)
slowprint("> 2. Look around")
time.sleep(0.3)
slowprint("> 3. Panic")
slowprint(green + "--------------------------------------------")
slowprint("\\\Press the number of your desired choice//")
slowprint(green + " -----------------------------------------" +white)

guards = 3



session_id = (msvcrt.getch().decode('ASCII'))

while True:
    if session_id == "1":
        slowprint("||You open the emergency exit door in midair... You are being sucked out of the plane!?")
        what()
        slowprint("|1. Close the door")
        slowprint("|2. Jump!!")
        session_id2 = (msvcrt.getch().decode('ASCII'))
        print(session_id2)
        br()
        if session_id2 == "1":
            slowprint("|| You close the door and manage to not fall out of the plane. However the guards in the plane have woken up from the loud noise and they knock you unconcious.")
            gameover()
            break


        elif session_id2 == "2": 
            slowprint("|| Well you jumped without a parachute. Nice one. You fall to your death.")
            gameover()
            break
        ## GAME OVER

        
    elif session_id == "2":
        slowprint("|| You are in the middle of the plane. You look behind you and see that all the passengers are knocked out.")
        slowprint("|| You see three unconcious guards on the back of the plane near the emergency exit")
        what()
        slowprint("> 1. Wake up the guards")
        time.sleep(0.3)
        slowprint("> 2. Try to rememeber")
        time.sleep(0.3)
        session_id2 = (msvcrt.getch().decode('ASCII'))

        #Wake up the guards
        if session_id2 == "1":
            slowprint("You try to wake up the guards. One of them wakes up and pulls a gun on you. Both of you seem confused. What is happening?")
            what()
            slowprint("> 1. Try to disarm him")
            slowprint("> 2. Try to run away")
            slowprint("> 3. Reason with him")
            
            session_id3 = (msvcrt.getch().decode('ASCII'))
            if session_id3 == "1":
                slowprint("You try to disarm the guard but he is too strong. He points the gun at you and shoots you")
                gameover()
                break
                
            #Run away from the Guards - Choose places to run to 2/3 safe, 1 bad
            elif session_id3 == "2":
                    slowprint("You try to run away but your options are limited")
                    what()
                    slowprint("> 1. Kick open the cabin door")
                    slowprint("> 2. Hide as one of the passengers")
                    slowprint("> 3. Run towards them")
                    session_id4 = (msvcrt.getch().decode('ASCII'))

                    if session_id4 == "1":
                        slowprint("You forgot that he has a gun. You get shot in the back and fall unconcious...")
                        gameover()
                    elif session_id4 == "2":
                        slowprint("You attempt to hide in the crowded seats, but they literally see you trying to hide. You get shot and fall unconcious")
                        gameover()
                    elif session_id4 == "3":
                        slowprint("You run towards them and knock the guy with the gun on the floor. The gun falls to the middle of the ground and you take it and shoot the guard")
                        slowprint("The other guards stand down and you are free to go to the cabin")
                        slowprint("\n You land the plane safely and live! ")
                        break

            elif session_id3 == "3": 
                    slowprint("It doesn't seem like the guards are in the mood to talk especially since a gun is pulled against you, yet you try but get shot instead")
                    gameover()
                    break
        if session_id2 == "2":
            slowprint("You try and try and try... but nothing comes to mind. You just wasted time. You hear the guards begin to wake up, capture you and you go unconcious")
            gameover()
            break


    #Panick Route
    elif session_id == "3":
        slowprint("|| Panicking is not a good option but you do so anyway. You wake up the unconcious guards.")
        what()
        slowprint("|1. Be friendly with the guards")
        slowprint("|2. Attack the guards")
        session_id2 = (msvcrt.getch().decode('ASCII'))
        slowprint("\n")
        

    #Run away or die route
        if session_id2 == "1":
            slowprint("|| They don't like how you look, so the guards ignore your friendly approach. They point a gun at you. What do you do?")
            

        #Bar Fight Route
        elif session_id2 == "2":
            slowprint("|| While you were panicking, you forget to count how many guards there are. There are 3 guards. \n || You begin a fist fight with the guards. Who do you target first? \n")
            slowprint("> 1. The left one")
            slowprint("> 2. The middle one")
            slowprint("> 3. The right one \n")
            session_id3 = (msvcrt.getch().decode('ASCII'))
            #Dies 
            if session_id3 == "1":
                slowprint("|| Oh no! You miss your punch and fall to the ground. \n The guards join forces and strike you. You fall unconcious. ")
                gameover()
                break
            #Dies
            elif session_id3 == "2":
                slowprint("|| You hit the guard! But your punch was so weak it didnt hurt him. \n The guards join forces and strike you. You fall unconcious.")
                gameover()
                break
            #Survive
            elif session_id3 == "3":
                slowprint("|| You obliterate the guard with a right hook punch, sending him flying. ")
                slowprint("There are two guards remaining.")
                what()
                slowprint("|1. Kick the guard on the left")
                slowprint("|2. Punch the guard on the right")
                br()
                session_id4 = (msvcrt.getch().decode('ASCII'))
                #survive
                if session_id4 == "1":
                    slowprint("The guard knew you would kick him, and he catches your kick and pins you to the floor. You fall unconcious.")
                    gameover()
                    break


                    
                # Lucky punch route
                elif session_id4 == "2":
                    slowprint("|| The guard on the right noticed your deadly gaze, and swiftly dodged your lunge and you fall to the ground. Not good.")
                    slowprint("Although you missed, there is some distance between you and the guards")
                    what()
                    slowprint("1. Run towards the cabin")
                    slowprint("2. Fight them off anyway")
                    slowprint("3. Try to talk your way through")
                    session_id5 = (msvcrt.getch().decode('ASCII'))

                    if session_id5 == 1:
                        slowprint("You swiftly turn your back to the guards and run towards the front of the plane. The cabin door seems locked so you jump kick the door open and somehow burst it open.")
                        #next location
                        br()
                        slowprint("There is nobody inside the cabin. How are we flying in the air without a pilot?")
                        slowprint("Instead of theorizing how, you rememeber the guards and how they are chasing you into the cabin.")
                        what()
                        slowprint("> 1. Close the door")
                        slowprint("> 2. Nosedive the plane")
                        session_id6 = (msvcrt.getch().decode('ASCII'))

                        if session_id6 == "1":
                            slowprint("You close the door, but forget that you broke the door to enter. The guards aprehend you and you fall unconcious.")
                            gameover()
                            break
                        elif session_id6 == "2":
                            slowprint("You nose dive the plane and the guards instantly fall towards you but are knocked out. You somehow manage to stay balanced and take control of the plane again")
                            slowprint("In the end you manage to land the plane safely and live")
                            slowprint("The end!")
                            break


                    elif session_id5 == 2:
                        slowprint("You foolishly attempt to brawl with them again but your attempt is cut short by an uppercut to your face. You fall unconcious")
                        gameover()
                        break

                    elif session_id5 == 3:
                        slowprint("For some reason, after punching a guard unconcious, you SOMEHOW think you can talk your way through this...")
                        time.sleep(1)
                        slowprint(blue + "It's... it's not what it looks lik-" + white)
                        slowprint("Your vision instantly goes black from the kick of one of the guards. You fall unconcious. ")
                        gameover()
                        break
    else:
        print(red + "Invalid option please try again." + white)