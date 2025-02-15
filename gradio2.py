import gradio as gr
import requests
import json
import requests
import ollama

def message_ollama(model,prompt,system_message):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
      ]
    completion = ollama.chat(
        model=model,
        messages=messages,
        stream=True
    )
    res=""
    for chunk in completion:
        res+=chunk['message']['content']
        yield res
   
    

view = gr.Interface(
    fn=message_ollama,
    title="Gradio AI Chatbot",
    inputs=[gr.Textbox(label="Your model", value="llama3.2", interactive=False),
            gr.Textbox(label="System Prompt", placeholder="Describe chatbot behavior"),
            gr.Textbox(label="Your Message", placeholder="Type here")],
    outputs=[gr.Text(label="Response",interactive=False)],
    flagging_mode="never",
    
)
view.launch(share=True)
