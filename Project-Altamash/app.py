import os
import openai
import gradio as gr


#if you have OpenAI API key as an environment variable, enable the below
# openai.api_key = os.getenv("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")

openai.api_key = "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"
#if you have OpenAI API key as a string, enable the below
# openai.api_key = "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"
# openai.api_key="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"

# openai.api_key = "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"
# openai.api_key ="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"


start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversesion with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\ncontact with Altamash: "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Welcome to Our AI Conversession  </center></h1>
    """)
    gr.Markdown("""<h1><center>J.C.BOSE UNIVERSITY OF SCIENCE & TECHNOLOGY , YMCA , FARIDABAD 💕 </center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("Ask What You Want")

    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)
