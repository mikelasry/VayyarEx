import os

TESTFILES_REL = os.path.join(".","testFiles")
TESTFILES_DIR_PATH = os.path.abspath(TESTFILES_REL)

REL_PATH = os.path.join(".","tracker_log.log")
LOGFILE_PATH = os.path.abspath(REL_PATH)

READ_MODE = 'r'
WRITE_MODE = 'w'

COLON = ':'
SPACE = ' '
EQUALS = "="
EMPTY = ""
SEP = "*"*100
ERR_CODE = -1000.0
ERROR_MSG = "Somthing went wrong!"

FRAME_ID_PREFIX = 'Process frame without interrupt'
EOF = 'endOfFrame'
TARGETS = 'Targets'
T_ID = 't_id'
FPS_RATE = 10
FRAME_DURATION = 0.1

TID_IX = 0
X_IX = 1
Y_IX = 2
Z_IX = 3

ROOM_AREA = {
    'X_START': -1.0,
    'X_END': 2.0,
    'Y_START': 0.0,
    'Y_END': 3.5
}

CHAIR_POS = {
    'X_START': -0.5,
    'X_END': 0.0,
    'Y_START': 1.8,
    'Y_END': 2.4
}