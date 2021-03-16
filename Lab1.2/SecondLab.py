# Вторая программа

from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(a):
    return a.value

wb = load_workbook('data_analysis_lab.xlsx')
lict = wb['Data']

years = list(map(getvalue, lict['A'][1:]))
relative_temp = list(map(getvalue, lict['C'][1:]))
activity = list(map(getvalue, lict['D'][1:]))

pyplot.plot(years, relative_temp, label='Относительная температура')
pyplot.plot(years, activity, label= 'Солнечная активность')

pyplot.xlabel('Год')
pyplot.ylabel('Температура/Солнечная активность')
pyplot.legend(loc='best')

pyplot.show()