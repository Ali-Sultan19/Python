list = [i for i in range(10)]
print(list)

#using append
print('Append Method')
list.append(11)
print(list)
list.append(12)
print(list)


#using insert
print('Insert Method')
list.insert(14,13)
print(list)
list.insert(15,20)
print(list)


#using iterable
print('Iterable')
lst=[1,2,3,4,5,6]
lst1=[7,8,9,0]
k=lst + lst1
print(k)
lst.extend(lst1)
print(lst)

#using remove
print('Remove')
lst.remove(1)
print(lst)
lst.remove(0)
print(lst)

#using pop
print('Pop')
lst.pop(4)
print(lst)
lst.pop(1)
print(lst)

#using clear
print("clear")
lst.clear()
print(lst)


#using sort
print('sort')
a = [0,9,8,7,6,5,4,3,2,1]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
b = [1,2,3,4,5,6,7,8,9,0]
b.reverse()
print(b)


#using index
print('index')
c = [0,2,3,4,1,6,9,7,8]
print(c.index(8))
print(c.index(1))

#using count
print('count')
d = [1,2,3,4,1,2,3,4,5,6,7,2,3,1,3,4,1,2,3,4,5,1,2,1,1]
print(d.count(1))
print(d.count(2))
print(d.count(3))
print(d.count(4))

#using copy
print('copy')
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)