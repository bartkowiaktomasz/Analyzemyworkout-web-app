##################################################
### GLOBAL VARIABLES
##################################################
COLUMN_NAMES = [
    'activity',
    'acc-x-axis',
    'acc-y-axis',
    'acc-z-axis',
    'gyro-x-axis',
    'gyro-y-axis',
    'gyro-z-axis',
    'mag-x-axis',
    'mag-y-axis',
    'mag-z-axis'
]

LABELS_NAMES = [
    'Pushup',
    'Pushup_Incorrect',
    'Squat',
    'Situp',
    'Situp_Incorrect',
    'Jumping',
    'Lunge'
]

# Web app
IP_ADDRESS = "http://35.234.141.115:5000/"

# Model
MODEL_PATH = 'model/model.h5'

# Architecture
N_CLASSES = len(LABELS_NAMES)
N_FEATURES = 3  # acc, gyro, magnetometer

# Data preprocessing
DATA_COLLECTION_TIME = 200
TIME_STEP = 20
SEGMENT_TIME_SIZE = 40
