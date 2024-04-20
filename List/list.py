marks = [95, 98, 100]
print(marks[0:2])   
print(marks[-3])

for i in marks:
    print(i)

marks.append(99)
marks.insert(0, 99)      #(index , element to be inserted)
print(marks)
print(99 in marks)   # Returns bool whether the element is present in the list or not
print(len(marks))


i = 0
while i< len(marks):
    print(marks[i])
    i=i+1

marks.clear()
print(marks)
