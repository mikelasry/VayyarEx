from pickle import EMPTY_DICT
from constants import *

class Frame:
    id  = None
    x = None
    y = None
    z = None

    def __init__(self, _fid, _x, _y, _z):
        ''' Generates a Frame object\n
        Args: 
            _fid: (int) frame identifier
            _x: (float) the x value of the snapshot coordinate
            _y: (float) the y value of the snapshot coordinate
            _z: (float) the z value of the snapshot coordinate
        '''
        self.id = _fid
        self.x = _x
        self.y = _y
        self.z = _z
    
    def isInChairArea(self):
        ''' Check whether the frame is inside the desired section\n
        
        Return: (boolean) 
            Indicatior if the frame is in the area
        '''
        if (self.x < CHAIR_POS['X_START']) or (self.x > CHAIR_POS['X_END']): return False
        if (self.y < CHAIR_POS['Y_START']) or (self.y > CHAIR_POS['Y_END']): return False
        return True

    def isOnEdge(self):
        ''' Check if a Frame is on the edge of the closed section\n
        Return: (boolean) Indication whether the snapshot coordinate is on the edge of the section
        '''
        xMatch = (self.x == CHAIR_POS['X_START']) or (self.x == CHAIR_POS['X_END'])
        yMatch = (self.y == CHAIR_POS['Y_START']) or (self.y == CHAIR_POS['Y_END'])

        xRange = (self.x >= CHAIR_POS['X_START']) and (self.x <= CHAIR_POS['X_END'])
        yRange = (self.y >= CHAIR_POS['Y_START']) and (self.y <= CHAIR_POS['Y_END'])
        
        onHorizontalEdges = yMatch and xRange
        onVerticalEdges =  xMatch and yRange

        return onHorizontalEdges or onVerticalEdges

    def getInfo(self):
        ''' Return: (str) generates a string representing the frame '''
        
        fidLine = f"{FRAME_ID_PREFIX}: {self.id}"
        infoLine = f"{T_ID}=0 x={'+' if self.x >= 0 else ''}{self.x} y={'+' if self.y >= 0 else ''}{self.y} z={'+' if self.z >= 0 else ''}{self.z}"
        return f"{fidLine}\n{infoLine}\n{EOF}\n\n"

    def show(self, prefix=EMPTY):
        ''' Displays the information of the frame to the standard output \n
        
        Args: 
            prefix: (str) a string prefix that could be injected in front of the Frame's displayed data
        
        Return: (None)
        '''
        print(f"{prefix} [fid:{self.id}] {self.getInfo()}")