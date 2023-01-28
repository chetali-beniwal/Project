def printTable(tableData):
    colWidths=[]
    for i in tableData:
        max=len(i[0])
        for a in i:                  
            if max<len(a):
                max=len(a)
        colWidths.append(max)
    max1=colWidths[0]
    for a in colWidths:
        if a>max1:
            max1=a
    for b in range(l2):
        for c in range(l1):
            print(tableData[c][b].rjust(max1),end=' ')
        print()
    
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
l1=len(tableData)
l2=len(tableData[0])
printTable(tableData)
