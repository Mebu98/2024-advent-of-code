## First we get all the numbers in the file
inputFile = open("input.txt", "r")
inputArr = inputFile.read().split()

## Then we split based on index being even or odd to get the two arrays
arr1 = inputArr[slice(0, len(inputArr), 2)]
arr2 = inputArr[slice(1, len(inputArr), 2)]

## Sort both arrays in ascending order
arr1.sort()
arr2.sort()

## Calculate distance for every index
sumDistance = 0

for i in range(0, len(arr1)):
    num1, num2 = int(arr1[i]), int(arr2[i])
    distance = abs(num1 - num2)
    sumDistance += distance

print(f'Distance: {sumDistance}')