count_numbers = input()
numbers = input().split(" ")
weights = input().split(" ")

numbers = [int(number) for number in numbers]
weights = [int(weight) for weight in weights]

weighted_numbers = [number*weight for number,weight in zip(numbers,weights)]

print(round(sum(weighted_numbers) / sum(weights),1))
