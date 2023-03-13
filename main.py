import csv
import random

# custom params
importColumn = [5, 8, 9, 10, 11]
importCSVname = "csv-doc.csv"
exportMDname = "export.md"
tail = "번 지원자"

### code ###
columnList = []
dataList = []

# import CSV
with open(importCSVname, 'r') as csvFile:
    rdr = csv.reader(csvFile)
    for line in rdr:
        dataList.append([])
        for columnNum in importColumn:
            dataList[-1].append(line[columnNum])

columnList = dataList[0]
del dataList[0]
random.shuffle(dataList)

# export Markdown
with open(exportMDname, 'w') as markdownFile:
    for i in range(len(dataList)):
        # heading
        markdownFile.write("# " + str(i+1) + tail + "\n")

        # data
        for j in range(len(columnList)):
            markdownFile.write("### " + columnList[j] + "\n")
            markdownFile.write(dataList[i][j] + "\n")
            markdownFile.write("\n")
        
        # separate
        markdownFile.write("\n\n")

# done
print("Done!")