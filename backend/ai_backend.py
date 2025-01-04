from flask import Flask, request, jsonify
from diffusers import StableDiffusionPipeline
import torch

# Initialize Flask app and AI model
app = Flask(__name__)
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    try:
        # Generate the image
        image = pipe(prompt).images[0]
        image_path = "generated_image.png"
        image.save(image_path)
        return jsonify({'image_url': f"https://your-backend-url.com/{image_path}"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
