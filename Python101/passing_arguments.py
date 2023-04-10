import sys
from enum import Enum




animals = ['dog', 'cat', 'lion', 'tiger']
for a in animals:
    print(a, len(a))
    
userDataSet = {'Surya' : 'Resident', 'Swathi' : 'Citizen', 'Stavya' : 'Citizen', 'Sthita' : 'Citizen'}
for user, citizenShipStatus in userDataSet.items():
    if citizenShipStatus == 'Citizen':
        print('User: ', user, 'Citizen')
    else:
        print('User: ', user, 'Resident')
        
class Color(Enum):
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    
color = Color( input("Enter color choice:").lower())

match color:
    case Color.RED:
        print('Red it is')
    case Color.BLUE:
        print('Blue it is')
    case Color.GREEN:
        print('Green it is')  
    case _:
        print('Color blind')      