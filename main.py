'''rakeshsir = [
    {
        'A':30, 'B' : 50, 'C' : 70
    },
    {
        'A':40, 'B' : 30, 'C' : 60
    },
    {
        'A':60, 'B' : 70, 'C' : 80
    },
    {
        'A':70, 'B' : 40, 'C' : 40
    }
]
listofBmarks = []
for i in rakeshsir:
    listofBmarks.append(i['B'])
maxmark = max(listofBmarks)
print(maxmark)

for one in rakeshsir:
    b_mark = one['B']
    if b_mark == maxmark:
        print(one)

maxRakesh = max(rakeshsir, key=lambda x: x['B'])
print(maxRakesh)

sortedRakesh = sorted(rakeshsir, key = lambda x : x['C'])
print(sortedRakesh)'''
        
