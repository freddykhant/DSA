from fileinput import filename
import DSAsorts

id = []

def processLine(row):

    tokens = row.split(",")
    try:
        id.append(int(tokens[0]))
    except:
        raise TypeError("CSV row had invalid format")


def readFile(filename):
    try:
        file = open(filename)
        lineNum = 0
        line = file.readline()

        while line:
            lineNum += lineNum
            processLine(line)
            line = file.readline()

        file.close()
    
    except IOError as e:
        print("Error in file processing: " + str(e))

def writeCSV(filename, array):
    try:
        file = open(filename, 'w')
        for line in array:
            file.write(str(line))
            file.write('\n')
    except IOError as e:
        print("Error in file processing: " + str(e))

readFile('RandomNames7000.csv')
DSAsorts.insertionSort(id)
writeCSV('SortedIDS.csv', id)