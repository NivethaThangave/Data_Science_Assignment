test_string = ["aaabbbccc","BATMAN","aabb"]
   
def encode(encoded_input):
  print("Passing the encoded Input string :" + encoded_input )
  encoded_output = ''
  data = ''
  encoded_input_check = any(i.isdigit() for i in encoded_input)
  print("Checking the Encoded_input value is an empty or it contains any integer values...")
  if(encoded_input == " "):
      print("Your Input string is empty, Please enter a proper non empty string value")
      return ""
  elif(encoded_input_check == True):
      print("Your Input contains a Numeric value, Please change it")
      return ""
  else:
   print("Hurray!!! your Encoded_Input is not empty and doesn't contain any integer value")   
   print("Creating a For-loop with range 0 to the length of the given encoded_input in order to get all the given encoded_input string as one by one character.")
  for i in range(0,len(encoded_input)):
   # To check if the data is empty or not if not the count will be assigned to 1    
   if (data==''):
      count = 1
   # To check if the iterated input string index character is equal to the character stored in the data or not, If its equal the count value will get increased to 1   
   elif (encoded_input[i]==data):
      count = count + 1
   # The below else part will be achieved when the abive two condition fails, will be succeed only when the previous and next character in a string are not equal, so the count will get assigned to 1 to calculate the new string.
   else:
      encoded_output = encoded_output+str(count)+data
      count = 1
   # storing the each iterated inout string data in data variable   
   data = encoded_input[i]
  # The encoded output will store the previous concatenated output value, its count and each iterated data stored in data variable. 
  encoded_output = encoded_output+str(count)+data
  #Returning encoded output for the function encode
  return(encoded_output)


def decode(a):
    # variable initializations
    data=''
    letterCount=0
    iterator =0
    internalIterator = 0
    # iterating the loop till it reaches the given length of the input string 
    while iterator<len(a):
        # checking whether the a[i] value is numeric or not, the a[i] value will get vary for each time when the i value get increased for each iteration..
        if(a[iterator].isnumeric()):
            letterCount = letterCount + int(a[iterator])
            internalIterator = internalIterator+1
            conditionCheck = False
            # checking the second charater whether its numeric or not
            for k in range(iterator+1,len(a)):
                if(a[k].isnumeric() and conditionCheck == False):
                    # To check and store if the encoded output contains any integer character value before 10
                    letterCount = (letterCount*10) + int(a[k])
                    internalIterator = internalIterator+1
                else:
                    # Initializing the conditioncheck to true in-order to stop the loop 
                    conditionCheck = True
                    
            iterator = iterator + internalIterator
            internalIterator=0
        for j in range(0, letterCount):
            data = data + a[iterator]
        letterCount = 0
        iterator = iterator+1
    return data 
# Creating the below function to check muliple input data in an array and print the result of encoded and decoded value.   
for word in test_string:
    print("Encoding Data: "+word)
    encodeoutput = encode(word)
    # To check the encodedoutput is empty or not, if  and print its value 
    if(not(encodeoutput  == "")):
        print("encodeoutput of "+word+": "+ encodeoutput)
        # calling decode function by passing encodedoutput as an input and storing it in decodeoutput.
        decodeoutput = decode(encodeoutput)
        # printing decodeoutput
        print('decoded output:'+ decodeoutput)
        # checking the encoded and decoded output length by subtracting them and storing it in a variable isencodlesser
        isencodlesser = len(encodeoutput) - len(decodeoutput)
        # if the differenciate value is less than zero then the encoded output length is less than decoded output length
        if(isencodlesser < 0):
            print("encoded output length is less than decoded output length")
        # if the differenciate value is greater than zero then encoded output length is greater than decoded output length
        elif(isencodlesser > 0):
            print("encoded output length is greater than decoded output length")
        # if both not satisfied then the length would be equal , so it will print the below statement, Both encoded output and decoded output length are equal   
        else:
            print("Both encoded output and decoded output length are equal")
            
    else: 'END'
       
