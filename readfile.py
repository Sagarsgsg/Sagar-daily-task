file =open('sagu.txt', 'r')
content = file.read()
print(content)

file =open('sagu.txt', 'r')
line = file.readline()
print(line)

file =open('sagu.txt', 'r')
lines =file.readlines() #Read in a list#
print(lines)
