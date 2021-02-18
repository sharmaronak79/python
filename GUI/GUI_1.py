from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def func(x):
    return x

# True or False for check box
interact (func,x=True)

# integervalue for slider
interact (func,x=10)

# for box we use any string to pass any string
interact (func,x='Ronak')

# we can use two parameter to fix using decorator
# return tuple

@interact(x=True,y=fixed(1.0))
def g(x,y):
    return (x,y)

interact (func,x=widgets.IntSlider(min=-100,max=100,step=1,value=0))

# we can do same thing using brevation
interact(func,x=(-10,10,1))

# for drop  down menu we use list methid also 
interact(func,x=['option1', 'option2', 'option3'])

# for key and value pair we can use dictionary as well
interact(func,x={'one':1,'Two':2,'Three':3})

# we can pass function also for particular output
def r():
    return 'ronak'
interact(func,x={'one':1,'Two':r(),'Three':3})





# for two input using slider
from IPython.display import display

def f(a,b):
    display(a+b)
    return a+b

w = interactive(f,a=10,b=20)

type(w)

w.children

display(w)

