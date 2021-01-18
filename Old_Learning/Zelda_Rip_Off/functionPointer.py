
def myfunction():
    print('this is my function\n')
    
def myfuncTwo():
    print('This one does some stuff\n')
funcdict = {
  'myfunction': myfunction, \
   'myfuncTwo': myfuncTwo   \
}


for myvar in funcdict:
    funcdict[myvar]()

print('Syntax correct\n')