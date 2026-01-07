# AutoSentry 🛡️
### Real-Time Network Anomaly Detection using Deep Learning & Kafka

**AutoSentry** is a production-grade Intrusion Detection System (IDS) that leverages **Autoencoders** to identify malicious network activity. Developed as part of an applied data science initiative (IIT Delhi), it moves beyond static analysis by utilizing a real-time streaming architecture.

---

## 🚀 Overview
Traditional security systems rely on signatures of *known* attacks. **AutoSentry** uses **Unsupervised Learning** to learn the "fingerprint" of normal network traffic, allowing it to detect **Zero-Day attacks** by identifying statistical deviations (Reconstruction Error).

## 🏗️ System Architecture
The system is built on a modular "Stream-to-Inference" pipeline:

1.  **Ingestion Layer**: Network flows are captured and streamed via **Apache Kafka**.
2.  **Processing Layer**: Tabular data is pre-processed and normalized using **Scikit-Learn**.
3.  **Inference Layer**: A **PyTorch-based Autoencoder** evaluates the reconstruction loss of incoming flows.
4.  **Alerting Layer**: High-loss events are flagged and visualized in a **Streamlit** dashboard.

---

## 🛠️ Tech Stack
* **AI/ML**: PyTorch (Deep Learning), Scikit-Learn (Preprocessing)
* **Data Pipeline**: Apache Kafka (Streaming), Pandas (Tabular manipulation)
* **Deployment**: FastAPI (Inference API), Docker & Docker Compose (Containerization)
* **Frontend**: Streamlit (Real-time Monitoring Dashboard)

---

## 📊 ML Approach: The Autoencoder
We utilize an **Undercomplete Autoencoder** architecture. By forcing the network through a narrow bottleneck (Latent Space), the model learns the most salient features of "Normal" traffic.

* **Training Data**: [e.g., CIC-IDS2017 Dataset - Normal packets only]
* **Loss Function**: Mean Squared Error (MSE)
* **Anomaly Threshold**: Determined via the 99th percentile of training reconstruction error.

