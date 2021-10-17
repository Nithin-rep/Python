my_name = "I_AM_KNIGHT_KING"
print(len(my_name))

breaker_at = int(input("enter the breaker point"))
loop = int((len(my_name)/ breaker_at))

for i in range(0,loop):
    print(my_name[(breaker_at * i) : (i* breaker_at + breaker_at)])
