#Drone Object Detection System
📌 Overview
This project implements a real-time drone surveillance system using YOLOv8, OpenCV, and DeepSORT. It detects, tracks, and analyzes objects from a live camera feed, simulating core functionalities used in defense-grade UAV systems.

✨ Key Features
🎯 Real-time Object Detection (YOLOv8)
🔄 Multi-Object Tracking (DeepSORT)
🎯 Target Locking System
🚨 Threat Classification (Low / Medium / High)
📏 Distance Estimation (Monocular Approximation)
🛰️ Drone Movement Simulation (Keyboard Control)
🎥 Live Video Processing + Recording
🧠 Tech Stack
  Python
  OpenCV
  YOLOv8 (Ultralytics)
  DeepSORT Tracker
  NumPy
📁 Project Structure
DRONE/
  │── main.py
  │── detector.py
  │── utils.py
  │── output/
  │── requirements.txt

⚙️ Installation
1. Clone Repository
  git clone https://github.com/yourusername/drone-object-detection.git
  cd drone-object-detection
2. Create Virtual Environment
  python -m venv venv
  venv\Scripts\activate   # Windows
3. Install Dependencies
  pip install -r requirements.txt
4. Run the Project
  python main.py
🎮 Controls
Key	Action:
L	Lock Target 🎯
W	Move Forward
S	Move Backward
A	Move Left
D	Move Right
ESC	Exit

📌 Use Cases
Defense Surveillance Systems
Smart Security Monitoring
Autonomous Drone Research

Author:
SHRUTI
