# Basic stuff

print("Hello World!")

# Basic data types

thisIsStr = "RAWR"
thisIsNumber = 123
thisIsFloat = 1.2
thisIsBool = True
thisIsDict = { "foo": "bar" }

print(thisIsDict['foo'])

# list, tuple, set, fronzenset

thisIsList = [1,'List',True]
thisIsTuple  = (1,'Tuple',True)

# Difference

print(thisIsList) # mutable
print(thisIsTuple) # immutable

# thisIsTuple[0] = 2 <-- ERROR!
thisIsList[0] = 2
print(thisIsList)

thisIsSet = {"apple","mango","set"}
thisIsFrozenSet = frozenset(thisIsSet)

# diiference

thisIsSet.add("cherry")
# thisIsFrozenSet.add("cherry") <-- ERROR! 

print(thisIsSet)
print(thisIsFrozenSet)


