
# OpenCV Video Processing Project

## Overview

This project is a real-time video processing application built using Python and OpenCV. The program captures live video from your computer’s camera and allows the user to apply different image processing effects and filters to the video stream.

The application demonstrates several important computer vision and image processing techniques, including:

* Edge Detection
* Grayscale Quantization
* Contrast Enhancement
* Soft and Polished Appearance Filter
* Cartoon Filter

---

# Features

## 1. Edge Detection

Applies an edge detection algorithm to highlight object boundaries and contours in the video stream.

Possible techniques:

* Canny Edge Detection
* Sobel Operator
* Laplacian Filter

### Purpose

Used for feature extraction, object recognition, and image segmentation.

---

## 2. Grayscale Quantization

Reduces the number of grayscale intensity levels in each frame.

### User Input

The user can define the number of grayscale levels.

### Purpose

Demonstrates image compression concepts and stylized visual effects.

---

## 3. Contrast Enhancement

Enhances frame contrast using histogram equalization.

### Technique Used

* Histogram Equalization applied frame-by-frame.

### Experiment

Change the lighting conditions around your camera and observe how the enhanced video adapts to brightness changes.

### Purpose

Improves visibility in low-contrast environments.

---

## 4. Soft and Polished Appearance

Applies smoothing/blurring filters to reduce noise and soften facial details.

### Possible Filters

* Gaussian Blur
* Bilateral Filter
* Median Blur

### Purpose

Creates a cleaner and more polished visual appearance.

---

## 5. Cartoon Filter

Applies a cartoon-style artistic effect.

### Typical Processing Pipeline

1. Convert frame to grayscale.
2. Apply smoothing.
3. Detect edges.
4. Quantize colors.
5. Combine edges with simplified colors.

### Purpose

Provides a creative and fun image stylization effect.

---

# Technologies Used

* Python 3
* OpenCV (`cv2`)
* NumPy

---

# Installation

## 1. Clone or Download the Project

```bash
git clone <repository-url>
```

Or download the ZIP file and extract it.

---

## 2. Install Required Libraries

Install OpenCV and NumPy:

```bash
pip install opencv-python numpy
```

---

# Running the Program

Run the Python script:

```bash
python OpenCV.py
```

---

# Controls

You can customize this section based on your implementation.

Example:

| Key | Function               |
| --- | ---------------------- |
| 1   | Edge Detection         |
| 2   | Grayscale Quantization |
| 3   | Contrast Enhancement   |
| 4   | Soft Appearance        |
| 5   | Cartoon Filter         |
| Q   | Quit Program           |

---

# Example Workflow

1. Start the application.
2. The webcam feed opens.
3. Press keyboard keys to switch between processing modes.
4. Observe the live processed output.
5. Press `Q` to exit.

---

# Learning Objectives

This project helps practice:

* Real-time image processing
* Video frame manipulation
* OpenCV fundamentals
* Filtering and enhancement techniques
* Computer vision concepts

---

# Troubleshooting

## Error: `ModuleNotFoundError: No module named 'cv2'`

Install OpenCV using:

```bash
pip install opencv-python
```

Or:

```bash
python -m pip install opencv-python
```

---

# Future Improvements

Possible future enhancements:

* Add a graphical user interface (GUI)
* Support video file input
* Add face detection
* Add object tracking
* Save processed videos
* Add more artistic filters

---

# Author

Developed as an OpenCV and Computer Vision practice project.
