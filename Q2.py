
# Write a python program that takes two numbers R and C as input and prints R * C 
# rectabgle of increasing numbers from 1 to C per row



R = int(input())
C = int(input())

for i in range(1, R+1):
    for j in range(1, C+1):
        print(j, end="")
    print()





