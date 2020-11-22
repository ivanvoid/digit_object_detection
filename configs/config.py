# HW2/configs/config.py
from yacs.config import CfgNode as CN


_C = CN()

_C.SYSTEM = CN()
# Number of workers for doing things
_C.SYSTEM.NUM_WORKERS = 4



_C.TRAIN = CN()
# Batch size for training
_C.TRAIN.BATCH_SIZE = 64
# PATH to save/load model for this try
_C.TRAIN.MODEL_PATH = './models/model'
# Use resized images for training?
_C.TRAIN.RESIZE_MODE = False
# Size for image resize transformation, if RESIZE_MODE==True
_C.TRAIN.RESIZE_SIZE = (64,64)
# TRAIN EPOCHS
_C.TRAIN.EPOCHS = 10


_C.MODEL = CN()
# Number of classes for the new head of the model
_C.MODEL.N_CLASSES = 10
# Use transfer learning
_C.MODEL.TRANSFER = False

def get_cfg_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  # Return a clone so that the defaults will not be altered
  # This is for the "local variable" use pattern
  return _C.clone()

# Alternatively, provide a way to import the defaults as
# a global singleton:
cfg = _C  # users can `from config import cfg`