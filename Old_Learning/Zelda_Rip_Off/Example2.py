

index = ['leftWall', 'rightWall',
              'downWall', 'upWall']
                   #'upLeftWall', 'upRightWall',
                   #'downLeftWall','downRightWall']
                   
mapIndex = {'leftWall': 'leftEdge', 'rightWall': 'rightEdge',
                 'downWall': 'downEdge', 'upWall': 'upEdge'}
for i in index:                 
    print(mapIndex[i])