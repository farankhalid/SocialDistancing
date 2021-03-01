# base path to YOLO directory
MODEL_PATH = "yolov4"
# initialize minimum probability to filter weak detections along with
# the threshold when applying non-maxima suppression
MIN_CONF = 0.4
NMS_THRESH = 0.5
# boolean indicating if NVIDIA CUDA GPU should be used
USE_GPU = False
# define the minimum safe distance (in pixels) that two people can be
# from each other
MIN_DISTANCE = 50
