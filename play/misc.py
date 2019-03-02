
print ('keargs')

def my_kwargs(param, **kwargs):
    print (param)
    for key in kwargs:
        print("{} : {}".format(key, kwargs[key]))

my_kwargs("Hello")
my_kwargs("Hello", a=1, b=2)
