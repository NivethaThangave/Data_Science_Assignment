import random
def dice():
    ''' The below is an interesting dice game for a single player. But what is interesting here 
    to play alone? Yes it’s because for each time when the player is throwing a dice the game 
    will collect a parts of a Beetle and form it to a complete structure. Okay That’s interesting…but how 
    to know which part will be collected for which dice thrown? The following are the scenarios 
    to get the beetle part. The dice 1 will give a Beetle Body, 2 will give a Head , 
    3 will give an Antenna, 4 will give an Eye, 5 will give a Mouth and 6 will give a leg.
    The Aim is to assemble a Beetle body which contains one Body, one Head, Two Antenna,
    Two Eyes, One Mouth and Six Legs.  But here are some rules to collect the beetle parts, 
    One cannot collect any parts directly and assemble a Beetle. The Body should be collected 
    first before any other parts and Head should be collected before collecting any Antennae,
    Eyes and Mouth.'''
    BeetleBody=False
    BeetleHead=False
    BeetleAntenna=False
    No_of_antenna=0
    BeetleEyes=False
    No_of_eyes=0
    BeetleMouth=False
    BeetleLegs=False
    No_of_legs=0
    Beetle = False
    print("START THE GAME by rolling the DICE...")
    print("The complete Beetle structure will be assembled by the below dice rules :")
    for n in range(0,200):
        dice_thrown=random.randint(1,6)
        if(dice_thrown==1 and BeetleBody==False):
            BeetleBody=True
            print("When throwing dice for " +str(n)+" th time, we got dice " + str(dice_thrown)+" Hence the Body got assembled for Beetle")
        elif(dice_thrown==2 and BeetleHead==False and BeetleBody==True):
            BeetleHead=True
            print("When throwing dice for " +str(n)+" th time, we got dice " + str(dice_thrown)+" Hence the Head got assembled for Beetle")
        elif(dice_thrown==3 and BeetleHead==True and BeetleAntenna==False and No_of_antenna<2):
            No_of_antenna=No_of_antenna+1
            print("When throwing dice for " +str(n)+" th time, we got dice " + str(dice_thrown)+" Hence the antenna no " + str(No_of_antenna) + " got assembled for Beetle")
            if(No_of_antenna==2):
                BeetleAntenna=True
        elif(dice_thrown==4 and BeetleHead==True and BeetleEyes==False and No_of_eyes<2):
            No_of_eyes=No_of_eyes+1
            print("When throwing dice for "+str(n)+" th time, we got dice " +str(dice_thrown)+" Hence the of eye " + str(No_of_eyes) + " got assembled for Beetle")
            if(No_of_eyes==2):
                BeetleEyes=True
        elif(dice_thrown==5 and BeetleHead==True and BeetleMouth==False):
            BeetleMouth=True
            print("When throwing dice for " +str(n)+" th time, we got dice " + str(dice_thrown)+" Hence the Mouth got assembled for Beetle")
        elif(dice_thrown==6 and BeetleBody==True and BeetleLegs==False and No_of_legs<6):
            No_of_legs=No_of_legs+1
            print("when throwing dice for " +str(n)+" th time, we got dice " +str(dice_thrown)+ " Hence the leg no " +str(No_of_legs) +" got assembled for Beetle")
            if(No_of_legs==6):
                BeetleLegs=True
        elif(BeetleBody==True and BeetleHead==True and BeetleAntenna==True and BeetleEyes==True and BeetleMouth==True and BeetleLegs==True and Beetle==False):
                print(" Congratulations!!!! You have Collected all the parts of the Beetle and assembled it.. The overall move is " + str(n))
                Beetle=True
    return("Hence the game is Over.!!!!!")
print(dice())
