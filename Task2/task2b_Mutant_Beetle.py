import random        
def mutant_beetle():
    
    body = False
    head1 = False
    head2 = False
    beetle_mouth_1 = False
    beetle_mouth_2 = False
    antennae_head_1 = False
    antennae_head_2 = False
    eyes_head_1 = False
    eyes_head_2 = False
    legs = False
    antennae_count_head_1 = 0
    antennae_count_head_2 = 0
    eyes_count_head_1 = 0
    eyes_count_head_2 = 0
    legs_count = 0
    
    print("Start the game to assemble a Mutant Beetle parts by throwing a dice!!!")
    for n in range(1,100):
        dice = random.randint(1,6)
        
        if(dice == 1 and body == False):
            print("When throwing for the  " + str(n) + " time we got dice "+ str(dice) +" Hence the body got assembled for Mutant Beetle." )
            body = True
        
        elif(body == True and dice == 2 and head1 == False): 
            print("When throwing for the " + str(n) + " time we got dice "+ str(dice) + " Hence , The Head 1 got assembled for Mutant Beetle.")
            head1 = True
        
        elif(body == True and dice == 2 and head2 == False and head1 == True): 
            print("when throwing for the " + str(n) + " time we got dice "+ str(dice) + " Hence, The Head 2 got assembled for Mutant Beetle.")
            head2 = True
        
        elif(body == True and dice == 6 and legs == False and legs_count < 6):
            legs_count = legs_count + 1 
            print("when throwing for the " + str(n) + " time we got dice " + str(dice) + " Hence the leg number", str(legs_count) + " got assembled for Mutant Beetle.")
            if(legs_count == 6):
                legs = True
        
        elif(head1 == True and dice == 3 and antennae_head_1 == False and antennae_count_head_1 < 2):
            antennae_count_head_1 = antennae_count_head_1 + 1
            print("when throwing for the " + str(n) + " time we got dice " + str(dice) + " Hence the Antenna", str(antennae_count_head_1), " for Head 1 got assembled for Mutant Beetle.")
            if(antennae_count_head_1 == 2):
                antennae_head_1 = True
        
        elif(head2 == True and dice == 3 and antennae_head_2 == False and antennae_count_head_2 < 2 and antennae_head_1 == True):
            antennae_count_head_2 = antennae_count_head_2 + 1
            print("when throwing for the " + str(n) + " time we got dice " + str(dice) +  " Hence the Antenna", str(antennae_count_head_2), "  for Head 2 got assembled for Mutant Beetle.")
            if(antennae_count_head_2 == 2):
                antennae_head_2 = True
        
        elif(head1 == True and dice == 4 and eyes_head_1 == False and eyes_count_head_1 < 2):
            eyes_count_head_1 = eyes_count_head_1 + 1
            print("when throwing for the " + str(n) + " time we got dice " + str(dice) +" Hence the eye", str(eyes_count_head_1), " for Head 1 got assembled for Mutant Beetle.")
            if(eyes_count_head_1 == 2):
                eyes_head_1 = True
        
        elif(head2 == True and dice == 4 and eyes_head_2 == False and eyes_count_head_2 < 2 and eyes_head_1 == True):
            eyes_count_head_2 = eyes_count_head_2 + 1
            print("when throwing for the " + str(n) + " time we got dice " + str(dice) + " Hence the eye", str(eyes_count_head_2), " for Head 2 got assembled for Mutant Beetle. ")
            if(eyes_count_head_2 == 2):
                eyes_head_2 = True
        
        elif(head1 == True and dice == 5 and beetle_mouth_1 == False):
            print("when throwing for the " + str(n) + " time we got dice " + str(dice) + " Hence , The Mouth 1 got assembled for Mutant Beetle.")
            beetle_mouth_1 = True
        
        elif(head2 == True and dice == 5 and beetle_mouth_2 == False and beetle_mouth_1 == True):
            print("when throwing for the " + str(n) + " time we got dice "+str(dice)+ " Hence , The Mouth 2 got assembled for Mutant Beetle.")
            beetle_mouth_2 = True
        
        elif(head2 == True and legs_count == 6 and antennae_count_head_2 == 2 and eyes_count_head_2 == 2 and beetle_mouth_2 == True): 
            print("The mutant beetle has been assembled when throwing the dice for "+ str(n)+ " time")
            print("Hence the Mutant beetle game has been finished")
            return(True)
        
print(mutant_beetle())
