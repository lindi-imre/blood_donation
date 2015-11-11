__author__ = 'Péter'

uniqeid = ['654321BA']
raw = open("Data/donors.csv", "r", encoding='utf-8')
lines = raw.read()
raw.close()
out = open("Data/donors.csv", "w", encoding='utf-8')
for line in lines.splitlines():
    found = False
    for c in uniqeid:
        if line.find(str(c)) > -1:
            found = True
            break
    if found:
        continue
    out.write(line+"\n")
out.close()