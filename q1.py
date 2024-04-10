userNum = int(input("Enter any Number "))

for i in range(1, userNum + 1):
    if(userNum % i == 0):
        print(i)