import gradio as gr
import google.generativeai as genai
import os

# ১. API Key সেটআপ
api_key = os.getenv("AIzaSyDs9XuXRHV6XS0jk-m7roRoTffo1CczmAE")
genai.configure(api_key=api_key)

# ২০২৬ এর সবচেয়ে পাওয়ারফুল এবং স্টেবল মডেল নাম
# এখানে 'gemini-2.0-pro' অথবা 'gemini-2.0-flash' ব্যবহার করছি
MODEL_NAME = 'gemini-2.5-flash' 

def generate_alert():
    infra_name = "Kurigram General Hospital"
    location = "25.8083, 89.6451"
    
    # মডেল কল করার সময় ভার্সন ইরর এড়াতে ট্রাই-ক্যাচ
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        
        prompt = f"""
        You are an elite Disaster Management Officer in Bangladesh. 
        Current Status: {infra_name} is isolated by floods (Coords: {location}).
        Task: Create a high-urgency Emergency Alert in BENGALI. 
        The tone should be authoritative yet helpful. 
        Include: Warning about transport disruption and instructions for emergency contact.
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        # যদি ২.০ প্রো-তে সমস্যা হয়, এটি অটোমেটিক ২.০ ফ্ল্যাশ ট্রাই করবে
        try:
            fallback_model = genai.GenerativeModel('gemini-2.0-flash')
            response = fallback_model.generate_content(prompt)
            return response.text
        except:
            return f"Error: {str(e)}. মেমোরি বা এপিআই কী সেটিংস চেক করুন।"

# ২. ড্যাশবোর্ড ডিজাইন
with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# 🛡️ OmniGuard-AI: Live Isolation Alert System")
    gr.Markdown("### Inter-University Mapathon 2026 Project (Kurigram Case Study)")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("## 🏥 Isolated Infrastructure Info")
            gr.Markdown(f"**Target:** Kurigram General Hospital")
            gr.Markdown(f"**Coordinates:** 25.8083, 89.6451")
            
            # ইমেজ এরর হ্যান্ডলিং
            try:
                gr.Image("kurigram_flood_impact.png", label="Live Flood Impact Map")
            except:
                gr.Markdown("*(ম্যাপের ছবিটি 'Files' ট্যাবে আপলোড করুন)*")
            
        with gr.Column():
            gr.Markdown("## 📡 Automated Bengali Alert")
            alert_output = gr.Textbox(label="Status: Waiting for trigger...", lines=10)
            btn = gr.Button("🚨 Generate Emergency Alert", variant="primary")
            btn.click(fn=generate_alert, inputs=[], outputs=alert_output)

demo.launch()