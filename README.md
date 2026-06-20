# 📄 Real-Time Edge Vision System  
## YOLOv8-Based Object Detection on Live Camera Feeds  

---

# 🔹 Overview

This project implements a real-time computer vision system for object detection on live camera feeds using a lightweight YOLOv8 model optimized for CPU-based edge execution.

The system simulates an edge deployment pipeline where inference, visualization, and structured logging are performed locally in real time.

---

# 🔹 Core Objectives

The system is designed to:

- Ingest continuous live camera feed  
- Perform real-time object detection and classification  
- Display bounding boxes, labels, and confidence scores  
- Generate structured detection logs in real time  
- Maintain performance suitable for edge devices  

---

# 🔹 System Architecture

Camera Input → Frame Capture → YOLOv8 Inference → Post-Processing → Visualization → Logging

### Key Properties

- Modular architecture  
- Real-time frame-based processing  
- CPU-optimized inference pipeline  
- Edge-device compatible design  

---

# 🔹 Hardware Assumption

### Deployment Targets

- Raspberry Pi / Single Board Computers  
- CPU-only inference systems  
- Laptop-based simulation (used for development)

### Justification

A laptop was used for development and testing. The system is designed for edge deployment using YOLOv8n, a lightweight model optimized for low-compute environments.

---

# 🔹 Vision Pipeline Capabilities

- Continuous video stream ingestion  
- Frame-level real-time inference  
- Multi-class object detection  
- Bounding box visualization  
- Confidence score display  
- FPS monitoring  
- Structured JSON logging  

---

# 🔹 Model Information

### YOLOv8 Nano (YOLOv8n)

Lightweight pre-trained object detection model.

### Characteristics

- High inference speed  
- CPU optimized  
- Edge-device friendly  
- Trained on COCO dataset (80 classes)  

---

# 🔹 Output System

### Visual Output

- Bounding boxes  
- Class labels  
- Confidence scores  
- FPS overlay  

### Structured Output

```json
{
  "timestamp": 1710000000,
  "detections": [
    {
      "label": "person",
      "confidence": 0.91,
      "bbox": [120, 200, 400, 600]
    }
  ]
}
🔹 Key Features
Real-time object detection using webcam
CPU-optimized inference pipeline
Multi-object class recognition
FPS performance tracking
Structured JSON logging
Modular edge-ready architecture
🔹 How to Run
pip install -r requirements.txt
python src/main.py

Press q to stop execution.

🔹 Design Decisions
YOLOv8n selected for low-latency edge performance
Modular separation of camera, detection, and logging
Local inference instead of cloud APIs
Frame-based logging for debugging and reproducibility
Lightweight design for embedded systems
🔹 Limitations
Performance depends on lighting conditions
CPU limits maximum FPS
COCO dataset may not generalize to custom objects
🔹 Future Improvements
Raspberry Pi deployment + benchmarking
INT8 quantization for acceleration
Web-based dashboard
Custom dataset fine-tuning
Real hardware camera integration
🔹 Demo

demo/demo.mp4

If the video does not play on GitHub, download and view locally.

🔹 Conclusion

This system demonstrates a complete real-time edge AI pipeline combining:

Computer vision inference
Modular software architecture
Structured output generation

Focus areas:

Real-time performance
Edge deployment readiness
Clean modular design
Scalable system structure
