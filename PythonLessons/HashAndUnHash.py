# Hashable and UnHashable

a=5
b=a #points to a copy of a not the original position in memeory
a=a+1
print b #not incremented

A = []
B = A
A.append(5)
print B #does get a new element

# However

A = [{},{}] # list of dicts
B = [x for x in A]
A[0]["name"] = "bob"
print B[0]["name"]