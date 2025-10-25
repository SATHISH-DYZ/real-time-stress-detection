# Live Stress Detection

A **real-time stress detection** web application using facial emotion recognition. The system captures live webcam video, sends frames to an AWS Lambda endpoint with Amazon Rekognition, and displays stress levels in real-time. This project is containerized using **Docker**.

---

## Features

- Real-time stress detection from webcam video.
- Displays:
  - Emotion
  - Stress Level (Low, Medium, High)
  - Stress Score
  - Gauge visualization
  - Stress history
  - Live chart of stress scores
- Color-coded background and stress indicators.
- Lightweight and fast using reduced frame resolution and JPEG compression.
- Fully containerized for easy deployment.

---

## Architecture

1. **Frontend**:
   - HTML + JavaScript for video capture and UI.
   - Sends base64-encoded frames to backend.
   - Displays gauge, chart, history, and overlays.
2. **Backend**:
   - Flask app serving HTML and `/analyze` API endpoint.
   - Forwards frames to AWS Lambda.
3. **AWS Lambda**:
   - Receives base64 images.
   - Uses Amazon Rekognition to detect facial emotions.
   - Calculates stress score and level.
   - Stores results in DynamoDB (optional).

---

## Technologies

- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Backend**: Python, Flask
- **AWS Services**: Lambda, Rekognition, DynamoDB
- **Containerization**: Docker

---

## Installation & Running

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd stress-web

Build Docker image

docker build -t stress-live .


Run Docker container

docker run -d -p 5000:5000 \
  -e API_URL="https://<your-lambda-endpoint>/strees/root" \
  --name stress-live stress-live


Access in browser

http://localhost:5000