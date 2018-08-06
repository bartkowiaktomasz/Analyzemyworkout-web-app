"""
Config file.
All other scripts import variables from this config
to their global namespace.
"""
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
IP_ADDRESS = "http://104.40.158.95:5000/"
IP_LOCAL = "http://192.168.1.71:5000"
PAYLOAD_KEY = "payload_json"

# Model
MODEL_PATH = 'models/model.h5'

# Architecture
N_CLASSES = len(LABELS_NAMES)
N_FEATURES = 9  # acc, gyro, magnetometer

# Data preprocessing
TIME_STEP = 5
SEGMENT_TIME_SIZE = 40
