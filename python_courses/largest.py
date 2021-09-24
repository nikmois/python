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
        smallest = num
    elif largest is None:
        lergest = num
    elif largest > num:
        largest = num
    elif num < smallest:
        smallest = num

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
