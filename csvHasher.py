import csv
import hashlib

def csvExtractor(fileName):
    csvList = []
    rowCounter = 0
    with open(fileName, 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader, None)
        for row in reader:
            rowCounter += 1
            if rowCounter %2 != 0:
                csvList.append(row[2])
        csvFile.close()
    return csvList

def stringCombiner(strList):
    unifiedString = ''
    for element in strList:
        unifiedString += str(element)
    return unifiedString

def md5Hasher(inputString): return hashlib.md5(inputString.encode())

# csvList = csvExtractor('testcase.csv') # 443DEC3062D0286986E21DC0631734C9
csvList = csvExtractor('annual-enterprise-survey-2020-financial-year-provisional-csv.csv') # 4DD595E104B509F219A56D3E52F409AC
unHashedString = stringCombiner(csvList)
hashedString = md5Hasher(unHashedString).hexdigest().upper()
print(hashedString)
