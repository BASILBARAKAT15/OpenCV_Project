
# Online Python - IDE, Editor, Compiler, Interpreter

import cv2
import numpy as np


def edge_detection(frame):
    return cv2.Canny(frame, 100, 200)

def grayscale_quantization(frame, levels=4):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    step = 256 // levels
    quantized = (gray // step) * step
    return cv2.cvtColor(quantized, cv2.COLOR_GRAY2BGR)

def contrast_enhancement(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    return cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)

def soft_polished(frame):
    return cv2.GaussianBlur(frame, (15, 15), 0)

def cartoon_filter(frame):
    # Step 1: Apply bilateral filter to reduce color palette
    color = cv2.bilateralFilter(frame, 9, 75, 75)
    
    # Step 2: Convert to grayscale and detect edges
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(blurred, 255, 
                                   cv2.ADAPTIVE_THRESH_MEAN_C, 
                                   cv2.THRESH_BINARY, 9, 9)
    
    # Step 3: Combine color and edges
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

# Main program
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Press keys 1–5 to select a mode:")
print("1: Edge Detection")
print("2: Grayscale Quantization")
print("3: Contrast Enhancement")
print("4: Soft and Polished Appearance")
print("5: Cartoon Filter")
print("Press 'E' to quit.")

mode = 0
levels = 4  # Default quantization level

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply selected mode
    if mode == 1:
        output = edge_detection(frame)
        output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)
    elif mode == 2:
        output = grayscale_quantization(frame, levels)
    elif mode == 3:
        output = contrast_enhancement(frame)
    elif mode == 4:
        output = soft_polished(frame)
    elif mode == 5:
        output = cartoon_filter(frame)
    else:
        output = frame

    cv2.imshow('Video Filter', output)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('e') or key ==  ord('E'):
        break
    elif key in [ord(str(i)) for i in range(6)]:
        mode = int(chr(key))
        if mode == 2:
            try:
                levels = int(input("Enter number of grayscale levels (e.g., 4, 8, 16): "))
            except:
                print("Invalid input, using default 4 levels.")
                levels = 4

cap.release()
cv2.destroyAllWindows()
