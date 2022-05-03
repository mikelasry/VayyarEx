from classes import Frame
from constants import *

def castValue(kv_pair): # x=-0.4
    """ Splits the param <kv_pair> by equals sign ('=') then casts the string into a number considering it's sign\n    
    Args: 
        kv_pair: (str) key-value pair to represent the value to be cast from string to float

    Returns: (float) | ERR_CODE = -1000.0
        A float value represented by the string <kv_pair> param
    """
    value = None
    parts = kv_pair.split(EQUALS)
    if not parts or len(parts) < 2: return ERR_CODE 
    else: value = parts[1] 
    sign = -1 if value[0] == '-' else 1
    return float(value[1:])*sign 

def parseFrame(fid, infoLine):
    """ Parse the given string and generate a Frame object\n
    Args:
        fid: (int) frame id
        infoLine: (str) string of shape t_id=t1 x=x1 y=y1 z=z1
    
    Return: (Frame)
        A new Frame object contains the parsed coordinates from the <infoLine> param
        and the frame id from the <fid> param
    """
    data = infoLine.split(SPACE)
    if not data or len(data) < 4:
        print("ERROR trying to parse information, not enough details")
        return ERR_CODE

    x = castValue(data[X_IX])
    y = castValue(data[Y_IX])
    z = castValue(data[Z_IX])
    
    if ERR_CODE in [x,y,z]:
        print(f"ERROR trying to parse coordinate: {infoLine}")
        return ERR_CODE
        
    return Frame(fid,x,y,z)


def isFrameStandsAlone(frame_a, frame_b, frame_c, standsin=True):
    ''' Given a partial series of 3 frames, check whether the middle frame stand alone,
        meaning frame a and c are outside of the area, whereas frame b is inside.\n
    Args:
        frame_a: first frame of the sub-series
        frame_b: second frame of the sub-series
        frame_c: third frame of the sub-series

    Return: (bolean)
        Indicator whether frame_b is inside the area' whereas frame_a and frame_c are outside of it
    '''
    cond_a = frame_a.isInChairArea()
    cond_b = frame_b.isInChairArea()
    cond_c = frame_c.isInChairArea()
    
    standsAlone_inside = (not cond_a) and cond_b and (not cond_c)
    standsAlone_outside = cond_a and (not cond_b) and cond_c

    return standsAlone_inside if standsin else standsAlone_outside

def createLogFile(path, frames, force=False):
    ''' Generates log file
    Args:
        path: (str) the path to the file to be created
        frames: (list<Frame>) list of frames to be written to the file
        force: (boolean) indicator whether to override the file in the specified path, if exists. default=False

    Return: (None) Generate the file in the path specified in the <path> param
    '''
    if not os.path.isdir(TESTFILES_DIR_PATH):
        os.mkdir(TESTFILES_DIR_PATH)

    if os.path.exists(path):
        if force: os.remove(path)    
        else: return ERR_CODE

    with open(path, WRITE_MODE) as f:
        for frame in frames:
            f.write(frame.getInfo())

def testFile(path, expected):
    ''' Tests the reliability of the 'isInChairArea' function, 
        using the log file specified at <path>, 
        and the expected output specified at the <expected> param
    
    Args:
        path: (str) specifies the path to the log file to be checked
        expected: (boolean) an indicator of the expected output

    Return: (float) score - number representing the accuracy ratio
    '''
    fid = 0
    count = 0
    falseAlerts = []

    with open(path, READ_MODE) as f:
        for line in f:
            if line.startswith(FRAME_ID_PREFIX):
                fid = int(line.split(COLON)[1])

            if line.startswith(T_ID):
                frame = parseFrame(fid, line)
                inArea = frame.isInChairArea()
                if inArea != expected:
                    falseAlerts.append(frame)
                    print(f"Problom with frame {frame.id}: Expectes {expected}, but got {inArea}")
                count += 1
                fid += 1
        
    score = (1 - len(falseAlerts)/count)*100
    return score