mydict = {
    'name': 'udin',
    'race': 'dwarf',
    'class': 'fighter',
    'age': 129    
}

print(mydict.get('name'))

print(mydict.items())

print(mydict.values())

print(mydict.keys())

mydict.update(age=mydict['age']+1)
print(mydict)

mydict.update(status='online')

print(mydict)

mydict.pop('status')

print(mydict)
mydict.popitem()
print(mydict)
print(mydict.setdefault('age',0))
print(mydict)

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x,1)

print(thisdict)

thisdict.clear()
print(thisdict)

print('name' in mydict)
print('nama' not in mydict)


