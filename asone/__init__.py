from .asone import ASOne
import asone.detectors
import asone.trackers
import asone.recognizers
import asone.segmentors
from .pose_estimator import PoseEstimator

BYTETRACK = 0
DEEPSORT = 1
NORFAIR = 2
MOTPY = 3
OCSORT = 4
STRONGSORT = 5


YOLOV5X6_PYTORCH = 0
YOLOV5S_PYTORCH = 2
YOLOV5N_PYTORCH = 4
YOLOV5M_PYTORCH = 6
YOLOV5L_PYTORCH = 8
YOLOV5X_PYTORCH = 10
YOLOV5N6_PYTORCH = 12
YOLOV5S6_PYTORCH = 14
YOLOV5M6_PYTORCH = 16
YOLOV5L6_PYTORCH = 18


YOLOV6N_PYTORCH = 20
YOLOV6T_PYTORCH = 22
YOLOV6S_PYTORCH = 24
YOLOV6M_PYTORCH = 26
YOLOV6L_PYTORCH = 28 
YOLOV6L_RELU_PYTORCH = 30
YOLOV6S_REPOPT_PYTORCH = 32

YOLOV7_TINY_PYTORCH = 34
YOLOV7_PYTORCH = 36
YOLOV7_X_PYTORCH = 38
YOLOV7_W6_PYTORCH = 40
YOLOV7_E6_PYTORCH = 42
YOLOV7_D6_PYTORCH = 44
YOLOV7_E6E_PYTORCH = 46

YOLOR_CSP_X_PYTORCH = 48
YOLOR_CSP_X_STAR_PYTORCH = 50 
YOLOR_CSP_STAR_PYTORCH = 52
YOLOR_CSP_PYTORCH = 54
YOLOR_P6_PYTORCH = 56




YOLOX_L_PYTORCH = 58
YOLOX_NANO_PYTORCH = 60 
YOLOX_TINY_PYTORCH = 62
YOLOX_DARKNET_PYTORCH = 64 
YOLOX_S_PYTORCH = 66
YOLOX_M_PYTORCH = 68
YOLOX_X_PYTORCH = 70

#ONNX

YOLOV5X6_ONNX = 1
YOLOV5S_ONNX = 3
YOLOV5N_ONNX = 5
YOLOV5M_ONNX = 7
YOLOV5L_ONNX = 9
YOLOV5X_ONNX = 11
YOLOV5N6_ONNX = 13
YOLOV5S6_ONNX = 15
YOLOV5M6_ONNX = 17
YOLOV5L6_ONNX = 19


YOLOV6N_ONNX = 21
YOLOV6T_ONNX = 23
YOLOV6S_ONNX = 25
YOLOV6M_ONNX = 27
YOLOV6L_ONNX = 29 
YOLOV6L_RELU_ONNX = 31
YOLOV6S_REPOPT_ONNX = 33

YOLOV7_TINY_ONNX = 35
YOLOV7_ONNX = 37
YOLOV7_X_ONNX = 39
YOLOV7_W6_ONNX = 41
YOLOV7_E6_ONNX = 43
YOLOV7_D6_ONNX = 45
YOLOV7_E6E_ONNX = 47

YOLOR_CSP_X_ONNX = 49
YOLOR_CSP_X_STAR_ONNX = 51
YOLOR_CSP_STAR_ONNX = 53
YOLOR_CSP_ONNX = 55
YOLOR_P6_ONNX = 57


YOLOX_L_ONNX = 59
YOLOX_NANO_ONNX = 61 
YOLOX_TINY_ONNX = 63
YOLOX_DARKNET_ONNX = 65 
YOLOX_S_ONNX = 67
YOLOX_M_ONNX = 69
YOLOX_X_ONNX = 71

# YOLOv8
YOLOV8N_PYTORCH = 72
YOLOV8N_ONNX = 73
YOLOV8S_PYTORCH = 74
YOLOV8S_ONNX = 75
YOLOV8M_PYTORCH = 76
YOLOV8M_ONNX = 77
YOLOV8L_PYTORCH = 78
YOLOV8L_ONNX = 79
YOLOV8X_PYTORCH = 80
YOLOV8X_ONNX = 81

# coreml

YOLOV5N_MLMODEL = 120
YOLOV5S_MLMODEL = 121
YOLOV5X6_MLMODEL = 122
YOLOV5M_MLMODEL = 123
YOLOV5L_MLMODEL = 124
YOLOV5X_MLMODEL = 125
YOLOV5N6_MLMODEL = 126
YOLOV5S6_MLMODEL = 127
YOLOV5M6_MLMODEL = 128
YOLOV5L6_MLMODEL = 129
    

YOLOV7_TINY_MLMODEL = 130
YOLOV7_MLMODEL = 131
YOLOV7_X_MLMODEL = 132
YOLOV7_W6_MLMODEL = 133
YOLOV7_E6_MLMODEL = 134
YOLOV7_D6_MLMODEL = 135
YOLOV7_E6E_MLMODEL = 136

YOLOV8N_MLMODEL = 139
YOLOV8S_MLMODEL = 140
YOLOV8M_MLMODEL = 141
YOLOV8L_MLMODEL = 142
YOLOV8X_MLMODEL = 143

YOLOV8N_POSE = 144
YOLOV8S_POSE = 145
YOLOV8M_POSE = 146
YOLOV8L_POSE = 147
YOLOV8X_POSE = 148

YOLOV7_W6_POSE = 149

YOLONAS_S_PYTORCH = 160
YOLONAS_M_PYTORCH = 161
YOLONAS_L_PYTORCH = 162

# YOLOv9
YOLOV9_C_CONVERTED = 164
YOLOV9_E_CONVERTED = 165
YOLOV9_C = 166
YOLOV9_E = 167
GELAN_C = 168
GELAN_E = 169

# Segmentors
SAM = 171

# Text Detectors
# easyocr
CRAFT = 82
DBNET18 = 83

# Text Recognizers
EASYOCR = 200



__all__ = ['ASOne', 'detectors', 'trackers', 'recognizers', 'segmentors', 'PoseEstimator'] 
