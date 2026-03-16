from generator import AdGenerator
import os

def run_generator():
    # Dynamic Inputs
    brand_name = "Zenith Herbal"
    product_name = "Vitality Blend"
    price = "₹599"
    product_image_path = "C:\\Users\\Main\\.gemini\\antigravity\\brain\\75c132c6-d0c9-41eb-8324-cff6b717fdde\\sample_wellness_product_1773650319659.png" # Using generated sample
    
    ingredient_list = [
        "Ashwagandha",
        "Brahmi",
        "Turmeric",
        "Ginger Root",
        "Pure Honey"
    ]
    
    benefit_points = [
        ("Ashwagandha", "Helps reduce stress"),
        ("Brahmi", "Supports cognitive focus"),
        ("Turmeric", "Maintains healthy joints"),
        ("Pure Honey", "Natural energy boost")
    ]
    
    wellness_headline = "Supports Your Daily Energy Levels"
    
    how_to_use_steps = [
        ("Step 1", "Mix 1 scoop with warm water"),
        ("Step 2", "Stir well until dissolved"),
        ("Step 3", "Drink every morning")
    ]
    
    # Initialize Generator
    gen = AdGenerator(brand_name, product_name, price)
    
    print("Generating GMC-Compliant Ad Creatives...")
    
    # Frame 1
    f1 = gen.generate_frame_1_product_shot(product_image_path)
    gen.save_frame(f1, "1_product_shot.png")
    
    # Frame 2
    f2 = gen.generate_frame_2_wellness_benefit(wellness_headline)
    gen.save_frame(f2, "2_wellness_benefit.png")
    
    # Frame 3
    f3 = gen.generate_frame_3_ingredient_benefit(benefit_points)
    gen.save_frame(f3, "3_ingredient_benefit.png")
    
    # Frame 4
    f4 = gen.generate_frame_4_how_to_use(how_to_use_steps)
    gen.save_frame(f4, "4_how_to_use.png")
    
    # Frame 5
    f5 = gen.generate_frame_5_ingredient_list(ingredient_list)
    gen.save_frame(f5, "5_ingredient_list.png")
    
    # Frame 6
    f6 = gen.generate_frame_6_offer_solution(product_image_path)
    gen.save_frame(f6, "6_offer_solution.png")
    
    print("Success! Creatives exported to 'exports/' folder.")

if __name__ == "__main__":
    run_generator()
