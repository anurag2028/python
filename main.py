entry = int(input("please insert integer only "))
table = [2,2,2,2,4,4,4,4,5,5,5,5,5,6,6,6,610,1,0.1,101,0,1,1,0,0,1]
new = []
for i in table:
    if i == entry:
        new.append(i)

print(new)
print(len(new))
x = (len(new))
length = []
length.append(x)
print(type(new[0]))
print(length)
h = length + table[0:10:2]
print(h)