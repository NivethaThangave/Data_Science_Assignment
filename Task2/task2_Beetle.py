import random
def dice():
    ''' The below is an interesting dice game for a single player. But what is interesting here 
    to play alone? Yes it’s because for each time when the player is throwing a dice the game 
    will collect a parts of a Beetle and form it to a complete structure. Okay That’s interesting…but how 
    to know which part will be collected for which dice thrown? The following are the scenarios 
    to get the beetle part. The dice 1 will give a Beetle Body, 2 will give a Head , 
    3 will give an Antennaee , 4 will give an Eye, 5 will give a Mouth and 6 will give a leg.
    The Aim is to assemble a Beetle body which contains one Body, one Head, Two Antenna,
    Two Eyes, One Mouth and Six Legs.  But here are some rules to collect the beetle parts, 
    One cannot collect any parts directly and assemble a Beetle. The Body should be collected 
    first before any other parts and Head should be collected before collecting any Antennae,
    Eyes and Mouth.'''
    # Beetle parts initialization
    btleBody=False
    btleHead=False
    btleAntennaee =False
    no_of_antennaee=0
    btleEyes=False
    no_of_eyes=0
    btleMouth=False
    btleLegs=False
    no_of_legs=0
    beetle = False
    print("START THE GAME by rolling the DICE...")
    print("The complete Beetle structure will be assembled by the below dice rules :")
    # Throwing the dice from o to 200 to assemble the beetle and it will come automatically out of the loop if it assembles a beetle body before 200 counts
    for n in range(0,100):
        # using random.randint(1,6) to get the integer vakue randomly from 1 to 6 
        dice_thrown=random.randint(1,6)
        # when throwing dice 1 to get a body
        if(dice_thrown==1 and btleBody==False):
            btleBody=True
            print("When throwing dice for " +str(n)+" th time, we got dice " + str(dice_thrown)+" Hence the Body got assembled for Beetle")
        # when throwing dice 2 to get a head
        elif(dice_thrown==2 and btleHead==False and btleBody==True):
            btleHead=True
            print("When throwing dice for " +str(n)+" th time, we got dice " + str(dice_thrown)+" Hence the Head got assembled for Beetle")
        # when throwing dice 3 to get an anennaee
        elif(dice_thrown==3 and btleHead==True and btleAntennaee ==False and no_of_antennaee<2):
            no_of_antennaee=no_of_antennaee+1
            print("When throwing dice for " +str(n)+" th time, we got dice " + str(dice_thrown)+" Hence the antenna no " + str(no_of_antennaee) + " got assembled for Beetle")
            if(no_of_antennaee==2):
                btleAntennaee=True
        #when thriwing dice 4 to get eyes
        elif(dice_thrown==4 and btleHead==True and btleEyes==False and no_of_eyes<2):
            no_of_eyes=no_of_eyes+1
            print("When throwing dice for "+str(n)+" th time, we got dice " +str(dice_thrown)+" Hence the of eye " + str(no_of_eyes) + " got assembled for Beetle")
            if(no_of_eyes==2):
                btleEyes=True
        # when throwing dice 5 to get a mouth        
        elif(dice_thrown==5 and btleHead==True and btleMouth==False):
            btleMouth=True
            print("When throwing dice for " +str(n)+" th time, we got dice " + str(dice_thrown)+" Hence the Mouth got assembled for Beetle")
        # when throwing dice 6 to get a leg
        elif(dice_thrown==6 and btleBody==True and btleLegs==False and no_of_legs<6):
            no_of_legs=no_of_legs+1
            print("when throwing dice for " +str(n)+" th time, we got dice " +str(dice_thrown)+ " Hence the leg no " +str(no_of_legs) +" got assembled for Beetle")
            if(no_of_legs==6):
                btleLegs=True
        # to check all the parts got assembled and to complete the game        
        elif(btleBody==True and btleHead==True and btleAntennaee==True and btleEyes==True and btleMouth==True and btleLegs==True and beetle==False):
                print(" Congradulations!!!! You have Collected all the parts of the Beetle and assembled it.. The overall move is " + str(n))
                beetle=True
    return("Hence the game is Over.!!!!!")
print(dice())

