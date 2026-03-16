from generator import AdGenerator
import os

def generate_heart_ads():
    # Extracted Details from User's Image
    brand_name = "EVID LABS"
    product_name = "Heart Lipid Lite"
    price = "₹599" # Keeping the previous example price
    
    # Path to the product image (using the provided sample for now)
    # The user can update this path to the actual "Heart Lipid Lite" image file.
    product_image_path = "C:\\Users\\Main\\.gemini\\antigravity\\brain\\75c132c6-d0c9-41eb-8324-cff6b717fdde\\sample_wellness_product_1773650319659.png"
    
    ingredient_list = [
        "Omega-3 (as Salmon Fish Oil)",
        "CoQ10",
        "Aged Garlic extract",
        "Vitamin D3"
    ]
    
    benefit_points = [
        ("Omega-3", "Supports heart health"),
        ("CoQ10", "Supports cellular energy"),
        ("Aged Garlic", "Helps maintain healthy cholesterol"),
        ("Vitamin D3", "Supports cardiovascular health")
    ]
    
    wellness_headline = "Premium Cardiometabolic Support"
    
    how_to_use_steps = [
        ("Step 1", "Take 2 softgels daily"),
        ("Step 2", "Take 2 capsules daily"),
        ("Step 3", "Consult your physician") # Following the text from the bottle
    ]
    
    # Initialize Generator with the new brand color (using a darker blue/navy theme)
    gen = AdGenerator(brand_name, product_name, price)
    # Customize palette to match the image (Navy Blue)
    gen.colors["accent"] = (25, 34, 69) # Dark Navy from image
    gen.colors["bg_light"] = (240, 242, 245)
    
    print(f"Generating {product_name} Creatives...")
    
    export_folder = os.path.join(os.path.dirname(__file__), 'exports_heart')
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
    
    # Generate all 6 frames
    frames = [
        (gen.generate_frame_1_product_shot(product_image_path), "1_heart_product_shot.png"),
        (gen.generate_frame_2_wellness_benefit(wellness_headline), "2_heart_wellness_benefit.png"),
        (gen.generate_frame_3_ingredient_benefit(benefit_points), "3_heart_ingredient_benefit.png"),
        (gen.generate_frame_4_how_to_use(how_to_use_steps), "4_heart_how_to_use.png"),
        (gen.generate_frame_5_ingredient_list(ingredient_list), "5_heart_ingredient_list.png"),
        (gen.generate_frame_6_offer_solution(product_image_path), "6_heart_offer_solution.png")
    ]
    
    for canvas, filename in frames:
        gen.save_frame(canvas, filename, output_dir=export_folder)
        print(f"Saved {filename}")

if __name__ == "__main__":
    generate_heart_ads()
