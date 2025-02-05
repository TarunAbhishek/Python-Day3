cmp1 = 5 + 3j
cmp2 = 6 - 5j

# print(cmp1 + cmp2)
# print(cmp1 - cmp2)
# print(cmp1 * cmp2)
# print(cmp1 / cmp2)
# print(cmp1 % cmp2) #Not working
# print(cmp1 // cmp2) #Floor Division is not working!!
# print(cmp1 ** cmp2) #Not working

print(2 > 3)
print(2 >= 3)
print(5>=3)

print(type(False))

print(int(True))
print(int(False))

a = 5
b = 8
print(int(a<=b)) #TODO:Try to do more stuff with this!!

#Sequences: List, Tuple, Strings, Range
#List - Collection of heterogenous elements which are indexable and mutable - []

list1=[1,2,3,4,5,6,7,8,[1,5,8,9],[2,4,6,8],"Tarun"]
print(len(list1)-1)
print(list1)

print(list1[0:8])
print(list1[2:])
print(list1[2::2])
print(list1[-1:-8:-1]) #? As this is -ve indexing here, The last -1 defines to go in opposite direction in the indexing!!
print(list1[4:1:-1]) #? As this is +ve indexing here, The last -1 defines to go in backward/opposite direction in the indexing!!
print(list1[9][2]) #? [2,4,6,8] as this is 9th element the [2] in the print statement tells to print the 2nd element which is 0,1,2 i.e., 6!!

#?To change element just by using a statement and not changing by going directly to list1
list1[10]= "Abhishek"
print(list1)

list1[3], list1[4]="I", "am" #?To change multiple elements at once!!
print(list1)

#Tuple- (), Immutable
#?Tuple is faster than list
tup1=(1,2,3,"Hello", "Ekkadunna", "Hello")
print(tup1)
print(tup1[3:1:-1])

#Range

print(range(0,100)) #?Won't work!!
print(list(range(0,100))) #? You should change the range to list or tuple to check the range elements!!
print(list(range(100,0,-1))) #?Here -1 defines opposite direction but if we change it to -2 we start the step here!! 
print(list(range(100,0,-2))) #?Now it makes step and starts 100,98,86.... likewise
print(list(range(0,100,2))) #?Here 2 defines step!!

#TODO: Today's Task: Check about string now, whether it is mutable/immutable!!