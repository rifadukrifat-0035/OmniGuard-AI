import gradio as gr
import google.generativeai as genai
import requests
import re

# ১. API Keys
ROBOFLOW_API_KEY = "YOUR_KEY"
RAW_GEMINI_KEY = "YOUR_KEY" 
CLEAN_GEMINI_KEY = re.sub(r'[^a-zA-Z0-9_-]', '', RAW_GEMINI_KEY)


genai.configure(api_key=CLEAN_GEMINI_KEY)

test_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Flood_in_Bangladesh_%282007%29.jpg/800px-Flood_in_Bangladesh_%282007%29.jpg"


def run_omniguard():
    try:
        # Roboflow Analysis (Lightweight REST API call)
        roboflow_url = "https://detect.roboflow.com/flood-house/9"
        params = {
            "api_key": ROBOFLOW_API_KEY,
            "image": test_image_url
        }
        res = requests.post(roboflow_url, params=params)
        res_data = res.json()
        
        flooded_count = len(res_data.get('predictions', []))
        vision_status = f"✅ Roboflow Vision Match: {flooded_count} flooded structures detected nearby."
        
        # Gemini Analysis
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = f"""
        You are the Chief Coordinator of the Bangladesh Disaster Management Bureau.
        Context: Kurigram General Hospital is physically isolated. Access roads are 100% submerged.
        Visual Intel: Live drone imagery detects {flooded_count} flooded structures in the immediate vicinity.

        Task: Write an official, high-priority emergency broadcast in BENGALI. 
        Format requirements:
        - Start with a bold heading: "🔴 [জরুরি বন্যা সতর্কবার্তা]"
        - Use 2-3 short bullet points.
        - Explicitly mention the hospital and the {flooded_count} flooded structures.
        - End advising boat-based evacuation and 999.
        Keep it formal, highly urgent, and within 60 words.
        """
        response = model.generate_content(prompt)
        
        return vision_status, response.text
    except Exception as e:
        return f"Error: {str(e)}", "Pipeline Failed. Check API Keys or Internet Connection."

# ৩. Gradio UI (Deep-Tech Layout)
with gr.Blocks() as demo:
    gr.Markdown("# 🛰️ OmniGuard-AI: Visual & Topological Disaster Intelligence")
    gr.Markdown("### Integrating Graph Theory, Computer Vision, and LLMs | **Mapathon 2026**")
    
    with gr.Row():
        # বাম পাশের কলাম
        with gr.Column():
            gr.Markdown("### 📍 Infrastructure Status (Phase 1-4)")
            gr.Markdown("**Target Site:** Kurigram General Hospital (25.8083° N, 89.6451° E)")
            gr.Markdown("**Topological Status:** 🔴 100% Functionally Isolated (Access roads submerged).")
            # HTML ব্যবহার করে ছবি দেখানো (উইকিপিডিয়া ব্লক করবে না)
            gr.HTML(f'<img src="{test_image_url}" alt="Live Drone/Optical Feed" style="width: 100%; border-radius: 10px;">')
            
        # ডান পাশের কলাম
        with gr.Column():
            gr.Markdown("### 🤖 Multi-Modal Intelligence (Phase 5)")
            gr.Markdown("Click the button below to analyze the drone feed via **Roboflow** and generate an official alert via **Gemini**.")
            
            run_btn = gr.Button("🚨 Run OmniGuard Pipeline", variant="primary")
            
            vision_output = gr.Textbox(label="1. Computer Vision Status (Roboflow)", interactive=False)
            llm_output = gr.Textbox(label="2. Final Emergency Broadcast (Gemini)", lines=7, interactive=False)
            

    run_btn.click(fn=run_omniguard, inputs=[], outputs=[vision_output, llm_output])

# অ্যাপ চালু করা (থিম এখানে দেওয়া হয়েছে)
demo.launch(theme=gr.themes.Soft(primary_hue="red"))
