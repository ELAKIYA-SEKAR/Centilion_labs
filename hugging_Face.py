from flask import Flask, render_template, request, jsonify
from diffusers import DiffusionPipeline
import torch

app = Flask(__name__)

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST', 'GET'])
def generate_image():
    if request.method == 'POST':
        text = request.form.get('text')
        images = pipe(prompt=text).images[0]
        image_bytes = images.numpy().tobytes()
        return jsonify({'image': image_bytes})
    
    return render_template('generate_image.html')

if __name__ == '__main__':
    app.run(debug=True)
