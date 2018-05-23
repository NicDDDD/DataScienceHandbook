#Complex Data Types

my_list = [1,2,3]
#list elements can be anything!

mixed_list = ["A",5.7,3,my_list]

#list comprehension

original_list = [1,2,3,4,5,6,7,8]
squares = [x*x for x in original_list]

#selection of lists

first3 = squares[0:2]

#strings and lists
letters = "ABC DEF"
#gives [ABC, DEF]
split1 = letters.split()

#gives 'ABCD'
joined = "".join(["A","B","C","D"])

start,end,count = 1,5,2
numbers = [1,2,3,4,5,6,7,8,9]
NewNumbers = numbers[start:end:count]


#Tuples

my_tuple = (1,2,"bullShit")
print my_tuple[0]

zerothEl,firstEl,thirdEl = my_tuple

#Dictionaries

dict1 = {"January":1,"February":5}
print dict1["January"]
dict1["March"] = 4 #add new element
dict1["January"] = "new shit" # over write element

#dictionary out of tuples
pairs = [("one",1),("two",2)]
as_dict = dict(pairs)

#Sets

s = set()
s.add(1)
s.add("a string?")
s.add(3)












