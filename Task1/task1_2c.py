def encode(encoded_input):
  encoded_output = ''
  data = ''
  encoded_input_check = any(i.isdigit() for i in encoded_input)
  print("Checking the Encoded string value is empty or it contains any integer values...")
  if(encoded_input == " "):
      print("Your Input string is empty, Please enter a proper non empty string value")
      return ""
  elif(encoded_input_check == True):
      print("Your Input contains a Numeric value, Please change it")
      return ""
  else:
   print("Hurray!!! your Input String is not empty and doesn't contain any integer value.. so it's perfect to be encoded..")   
   print("Creating a For-loop with range 0 to the length of the given encoded_input in order to get all the given encoded_input string as one by one character.")
  for i in range(0,len(encoded_input)):
   if (data==''):
      count = 1
   elif (encoded_input[i]==data):
      count = count + 1
   else:
      encoded_output = encoded_output+str(count)+data
      count = 1
   data = encoded_input[i]
  encoded_output = encoded_output+str(count)+data
  return(encoded_output)


def decode(encrytpedValue):
    data=''
    letterCount=0
    iterator =0
    internalIterator = 0
    while iterator<len(encrytpedValue):
        if(encrytpedValue[iterator].isnumeric()):
            letterCount = letterCount + int(encrytpedValue[iterator])
            internalIterator = internalIterator+1
            conditionCheck = False
            for k in range(iterator+1,len(encrytpedValue)):
                if(encrytpedValue[k].isnumeric() and conditionCheck == False):
                    letterCount = (letterCount*10) + int(encrytpedValue[k])
                    internalIterator = internalIterator+1
                else:
                    conditionCheck = True
                    
            iterator = iterator + internalIterator
            internalIterator=0
        for j in range(0, letterCount):
            data = data + encrytpedValue[iterator]
        letterCount = 0
        iterator = iterator+1
    return data 

input_data = "APPLE" 
 
print("Input string: "+ input_data)
encodeoutput = encode(input_data)
print("Encoded Output of "+input_data+": "+ encodeoutput)
decodeoutput = decode(encodeoutput)
print('decoded output:'+ decodeoutput)
