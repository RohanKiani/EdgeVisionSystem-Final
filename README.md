
Real-Time Edge Vision System

YOLOv8-Based Object Detection on Live Camera Feeds

🔹 Overview

This project implements a real-time computer vision system for object detection on live camera feeds using a lightweight YOLOv8 model optimized for CPU-based edge execution.

The system is designed with a modular streaming architecture that processes frames in real time, performs inference, and outputs both visual and structured detection results.

🔹 Core Objectives

The system is designed to:

Ingest continuous live camera feed
Perform real-time object detection and classification
Display bounding boxes, labels, and confidence scores
Generate structured detection logs in real time
Maintain performance suitable for edge devices

🔹 System Architecture

The system follows a modular streaming pipeline:

Camera Input → Frame Capture → YOLOv8 Inference → Post-Processing → Visualization → Logging

Key Design Properties:
Fully modular architecture
Real-time frame-based processing
CPU-optimized inference pipeline
Edge-device deployment compatibility

🔹 Hardware Assumption

Deployment Targets:
Raspberry Pi / Single Board Computers
CPU-only inference systems
Laptop-based simulation environment (used for development)
Justification:

A laptop was used for development and testing. However, the system is explicitly designed for edge deployment using YOLOv8n, a lightweight model optimized for low-compute environments.

🔹 Vision Pipeline Capabilities

The system supports:

Continuous video stream ingestion
Frame-level real-time inference
Multi-class object detection
Bounding box visualization
Confidence score display
FPS monitoring
Structured JSON logging

🔹 Model Information

YOLOv8 Nano (YOLOv8n)

A lightweight pre-trained object detection model.

Key Characteristics:
High inference speed
Optimized for CPU execution
Suitable for edge deployment
Trained on COCO dataset (80 classes)

🔹 Output System

Visual Output
Bounding boxes
Class labels
Confidence scores
FPS overlay
Structured Output

JSON-based per-frame detection logs:

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
Structured JSON logging system
Modular edge-ready architecture

🔹 How to Run

pip install -r requirements.txt
python src/main.py

Press q to stop execution.

🔹 Design Decisions

YOLOv8n selected for low-latency edge performance
Modular separation of camera, detection, and logging logic
Local inference used instead of cloud APIs
Frame-based logging for reproducibility and debugging
Lightweight architecture for embedded deployment

🔹 Limitations

Performance depends on lighting conditions
CPU inference limits maximum FPS
COCO dataset may not generalize to custom objects

🔹 Future Improvements

Raspberry Pi deployment with benchmarking
INT8 quantization for faster edge inference
Web-based real-time dashboard
Custom dataset fine-tuning
Real hardware camera integration optimization

🔹 Demo

Live demonstration available at:

demo/demo.mp4

If video does not play on GitHub, download and view locally.

🔹 Conclusion

This project demonstrates a complete real-time edge AI perception system combining computer vision inference, modular software architecture, and structured output generation.

The focus is on:

Real-time performance
Edge deployment feasibility
Clean system design
Scalable modular structure
