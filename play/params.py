''' Passing parameters to functions'''

''' from https://www.python-course.eu/passing_arguments.php
If you pass immutable arguments like integers, strings or tuples to a function, the passing acts like call-by-value. 

If we pass a list to a function, we have to consider two cases: 
Elements of a list can be changed in place, i.e. the list will be changed even in the caller's scope. 
If a new list is assigned to the name, the old list will not be affected, 
i.e. the list in the caller's scope will remain untouched.

'''
print ('The first example a new object is created becuase the first use of x is assignemt to x')
def ref_demo(x):
    print ("x=",x," id=",id(x))
    x=42
    print ("x=",x," id=",id(x))

x = 9
print (id(x))
ref_demo(x)
##x= 9  id= 41902552
##x= 42  id= 41903752
id(x)
print (id(x))

print ('The following example gave the same result as the previous one')
def ref_demo_b(x):
    print ("x=",x," id=",id(x))
    b=x
    x+=1
    print ('b=',b)
    print ("x=",x," id=",id(x))

x = 8
print (x, id(x))
x = 9
print (x, id(x))

ref_demo_b(x)
##x= 9  id= 41902552
##x= 42  id= 41903752
id(x)
print (id(x))

print ('\nNo side effects:')
def func1(list):
    print (list, '    List id:',id(list))
    list = [47,11]  #this will create a separate list objcet
    list+= [22,33] #this works just on the local list
    print (list, 'List id:',id(list))

fib = [0,1,1,2,3,5,8]
func1(fib)
#[0, 1, 1, 2, 3, 5, 8]
#[47, 11]
print (fib, 'fib list ID:',id(fib))
#[0, 1, 1, 2, 3, 5, 8]

print ('\nNow with side effect:')
def func2(list):
    print (list, 'inside, before List id:',id(list)) #
    list += [47,11]
    ## or with append
    #list.append(77)
    print (list, 'inside, after List id:',id(list))

fib = [9,1,1,2,3,5,8] #not clear why the id here is same as the local one in the prev func1
print (fib, 'fib list ID before:',id(fib))
func2(fib)
print (fib, 'fib list ID after: ',id(fib)) #no change from before

fib = [10,1,1,2,3,5,8] #no new object created
print ('to avoid side effect one can pass the attributes  fib[:]')
func2(fib[:]) #this will not have a side
print (fib, 'fib list ID:',id(fib))
