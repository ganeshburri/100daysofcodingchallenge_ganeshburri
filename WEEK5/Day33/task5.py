#square of numbers from 1 to 5
for i in range(1,6):
    print(i ** 2 )
#cube of numbers from 1 to 3
i=1
while i < 4:
    print(i ** 3)
    i += 1
#Reading a list using for-loop
list1 = ['Rich dad poor dad', 'The Alchemist', 'The 7 habits of highly effective people']
for book in list1:
    print(book)
#sum of numbers
sum = 0
while True:
    num = int(input("Enter a number: "))
    sum += num
    if num == 0:
        break
print("Sum of numbers is: ", sum)