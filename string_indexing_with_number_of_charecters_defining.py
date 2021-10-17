string = input("Enter the string you want to break: ")
print("The string length is {} " .format(len(string)))

breaker_at = int(input("Enter the number of charecters after which you want to break: "))
loop = int((len(string)/ breaker_at))

for i in range(0,loop):
    print(string[(breaker_at * i) : (i* breaker_at + breaker_at)])
