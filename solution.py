from functions import *
from constants import *

def calcDuration():
    framesCount = 0
    inAreaDuration = 0.0 # seconds
    try:
        with open(LOGFILE_PATH, READ_MODE) as f:
            for line in f:

                # handle new frame
                if line.startswith(FRAME_ID_PREFIX):
                    fid = -1
                    parts = line.split(COLON)
                    if len(parts) > 1: fid = int(parts[1])
                    else: print("Error trying to parse frame id")

                # skip empty frames
                if line.startswith(TARGETS):
                    parts = line.split(COLON)
                    if (len(parts) < 2) or (parts[1]) == 0:
                        continue

                # extract information
                if line.startswith(T_ID):
                    frame = parseFrame(fid,line)
                    framesCount += 0 if frame == ERR_CODE else 1

                    if frame.isInChairArea():
                        inAreaDuration += FRAME_DURATION

                # handle end of frame
                if line.startswith(EOF):
                    pass
                
        return (framesCount,inAreaDuration)
    except Exception as e: 
        print(ERROR_MSG)
        print(e, e.args)
        return ERR_CODE, ERR_CODE
    

(totalFrames,totalDuration) = calcDuration()
if totalFrames == ERR_CODE  or totalDuration is None:
    exit(0)
relFrames = totalDuration*10

print(f"Total frames: {totalFrames}")
print(f"Relevant frames: {round(relFrames)} ({round(relFrames/totalFrames*100)}%)")
print(f"Total duration inside closed section is:\n\t{round(totalDuration,1)} seconds")


