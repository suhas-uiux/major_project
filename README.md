# 🚗 Real-Time Number Plate Detection Using YOLOv8
This project performs **real-time number plate detection** using **YOLOv8** and **OpenCV**. It captures frames from your webcam, detects number plates, and displays bounding boxes around them in real-time. You can also adapt it for **CCTV, video streams**, or **image-based detection**.

## 📦 Features
- Real-time video capture using webcam.
- Fast and accurate number plate detection using YOLOv8.
- Works on **CPU** and **GPU**.
- Easily extendable to OCR (Optical Character Recognition) for reading plate numbers.

## 🧠 Tech Stack
- **Python 3.8+**
- **OpenCV**
- **Ultralytics YOLOv8**
- **Torch**
- **Numpy**

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/number-plate-detection.git
cd number-plate-detection
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # For Windows
# source venv/bin/activate  # For Linux/Mac
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

If you face OpenCV display issues, install the **headless version**:
```bash
pip uninstall opencv-python
pip install opencv-python-headless==4.12.0.88
```

## 📁 Project Structure
```
📦 number-plate-detection
 ┣ 📜 number_plate_detection.py     # Main detection script
 ┣ 📜 requirements.txt              # Dependencies list
 ┣ 📜 README.md                     # Documentation
 ┗ 📁 runs/                         # YOLO output results (auto-generated)
```

## ▶️ Usage

### Run the Detection Script
```bash
python number_plate_detection.py
```

If you want to detect number plates from an image:
```bash
python number_plate_detection.py --source path/to/image.jpg
```

To detect from a video file:
```bash
python number_plate_detection.py --source path/to/video.mp4
```

## 🧩 Example Output

**Input:** Real-time webcam feed  
**Output:**  
- Bounding boxes drawn around detected number plates.  
- Labels showing detection confidence.


## 🚀 Future Improvements
- Add OCR for automatic number extraction (e.g., using Tesseract).
- Build a Flask/Streamlit web dashboard for live detection.
- Store detected plates in a database for tracking.


## 🪪 License
This project is licensed under the **MIT License** — you are free to use, modify, and distribute it.

