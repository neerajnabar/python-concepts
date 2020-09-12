# closures.py

def outer_func(name):
    message = f"Hi {name}"              # A.K.A "The Free Variable"

    def inner_func():
        print(message)

    return inner_func

greet_adam = outer_func('Adam')         # outer_func gets called and returns here
greet_neeraj = outer_func('Neeraj')     # outer_func gets called and returns here

greet_adam()                            # only inner function runs, but it maintains a record of `name` from outer_func, in this case 'Adam'
greet_neeraj()                          # only inner function runs, but it maintains a record of `name` from outer_func, in this case 'Neeraj'