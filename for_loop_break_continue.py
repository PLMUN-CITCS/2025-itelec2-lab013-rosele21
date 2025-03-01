numbers = list(range(1, 11))
for num in numbers:
    if num == 3:
        continue  # Skip the rest of this iteration
    if num == 7:
        break  # Exit the loop completely
    print(num)