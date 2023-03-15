import csv
import random


### custom params ###
importCSVname = "csv-doc.csv"
exportMDname = "export.md"

importColumn = [5, 8, 9, 10, 11]
numberForm = "adVirtual %d번 지원자"
### end           ###


### code          ###
columnList = []
dataList = []

# import CSV
with open(importCSVname, 'r') as csvFile:
    rdr = csv.reader(csvFile)
    for line in rdr:
        dataList.append([])
        for columnNum in importColumn:
            dataList[-1].append(line[columnNum])

# post processing
columnList = dataList[0]
del dataList[0]
random.shuffle(dataList)

# export Markdown
with open(exportMDname, 'w') as markdownFile:
    for i in range(len(dataList)):
        # write heading
        markdownFile.write("# "  +  numberForm%(i+1)  +  "\n")

        # write data
        for j in range(len(columnList)):
            markdownFile.write("### " + columnList[j] + "\n")
            markdownFile.write(dataList[i][j] + "\n")
        
        # separate heading
        markdownFile.write("\n\n\n\n\n\n")

# done
print("Done!")