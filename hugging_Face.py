from flask import Flask, render_template, request, jsonify
from diffusers import DiffusionPipeline
import torch

app = Flask(__name)

# Initialize the DiffusionPipeline and set it to run on GPU
pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")

# Define the home route to render the HTML UI
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to handle image generation
@app.route('/generate_image', methods=['POST'])
def generate_image():
    text = request.form.get('text')
    
    # Generate an image using the text-to-image model
    images = pipe(prompt=text).images[0]
    
    # Convert the image tensor to bytes
    image_bytes = images.numpy().tobytes()
    
    return image_bytes

if __name__ == '__main__':
    app.run(debug=True)
