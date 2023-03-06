
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])#cherry
print(thislist[-2])#banana
print(thislist[-3])#apple
print(thislist[-4])#IndexError: list index out of range
print(thislist[0])#apple


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#['cherry', 'orange', 'kiwi']
print(thislist[:4])#['apple', 'banana', 'cherry', 'orange']
print(thislist[2:])#['cherry', 'orange', 'kiwi', 'melon', 'mango']


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])#['orange', 'kiwi', 'melon']


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)#['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)#['apple', 'banana', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)#['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
print(thislist + tropical )#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop()#pop last item
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)#['banana', 'cherry']


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]  


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)#['apple', 'banana', 'mango']


newlist = [x for x in range(10)]
newlist#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x for x in range(10)]
newlist = [x if x %2 == 0 else "orange" for x in newlist if x > 5]
print(newlist)#[6, 'orange', 8, 'orange']




thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)#['banana', 'kiwi', 'mango', 'orange', 'pineapple']
thislist.sort(reverse=True)
print(thislist)#['pineapple', 'orange', 'mango', 'kiwi', 'banana']

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)






