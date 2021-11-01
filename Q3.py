list = []

while True:
    user_input = int(input())
    if user_input == -1:
        break
    list.append(user_input)

for i in list:
    print(i)
result = sum(list)
print("Sum=",result)