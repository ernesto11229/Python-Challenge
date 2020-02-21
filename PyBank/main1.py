import csv
import os

#bank_cvs=os.path.join('C:/Users/ernes/Desktop/the class/python-challenge/pybank/budget_data.csv')

months=[]
PnL=[]

#with open(bank_cvs, 'r') as csvfile:
with open("budget_data.csv", 'r') as csvfile:
    csvread=csv.reader(csvfile)
    next(csvread,None)

    for row in csvread:
        months.append(row[0])
        PnL.append(int(row[1]))

TotalMonths=len(months)

Gincrease=PnL[0]
Gdecrease=PnL[0]
TotalR=0

for R in range(len(PnL)):
    if PnL[R] >= Gincrease:
        Gincrease = PnL[R]
        Gmonth = months[R]
    elif PnL[R] <= Gdecrease:
        Gdecrease = PnL[R]
        LoMonth = months[R]
    TotalR += PnL[R]


AverageChange=round(TotalR/TotalMonths,2)

output=os.path.join('C:/Users/ernes/Desktop/the class/python-challenge/pybank/Analysis.txt')

with open(output,'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('--------------------'+'\n')
    writefile.writelines('Total Months:' + str(TotalMonths)+'\n')
    writefile.writelines('Total Revenue: $' + str(TotalR) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(AverageChange) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + Gmonth + ' ($' + str(Gincrease) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + LoMonth + ' ($' + str(Gdecrease) + ')')

with open(output,'r') as readfile:
    print(readfile.read())
