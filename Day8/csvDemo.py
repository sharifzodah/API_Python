import csv

with open('D:\\QA COURSE\\API_Testing_Python\\BackEndAutomation\\utils\\loanApp.csv') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    # print(reader)
    # print(list(reader))
    names = []
    stats = []
    for row in reader:
        names.append(row[0])
        stats.append(row[1])

print(names)
print(stats)
index = names.index('Fatima')
loanStatus = stats[index]
print('loan status = ' + loanStatus)

with open('D:\\QA COURSE\\API_Testing_Python\\BackEndAutomation\\utils\\loanApp.csv', 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow(['Bob', 'Rejected'])
