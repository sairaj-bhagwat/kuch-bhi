from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from generator import AdGenerator

app = Flask(__name__)
EXPORT_DIR = os.path.join(os.path.dirname(__file__), 'exports')

# Ensure export directory exists
if not os.path.exists(EXPORT_DIR):
    os.makedirs(EXPORT_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get form data
    brand_name = request.form.get('brand_name')
    product_name = request.form.get('product_name')
    price = request.form.get('price')
    # For local hosting, we'll use a fixed sample path or allow upload. 
    # For now, we'll use the sample generated previously for demo.
    product_image_path = "C:\\Users\\Main\\.gemini\\antigravity\\brain\\75c132c6-d0c9-41eb-8324-cff6b717fdde\\sample_wellness_product_1773650319659.png"
    
    ingredients = request.form.get('ingredients').split(',')
    benefit_headlines = request.form.get('benefit_headlines').split(',')
    
    # Simple list of tuples for ingredients with benefits
    benefit_points = [(ing.strip(), f"Supports {ing.strip()} health") for ing in ingredients[:4]]
    
    how_to_use_steps = [
        ("Step 1", "Mix with water"),
        ("Step 2", "Shake well"),
        ("Step 3", "Enjoy daily")
    ]
    
    # Initialize Generator
    gen = AdGenerator(brand_name, product_name, price)
    
    # Generate Frames
    f1 = gen.generate_frame_1_product_shot(product_image_path)
    gen.save_frame(f1, "1_product_shot.png", output_dir=EXPORT_DIR)
    
    f2 = gen.generate_frame_2_wellness_benefit(benefit_headlines[0])
    gen.save_frame(f2, "2_wellness_benefit.png", output_dir=EXPORT_DIR)
    
    f3 = gen.generate_frame_3_ingredient_benefit(benefit_points)
    gen.save_frame(f3, "3_ingredient_benefit.png", output_dir=EXPORT_DIR)
    
    f4 = gen.generate_frame_4_how_to_use(how_to_use_steps)
    gen.save_frame(f4, "4_how_to_use.png", output_dir=EXPORT_DIR)
    
    f5 = gen.generate_frame_5_ingredient_list([i.strip() for i in ingredients])
    gen.save_frame(f5, "5_ingredient_list.png", output_dir=EXPORT_DIR)
    
    f6 = gen.generate_frame_6_offer_solution(product_image_path)
    gen.save_frame(f6, "6_offer_solution.png", output_dir=EXPORT_DIR)
    
    return redirect(url_for('results'))

@app.route('/results')
def results():
    images = [f for f in os.listdir(EXPORT_DIR) if f.endswith('.png')]
    return render_template('results.html', images=images)

@app.route('/exports/<filename>')
def serve_export(filename):
    return send_from_directory(EXPORT_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
