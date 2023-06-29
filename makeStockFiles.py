import uuid
with open("all_stocks_5yr.csv") as file:
    lines = [line.rstrip() for line in file]

id = ""
testdata = open(f"testdata-{id}.csv", "w")
trainingdata = open(f"trainingdata-{id}.csv", "w")
print("created trainig/test data UUID: " + str(id))

def writeToTestData(line):
    testdata.write(line + " \n")
def writeToTrainingData(line):
    trainingdata.write(line + " \n")

# Write Headers
writeToTestData("date,open,high,low,close,volume")
writeToTrainingData("date,open,high,low,close,volume")


# stock to make CSV file of, leave empty if none
findstock = "AAPL"

# remove first line
lines.pop(0)

putLineInTestingData = True
for i in lines:

    # Check if it is the desired stock 
    if i.find(findstock) >= 0:

        # Remove stock name from syntax 
        i = i.rstrip(f',{findstock}')

        # Take evrey other value and sort into seperate document
        if putLineInTestingData == True:
            # Insert line into testing data
            writeToTrainingData(i)
            putLineInTestingData = False
        else:
            writeToTestData(i)
            # Insert line into training data
            putLineInTestingData = True