# 🛰️ OmniGuard-AI: Visual & Topological Disaster Intelligence
**"Solving the Invisibility Gap: Mapping Functional Paralysis and Cascading Connectivity Failure."**

[![Cloud-Native](https://img.shields.io/badge/Architecture-100%25%20Cloud--Native-blue.svg)](https://earthengine.google.com/)
[![Track](https://img.shields.io/badge/Mapathon%202026-ResilienceAI-red)](https://example.com)
[![Engine](https://img.shields.io/badge/AI-Gemini%20%2B%20Roboflow-green)](https://aistudio.google.com/)

---

## 📌 Overview
OmniGuard-AI is a high-performance **Geospatial Pipeline** designed to identify **"Functional Isolation"** during disaster events. Traditional flood maps only show where the water is; OmniGuard-AI identifies critical infrastructure (Hospitals, Shelters) that remains dry but becomes functionally paralyzed because all connecting road networks are submerged.

This project was built under strict hardware constraints (4GB RAM), utilizing a **100% Cloud-Native stack** to ensure scalability and accessibility for last-mile responders.

## 🚨 The Problem: "The Invisibility Gap"
During floods (e.g., Kurigram 2024), many facilities remain physically above water but are "isolated" due to the **Topological Island Effect**. Current GIS tools often fail to alert rescue teams that a dry facility is actually unreachable by land.

## 🛠️ The OmniGuard Solution (Phase 1-5)

### 1. Hazard Detection (GEE)
Uses **Sentinel-1 SAR** imagery and Otsu Thresholding via Google Earth Engine to create real-time, cloud-free binary water masks.

### 2. Topological Analysis (NetworkX)
Models the road network as a mathematical graph $G(V, E)$. The system dynamically "prunes" edges (roads) that intersect with the flood mask to identify disconnected sub-graphs.

### 3. Visual Intelligence (Roboflow API)
Integrates a **Computer Vision Layer** that fetches localized drone/satellite imagery of flagged isolated nodes. Using the Roboflow API, it autonomously detects flooded structures and stranded objects for ground-truth verification.

### 4. Generative AI Reasoning (Gemini)
Synthesizes topological data (isolation) and visual data (object counts) through **Google Gemini 1.5 Flash**. It generates professional, high-priority **Bengali Emergency Broadcasts** advising specific actions (e.g., boat-based rescue).

### 5. Live Dashboard (Hugging Face)
A live, interactive Gradio dashboard where users can run the entire pipeline and view real-time situational reports.

## 💻 Tech Stack
* **Satellite Engine:** Google Earth Engine (Python API)
* **Graph Theory:** NetworkX, OSMNX
* **Computer Vision:** Roboflow API (YOLOv8 Weights)
* **Generative AI:** Google Gemini 1.5 Flash
* **Deployment:** Hugging Face Spaces (Gradio)
* **Hardware Efficiency:** 100% Cloud-based (No local GPU/RAM load)

## 📁 Repository Structure
```text
├── OmniGuard_Pipeline.ipynb  # Main Research & Analysis Notebook (Colab)
├── app.py                    # Live Gradio Dashboard Code (Hugging Face)
├── requirements.txt          # Cloud Dependencies
├── assets/                   # Maps, Graph Results & Roboflow Detections
└── README.md                 # Project Documentation & Master Plan
