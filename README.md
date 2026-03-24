# 🚀 Drone Object Detection System

## 📌 Overview

This project implements a **real-time drone surveillance system** using **YOLOv8, OpenCV, and DeepSORT**.
It detects, tracks, and analyzes objects from a live camera feed, simulating functionalities used in defense-grade UAV systems.

---

## ✨ Key Features

* 🎯 Real-time Object Detection (YOLOv8)
* 🔄 Multi-Object Tracking (DeepSORT)
* 🎯 Target Locking System
* 🚨 Threat Classification (Low / Medium / High)
* 📏 Distance Estimation (Monocular Approximation)
* 🛰️ Drone Movement Simulation (Keyboard Control)
* 🎥 Live Video Processing + Recording

---

## 🧠 Tech Stack

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* DeepSORT
* NumPy

---

## 📁 Project Structure

```
DRONE/
│── main.py
│── detector.py
│── utils.py
│── output/
│── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone Repository

```
git clone https://github.com/SHRUTI-BARUA/DRONE_OBJECT_DETECTION.git
cd DRONE_OBJECT_DETECTION
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```
python main.py
```

---

## 🎮 Controls

| Key | Action        |
| --- | ------------- |
| L   | Lock Target   |
| W   | Move Forward  |
| S   | Move Backward |
| A   | Move Left     |
| D   | Move Right    |
| ESC | Exit          |

---

## 📸 Output

* Live detection window
* Saved video: `output/output.mp4`

---

## 👨‍💻 Author

Shruti 


