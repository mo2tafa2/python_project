number = list(range(1, 21))
divisible_by_three = []
for num in number:
    if num % 3 == 0:
        divisible_by_three.append(num)
        print("numbers divisible by 3:", divisible_by_three)