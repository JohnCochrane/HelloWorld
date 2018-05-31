print("This is a for loop")
for value in range(1,5):
    print(value)

print("\n")

print("This is a List and range")
odd_numbers = list(range(1,11,2))
print("Odd Numbers: " , odd_numbers , "\n")

even_numbers = list(range(2,11,2))
print("Even Numbers: " , even_numbers , "\n")

players = ["John", "Neil" , "Nik" , "Mike"]
print(players[0:3])

print("\n")
print("This is a Looping through a slice")
for player in players [:3]:
    print(player.title())

    