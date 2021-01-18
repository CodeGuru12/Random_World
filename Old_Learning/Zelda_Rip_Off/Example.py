

class Example():
    def __init__(self):
        self.index = ['leftWall', 'rightWall',
                      'downWall', 'upWall']
                      
        self.wallCollision = {'leftWall': self.hitLeftWall, 
                          'rightWall': self.hitRightWall,
                          'upWall': self.hitUpWall,
                          'downWall': self.hitDownWall}                      
                       
                       
    def hitLeftWall(self):
        print("Hit Left wall check")
    def hitRightWall(self):
        print("Hit Right wall check")
            
    def hitUpWall(self):
        print("Hit Up wall check")
    
    def hitDownWall(self):
        print("Hit Down wall check")
    
    def Check(self):
        for index in self.index:
            fun = self.wallCollision[index]
            fun()
            #fun()


Ex = Example()
print("Success\n")
#Ex.Check()

a = Example()
a.wallCollision['leftWall']
a.Check()
#keyboardInput = Input()
#keystates =keyboardInput.update()
#a.handleInput(keystates)
