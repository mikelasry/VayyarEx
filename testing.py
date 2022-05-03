from constants import *
from classes import *
from functions import *

fid = 0
trueFile_name = "logger_true_file.log"
falseFile_name = "logger_false_file.log"

roomFrames = []
outFrames, inFrames = [],[]

# generate all possible frames in room regardless to z axis
X,Y = [],[]
pos = ROOM_AREA['X_START']
while round(pos,1) <= ROOM_AREA['X_END']:
    X.append(round(pos,1))
    pos += 0.1

pos = ROOM_AREA['Y_START']
while round(pos,1) <= ROOM_AREA['Y_END']:
    Y.append(round(pos,1))
    pos += 0.1

for x in X:
    for y in Y:
        roomFrames.append(Frame(fid,x,y,0))
        fid += 1

# for each frame, add to matching list
for frame in roomFrames:
    if frame.isInChairArea():
        inFrames.append(frame)
    else: outFrames.append(frame)

# send lists to function to generate files
trueFile_path = os.path.join(TESTFILES_DIR_PATH, trueFile_name)
falseFile_path = os.path.join(TESTFILES_DIR_PATH, falseFile_name)

createLogFile(trueFile_path, inFrames, force=True)
createLogFile(falseFile_path, outFrames, force=True)

trueScore = testFile(trueFile_path, True)
falseScore = testFile(falseFile_path, False)

trueMsg = "Test 1/2 completed succeessfully" if trueScore == 100 else f"True file test score: {trueScore}"
falseMsg = "Test 2/2 completed succeessfully" if falseScore == 100 else f"False file test score: {trueScore}"

print(trueMsg)
print(falseMsg)
print("Done.")