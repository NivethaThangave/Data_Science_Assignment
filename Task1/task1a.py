def e(input_data):
  output_data = ''
  storing_data = ''
  count = 0
  for i in range(1,len(input_data)-1):
   if (storing_data==''):
    count = 1
   elif (input_data[i]==storing_data):
    count = count+1 
   else:
    output_data = output_data+str(count)+storing_data
    count = 1
   storing_data = input_data[i] 
  output_data = output_data+str(count)+storing_data
  return(output_data)
outputData = e("kkkkk")
print("Output Value : "+ outputData)
