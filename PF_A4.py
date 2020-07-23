import csv

def show(title, fileName, f):
    print('--- '+title+' ---')
    with open(fileName, 'r') as file:
        data = csv.DictReader(file)
        newData = f(data)
        try:
            iterator = iter(newData)
        except TypeError:
            print(newData)
        else:
            for row in newData:
                print(row)

getTeam = lambda team: lambda data: \
    filter(lambda e: e['Clube 1']==team or e['Clube 2']==team, data)

def getYear(match):
    dateStr = match['Data']
    yearStr = dateStr[:4]
    return int(yearStr)

def addYearField(match):
    newMatch = dict(match)
    newMatch['Ano'] = getYear(match)
    return newMatch

def addYear(data):
    return map(addYearField, data)



show('getTeam', 'Brasileirao.csv', getTeam('Atl\xc3\xa9tico-MG'))