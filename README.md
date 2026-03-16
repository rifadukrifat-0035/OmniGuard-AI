# 🛰️ OmniGuard-AI: Disaster Isolation Tracker
**"Mapping Functional Paralysis and Cascading Connectivity Failure in Flood-Prone Regions."**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Google Earth Engine](https://img.shields.io/badge/Cloud-Google%20Earth%20Engine-green)](https://earthengine.google.com/)
[![Track](https://img.shields.io/badge/Mapathon%202026-ResilienceAI-red)](https://example.com)

## 📌 Overview
OmniGuard-AI is a high-performance, **Cloud-Native Geospatial Pipeline** designed to identify "Cascading Isolation" during flood disasters. Unlike traditional flood maps that only show inundation, OmniGuard-AI mathematically identifies critical infrastructure (Hospitals, Cyclone Shelters) that are physically dry but functionally isolated because their access road networks are submerged.

## 🚨 The Problem: "The Isolation Gap"
During floods in Bangladesh (e.g., Kurigram 2024), rescue teams often face the "Isolation Gap"—where a hospital remains above water, but all connecting roads are flooded. Traditional GIS tools fail to alert responders about these **Topological Islands** in real-time.

## 🛠️ The Solution: OmniGuard-AI Architecture
We bypass local hardware limitations (4GB RAM) by using a 100% Cloud-Native stack:

1.  **Hazard Detection (GEE):** Uses Sentinel-1 SAR imagery and Otsu Thresholding to create a real-time binary water mask.
2.  **Graph-Based Analysis (NetworkX):** Models the OpenStreetMap (OSM) road network as a mathematical graph $G(V, E)$. Roads intersecting the water mask are dynamically pruned.
3.  **Isolation Logic:** Detects disconnected sub-graphs to identify isolated lifeline buildings.
4.  **Generative AI Intelligence (Gemini):** Converts complex coordinate data into professional, localized **Bengali Emergency Alerts** for last-mile communication.

## 🚀 Key Features
- **Real-Time SAR Processing:** High-frequency monitoring even during cloud cover.
- **Graph-Intersector:** Identifies the exact road segments causing isolation.
- **LLM-Powered Alerts:** Automated, human-readable Bengali SMS/Alert generation.
- **Zero-Local Footprint:** Entirely hosted on Google Colab and Hugging Face.

## 💻 Tech Stack
* **Engine:** Google Earth Engine (Python API)
* **Graph Theory:** NetworkX, OSMNX
* **LLM Core:** Google Gemini 1.5/2.5 Flash
* **Dashboard:** Streamlit / Gradio
* **Deployment:** Hugging Face Spaces

## 🏥 Case Study: Kurigram 2024
- **Detected Infrastructure:** Kurigram General Hospital (25.8083, 89.6451).
- **Impact:** 100% road connectivity failure identified.
- **AI Alert:** *"কুড়িগ্রাম জেনারেল হাসপাতাল বর্তমানে সম্পূর্ণভাবে যোগাযোগ বিচ্ছিন্ন... নৌকা-ভিত্তিক পরিবহন ব্যবহার করুন।"*

## 📁 Repository Structure
```text
├── OmniGuard_Pipeline.ipynb  # Core Research & Colab Notebook
├── app.py                    # Streamlit/Gradio UI Code
├── requirements.txt          # Environment Dependencies
├── assets/                   # Geospatial Result Maps
└── README.md                 # Project Documentation
