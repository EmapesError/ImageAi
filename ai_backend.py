from flask import Flask, request, jsonify
from diffusers import StableDiffusionPipeline
import torch

# Initialize AI model
app = Flask(__name__)
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    # Generate image
    try:
        image = pipe(prompt).images[0]
        output_path = "generated_image.png"
        image.save(output_path)
        return jsonify({'image_url': f"/{output_path}"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/<path:path>', methods=['GET'])
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
