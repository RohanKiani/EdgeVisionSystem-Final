Real-Time Edge Vision System
YOLOv8-Based Object Detection on Live Camera Feeds
1. Project Context

Modern edge systems require real-time perception under constrained compute environments. This project demonstrates a lightweight but fully functional computer vision pipeline capable of performing real-time object detection on live camera input using a CPU-optimized deep learning model.

The system simulates an edge deployment scenario where inference, visualization, and logging are performed locally without relying on cloud processing.

2. Problem Statement

The objective is to design and implement an end-to-end vision system that:

Continuously processes live camera input
Performs real-time object detection and classification
Outputs both visual and structured representations of detected objects
Maintains real-time performance suitable for edge environments

The system must remain efficient, modular, and deployable on resource-constrained hardware such as Raspberry Pi or equivalent systems.

3. System Architecture

The system follows a modular perception pipeline:

Camera Input → Frame Acquisition → YOLOv8 Inference → Post-Processing → Visualization + Logging

Each module is decoupled to ensure:

Maintainability
Scalability
Easy hardware portability (PC → Edge device transition)
4. Hardware Assumption

While development was performed on a laptop, the system is explicitly designed for edge compatibility.

Deployment Target:
Raspberry Pi / Single Board Computer
CPU-only inference environment
Justification:

A laptop was used for rapid prototyping. However, YOLOv8n (nano variant) was intentionally selected to ensure feasibility on low-power embedded systems, aligning with real edge deployment constraints.

5. Vision Pipeline Capabilities

The system fulfills all required functional constraints:

Continuous live video stream ingestion
Frame-level real-time inference
Multi-class object detection
Bounding boxes with confidence visualization
Real-time performance monitoring (FPS tracking)
Structured output generation per frame
6. Model Selection Rationale
Model: YOLOv8 Nano (YOLOv8n)

This model was selected due to the following trade-offs:

Factor	Decision
Accuracy	Moderate (acceptable for real-time use)
Speed	High (optimized for CPU inference)
Deployment	Edge-friendly
Complexity	Low overhead

The model is pre-trained on the COCO dataset, enabling detection of 80 general object classes without additional training.

7. Output Design Philosophy

A key design decision was ensuring the system is not only visual but also machine-interpretable.

🔹 Dual Output Strategy
1. Human-readable output
Bounding boxes
Class labels
Confidence scores
FPS overlay
2. Machine-readable output
JSON-based structured logs per frame
Timestamped detection history

This enables debugging, analytics, and downstream system integration.

8. Structured Output Example
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
9. Key Features
Real-time object detection on live webcam feed
CPU-optimized inference pipeline
Multi-object class recognition
FPS-based performance monitoring
Structured JSON logging system
Modular architecture for edge adaptability
10. How to Run
pip install -r requirements.txt
python src/main.py

Press q to terminate execution.

11. Design Decisions & Trade-offs

Several intentional engineering trade-offs were made:

YOLOv8n over larger models → prioritizing latency over marginal accuracy
Local inference over cloud APIs → ensuring edge feasibility
Frame-by-frame logging → enabling reproducibility and debugging
Modular architecture → supporting future hardware migration

These choices reflect a system designed for real-world embedded AI constraints rather than purely academic benchmarks.

12. Limitations
Performance depends on lighting conditions and camera quality
CPU-bound execution limits maximum FPS
Pre-trained COCO dataset may not generalize to domain-specific objects
13. Future Improvements
Raspberry Pi deployment with hardware benchmarking
INT8 model quantization for edge acceleration
Web-based real-time monitoring dashboard
Custom dataset fine-tuning for domain-specific detection
14. Demo

A live demonstration is available in:

demo/demo.mp4

If the video does not play on GitHub, download it and view locally.

15. Closing Statement

This project demonstrates a complete real-time edge perception pipeline integrating computer vision inference, system-level modular design, and structured output engineering.

The emphasis is not only on detection accuracy, but on deployability, architectural clarity, and real-time performance under constrained compute environments.
