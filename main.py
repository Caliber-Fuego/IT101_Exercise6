dataSum = 0.0
dataAverage = 0.0
dataLength = 0.0
data = input("Enter a number or press Enter to quit: ")
while data != "": #sets the condition for the loop (while data is not equal to blank)
    number = float(data)
    dataLength += 1
    dataSum += number
    dataAverage = dataSum/dataLength
    data = input("Enter a number or just Enter to quit: ")
print("The sum is", dataSum,
      "\nThe average is", dataAverage)