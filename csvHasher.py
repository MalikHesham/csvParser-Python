import csv
import hashlib

csvList = []

def csvExtractor(fileName):
    rowCounter = 0
    with open(fileName, 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader, None)
        for row in reader:
            rowCounter += 1
            if rowCounter %2 != 0:
                csvList.append(row[2])
        csvFile.close()
# csvExtractor('testcase.csv') => 443dec3062d0286986e21dc0631734c9
csvExtractor('annual-enterprise-survey-2020-financial-year-provisional-csv.csv') # 4DD595E104B509F219A56D3E52F409AC

def stringCombiner(strList):
    unifiedString = ''
    for element in csvList:
        unifiedString += str(element)
    return unifiedString

def md5Hasher(inputString): return hashlib.md5(inputString.encode())

unHashedString = stringCombiner(csvList)
hashedString = md5Hasher(unHashedString).hexdigest().upper()
print(hashedString)
