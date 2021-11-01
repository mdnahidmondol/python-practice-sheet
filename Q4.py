number_list = []

user_input = input()

while user_input.upper() != "STOP":
    number_list.append(int(user_input))
    user_input = input()
    print("User input",user_input)
    
frequency_number = {}

for i in number_list:
    if (i in frequency_number):
        frequency_number[i] +=1
    else:
        frequency_number[i] = 1
for key,value in frequency_number.items():
    print(key,"-",value,"times")