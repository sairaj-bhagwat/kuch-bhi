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
    
    # Parse ingredients and headlines more robustly
    ingredients = [i.strip() for i in request.form.get('ingredients', '').split(',') if i.strip()]
    benefit_headlines = [b.strip() for b in request.form.get('benefit_headlines', '').split(',') if b.strip()]
    
    if not benefit_headlines:
        benefit_headlines = ["Supports Your Natural Wellness"]
        
    # Simple list of tuples for ingredients with benefits
    benefit_points = [(ing, f"Supports {ing} health") for ing in ingredients[:4]]
    
    how_to_use_steps = [
        ("Step 1", "Mix with water"),
        ("Step 2", "Shake well"),
        ("Step 3", "Enjoy daily")
    ]
    
    # Initialize Generator
    gen = AdGenerator(brand_name, product_name, price)
    
    print(f"Generating ads for: {product_name}...")
    
    # Generate and save all 6 frames
    frames = [
        (gen.generate_frame_1_product_shot(product_image_path), "1_product_shot.png"),
        (gen.generate_frame_2_wellness_benefit(benefit_headlines[0]), "2_wellness_benefit.png"),
        (gen.generate_frame_3_ingredient_benefit(benefit_points), "3_ingredient_benefit.png"),
        (gen.generate_frame_4_how_to_use(how_to_use_steps), "4_how_to_use.png"),
        (gen.generate_frame_5_ingredient_list(ingredients), "5_ingredient_list.png"),
        (gen.generate_frame_6_offer_solution(product_image_path), "6_offer_solution.png")
    ]
    
    for canvas, filename in frames:
        gen.save_frame(canvas, filename, output_dir=EXPORT_DIR)
        print(f"Saved {filename}")
    
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
