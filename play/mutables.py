''' per https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference.
some data types are mutable, but others aren't
So:

If you pass a mutable object into a method,
the method gets a reference to that same object and you can mutate it to your heart's delight,
but if you rebind the reference in the method, the outer scope will know nothing about it, and after you're done,
the outer reference will still point at the original object.

If you pass an immutable object to a method, you still can't rebind the outer reference,
and you can't even mutate the object.
'''

print ('\nShowing that integer is immutable:')
x = 8
print ('x =',x, id(x))
x = 9  #x gets a new object!!
print ('x =',x, id(x))

print ('\nIntegers (immutable) then lists (mutable) examples:')
print ('\n With integer (immutable')
a=5
b=a #b gets the reference of a
print ('ids and values: ',id(a), a, id(b), b) #same same
b=77 # b gets a new object!!
print ('afte assignment to b:')
print ('ids and values: ',id(a), a, id(b), b) #b has differenet object and value
print ('the above shows that assignment to the immutable integer variable triggered creating a new object for b')

print ('\n Now with lists (mutable)')
a=[5,6]
b=a #b gets the reference of a
print ('ids and values: ',id(a), a, id(b), b)
b.append(2) #the content of the reference has chanegd, no new object for b!
print ('afte appending 2 to to b:')
print ('ids and values: ',id(a), a, id(b), b) ##same same!
print ('the above shows that changing the list DID NOT trigger creating a new object for b')
