def check(*args):
    return args


def mean(*args):
    return sum(args)/len(args)


# Python program to illustrate *args with first extra argument
def check(arg1, *argv):
    print("First argument :", arg1)
    return str("Next argument through *argv : ") + str(argv)


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


def upper_sort(*args):
    upper_list = [word.upper() for word in args]
    return sorted(upper_list)


print(check(1, 2, 3, 'asd'))
print(mean(1, 34, 12, 56, 78, -90, 0.01))
print(check('Hello', 'Welcome', 'to', 'GeeksforGeeks'))
args = ("Romans", "for", "Greeks")
myFun(*args)

kwargs = {"arg1": "Persians", "arg2": "for", "arg3": "Greeks"}
myFun(**kwargs)

print(upper_sort('bamboo', 'for', 'panda', 'hate', 'mango'))
