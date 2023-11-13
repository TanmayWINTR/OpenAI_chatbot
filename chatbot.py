import openai
import gradio as gr

# Load the API key securely (replace 'your-api-key' with your actual API key)
openai.api_key = "your-api-key"

messages = [{"role": "system", "content": "You are a financial expert specializing in real estate investment and negotiation. You answer the financial questions in less than 20 words."}]

def CustomChatGPT(user_input):
    if not user_input.strip():
        return "Please enter a valid question or statement related to real estate investment."

    try:
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ChatGPT_reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
    except Exception as e:
        return f"An error occurred: {str(e)}"

def clear_messages():
    messages.clear()
    messages.append({"role": "system", "content": "You are a financial expert specializing in real estate investment and negotiation"})
    return "Chat history cleared."

with gr.Blocks() as demo:
    gr.Markdown("### Real Estate Pro Chatbot")
    gr.Markdown("Ask any questions about real estate investment and negotiation.")
    input_text = gr.Textbox(label="Your Question", placeholder="Enter your question here...")
    output_text = gr.Textbox(label="Chatbot Response", placeholder="Response will appear here...")
    clear_button = gr.Button("Clear Chat")
    submit_button = gr.Button("Submit")

    submit_button.click(CustomChatGPT, inputs=input_text, outputs=output_text)
    clear_button.click(clear_messages, inputs=None, outputs=output_text)

demo.launch(share=True)
