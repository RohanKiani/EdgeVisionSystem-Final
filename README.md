# 📄 Real-Time Edge Vision System  
## YOLOv8-Based Object Detection on Live Camera Feeds  

---

## 🔹 Overview

This project implements a real-time computer vision system for object detection on live camera feeds using a lightweight YOLOv8 model optimized for CPU-based edge execution.

The system simulates an edge deployment pipeline where inference, visualization, and structured logging are performed locally in real time.

---

## 🔹 Core Objectives

* **Live Ingestion:** Ingest continuous live camera feeds.
* **Real-Time Inference:** Perform real-time object detection and classification.
* **Dynamic Visualization:** Display bounding boxes, labels, and confidence scores dynamically on screen.
* **Structured Logging:** Generate structured detection logs in real time.
* **Edge-Ready:** Maintain high performance suitable for resource-constrained edge devices.

---

## 🔹 System Architecture

Camera Input ──> Frame Capture ──> YOLOv8 Inference ──> Post-Processing ──> Visualization ──> Logging


---

## 🔹 Key Properties

* **Modular Architecture:** Decoupled components for easy maintenance and scalability.
* **Frame-Based Processing:** Real-time throughput ensuring low latency.
* **CPU-Optimized Inference:** Tailored pipeline to maximize performance without requiring a dedicated GPU.
* **Edge-Compatible:** Light footprint designed with embedded hardware deployment in mind.

---

## 🔹 Hardware Assumptions

### Deployment Targets
* Raspberry Pi / Single Board Computers (SBCs)
* CPU-only inference systems
* Laptop-based simulation (used for development and evaluation)

### Justification
A laptop was utilized for primary development and testing. The architecture is explicitly designed for edge deployment by leveraging **YOLOv8n**, a highly lightweight model tailored for low-compute environments.

---

## 🔹 Vision Pipeline Capabilities

* Continuous video stream ingestion  
* Frame-level real-time inference  
* Multi-class object detection  
* Dynamic bounding box visualization  
* Confidence score overlay  
* Real-time FPS monitoring  
* Structured JSON logging per frame  

---

## 🔹 Model Information

### YOLOv8 Nano (YOLOv8n)
A lightweight, state-of-the-art pre-trained object detection model.

### Characteristics
* High inference speed on commodity hardware
* Heavily CPU optimized
* Embedded/Edge device friendly
* Pre-trained on the COCO dataset (supporting 80 distinct classes)

---

## 🔹 Output System

### 1. Visual Output
* Real-time rendering of bounding boxes  
* Dynamic class labels  
* Confidence scores  
* Live FPS overlay counter  

### 2. Structured Output
Detections are exported natively using the following structured JSON format:

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

---

## 🔹 Key Features

* **Webcam Integration:** Real-time object detection directly from active local camera feeds.
* **Hardware Efficiency:** CPU-optimized inference pipeline avoiding cloud overhead.
* **Multi-Object Capabilities:** Concurrent multi-object class recognition.
* **Performance Telemetry:** Integrated live FPS tracking.
* **Data Reproducibility:** Structured JSON logging for downstream analytics.

---

## 🔹 How to Run

Clone the repository, install the dependencies, and launch the main execution script:

```bash
pip install -r requirements.txt
python src/main.py
💡 Tip: Press q while focused on the video window to safely stop execution.

🔹 Design Decisions
Model Choice: YOLOv8n was chosen over larger variants to minimize operational latency on edge hardware.

Separation of Concerns: Implemented a highly modular separation between camera capture, core detection, and logging routines.

Local Computing: Prioritized local inference over cloud APIs to ensure network independence and reduced data latency.

Granular Logs: Frame-based logging architecture simplifies debugging and verification pipelines.

🔹 Limitations
Environmental Dependencies: System performance and confidence scores depend heavily on ambient lighting conditions.

Hardware Thresholds: CPU execution imposes an upper limit on maximum achievable FPS.

Domain Adaptation: The baseline COCO dataset may not generalize accurately to niche or highly custom objects without retraining.

🔹 Future Improvements
[ ] Deploy directly to Raspberry Pi hardware and conduct extensive profiling benchmarks.

[ ] Implement INT8 Quantization to accelerate inference speeds on target CPUs.

[ ] Build a local web-based telemetry dashboard.

[ ] Fine-tune the model on domain-specific custom datasets.

[ ] Integrate multiple industrial-grade hardware camera inputs.

🔹 Demo
You can view the system in action here:

Plaintext
demo/demo.mp4
If the video file does not preview or play directly within GitHub, please download it to view the recording locally.

🔹 Conclusion
This system demonstrates a complete, end-to-end real-time edge AI pipeline. By combining robust computer vision inference, a clean modular software layout, and structured output logging, it creates a reliable blueprint for production-ready edge deployment.
