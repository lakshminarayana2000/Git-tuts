import gradio as gr

def greet(name, age):
  return "Hello " + name + "! You are " + str(age) + " years old."

demo = gr.Interface(
    fn=greet,
    inputs=["text", "number"],
    outputs="text"
)

if __name__ == "__main__":
    demo.launch()