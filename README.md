📄 Real-Time Edge Vision System
YOLOv8-Based Object Detection on Live Camera Feeds

1. Project Context
Modern edge systems require real-time perception capabilities under constrained compute environments. This project demonstrates a lightweight yet fully functional computer vision pipeline capable of performing real-time object detection on live camera input using a CPU-optimized deep learning model.

The system is designed to simulate an edge deployment scenario where inference, visualization, and logging are performed locally without reliance on cloud processing.

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
Raspberry Pi / SBC
CPU-only inference environment
Justification:

A laptop environment was used for rapid prototyping. However, YOLOv8n (nano variant) was intentionally selected to ensure feasibility on low-power embedded systems, aligning with real edge deployment constraints.

5. Vision Pipeline Capabilities
The system fulfills all required functional constraints:

Continuous live video stream ingestion
Frame-level real-time inference
Multi-class object detection
Bounding box + confidence visualization
Real-time performance monitoring (FPS tracking)
Structured output generation per frame

6. Model Selection Rationale
Model: YOLOv8 Nano (YOLOv8n)

This model was selected based on the following trade-offs:

Factor	Decision
Accuracy	Moderate (acceptable for real-time use)
Speed	High (optimized for CPU inference)
Deployment	Edge-friendly
Complexity	Low overhead

The model is pre-trained on the COCO dataset, enabling detection of 80 general object classes without additional training overhead.

7. Output Design Philosophy
A key design decision was to ensure that the system is not purely visual, but also machine-interpretable.

Dual Output Strategy:
Human-readable output
Bounding boxes
Labels
Confidence scores
FPS overlay
Machine-readable output
JSON-based structured logs per frame
Timestamped detection history

This enables downstream analytics, debugging, and system evaluation.

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
Modular architecture for edge deployment adaptability

10. How to Run
pip install -r requirements.txt
python src/main.py

Press q to terminate execution.

11. Design Decisions & Engineering Trade-offs
Several intentional trade-offs were made:

YOLOv8n over larger models → prioritizing latency over marginal accuracy gains
Local inference over cloud APIs → ensuring edge-device feasibility
Frame-by-frame logging → enabling reproducibility and debugging
Modular architecture → supporting future hardware migration

These decisions reflect a system designed for real-world embedded AI constraints rather than purely academic performance.

12. Limitations
Performance depends on lighting conditions and camera quality
CPU-bound execution limits maximum achievable FPS
Pre-trained COCO dataset may not generalize to domain-specific objects

13. Future Improvements
Deployment on Raspberry Pi with hardware benchmarking
Model quantization (INT8 optimization for edge acceleration)
Web-based real-time dashboard
Custom dataset fine-tuning for domain-specific detection

14. Demo
A live demonstration of the system is available in:
demo/demo.mp4
If the video does not play on GitHub, download it and view locally.

15. Closing Statement
This project demonstrates a complete real-time edge perception pipeline integrating computer vision inference, system-level design, and structured output engineering. The focus was not only on achieving detection accuracy but also on ensuring deployability, modularity, and real-time performance under constrained compute environments.