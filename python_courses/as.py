largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = float(num)
    except:
        print("Invalid input")
        continue

    if smallest is None:
        smallest = int(num)
    elif int(num) < smallest:
        smallest = int(num)
    elif largest is None:
        largest = int(num)
    elif int(num) > largest:
        largest = int(num)

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
