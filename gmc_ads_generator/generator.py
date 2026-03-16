import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

class AdGenerator:
    def __init__(self, brand_name, product_name, price, font_path="C:\\Windows\\Fonts\\arial.ttf"):
        self.width = 1080
        self.height = 1080
        self.brand_name = brand_name
        self.product_name = product_name
        self.price = price
        self.font_path = font_path
        
        # Color Palette (Wellness/Clean Theme)
        self.colors = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "accent": (76, 175, 80),  # Wellness Green
            "text": (50, 50, 50),
            "bg_light": (245, 245, 245)
        }

    def create_canvas(self, bg_color=None):
        if bg_color is None:
            bg_color = self.colors["white"]
        return Image.new("RGB", (self.width, self.height), bg_color)

    def get_font(self, size):
        try:
            return ImageFont.truetype(self.font_path, size)
        except Exception:
            return ImageFont.load_default()

    def draw_text_centered(self, draw, text, y_offset, size, color=None):
        if color is None:
            color = self.colors["text"]
        font = self.get_font(size)
        
        # Get text bounding box for older and newer Pillow versions
        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
        except AttributeError:
            # Fallback for very old Pillow versions
            text_width, _ = draw.textsize(text, font=font)
            
        x = (self.width - text_width) // 2
        draw.text((x, y_offset), text, font=font, fill=color)

    def draw_rounded_button(self, draw, text, center_pos, size=(300, 80), color=None):
        if color is None:
            color = self.colors["accent"]
        
        x, y = center_pos
        w, h = size
        left = x - w // 2
        top = y - h // 2
        right = x + w // 2
        bottom = y + h // 2
        
        draw.rounded_rectangle([left, top, right, bottom], radius=40, fill=color)
        
        font = self.get_font(32)
        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
        except AttributeError:
            tw, th = draw.textsize(text, font=font)
            
        draw.text((x - tw // 2, y - th // 2 - 5), text, font=font, fill=self.colors["white"])

    def paste_product_image(self, canvas, image_path, size=(600, 600), position=None):
        try:
            img = Image.open(image_path).convert("RGBA")
            img.thumbnail(size)
            
            if position is None:
                # Center
                pos_x = (self.width - img.width) // 2
                pos_y = (self.height - img.height) // 2
            else:
                pos_x, pos_y = position
                
            canvas.paste(img, (pos_x, pos_y), img)
        except Exception as e:
            print(f"Error pasting image: {e}")
            # Placeholder box if image fails
            draw = ImageDraw.Draw(canvas)
            draw.rectangle([200, 200, 880, 880], outline=self.colors["accent"], width=5)
            self.draw_text_centered(draw, "Product Image Placeholder", 500, 40)

    def save_frame(self, canvas, filename, output_dir="exports"):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        path = os.path.join(output_dir, filename)
        canvas.save(path, "PNG")
        return path

    def draw_header(self, draw):
        self.draw_text_centered(draw, self.brand_name.upper(), 50, 40, self.colors["accent"])
        draw.line([300, 110, 780, 110], fill=self.colors["accent"], width=2)

    def draw_text_at_pos(self, draw, text, pos, size, color=None, center=True):
        if color is None:
            color = self.colors["text"]
        font = self.get_font(size)
        x, y = pos
        if center:
            try:
                bbox = draw.textbbox((0, 0), text, font=font)
                tw = bbox[2] - bbox[0]
                th = bbox[3] - bbox[1]
                x = x - tw // 2
                y = y - th // 2 - 5 # Small adjustment for baseline
            except AttributeError:
                tw, th = draw.textsize(text, font=font)
                x = x - tw // 2
                y = y - th // 2
        draw.text((x, y), text, font=font, fill=color)

    def generate_frame_1_product_shot(self, product_image_path):
        canvas = self.create_canvas()
        draw = ImageDraw.Draw(canvas)
        self.draw_header(draw)
        self.paste_product_image(canvas, product_image_path, size=(650, 650), position=((self.width-650)//2, 150))
        self.draw_text_centered(draw, self.product_name, 850, 70)
        return canvas

    def generate_frame_2_wellness_benefit(self, benefit_headline):
        canvas = self.create_canvas(self.colors["bg_light"])
        draw = ImageDraw.Draw(canvas)
        self.draw_header(draw)
        
        # Elegant border for wellness frame
        draw.rectangle([50, 150, 1030, 930], outline=self.colors["accent"], width=4)
        
        # Subtitle
        self.draw_text_centered(draw, "HERBAL WELLNESS BLEND", 200, 35, self.colors["accent"])
        
        # Large central text for benefit
        lines = [benefit_headline]
        if len(benefit_headline) > 25:
            # Simple wrapping if headline is long
            words = benefit_headline.split()
            lines = [" ".join(words[:len(words)//2]), " ".join(words[len(words)//2:])]
            
        y = 450
        for line in lines:
            self.draw_text_centered(draw, line, y, 65)
            y += 85
            
        # Small Footer note for compliance
        self.draw_text_centered(draw, "*This product is a dietary supplement and supports general well-being.", 980, 20, (150, 150, 150))
        return canvas

    def generate_frame_3_ingredient_benefit(self, ingredients_with_benefits):
        canvas = self.create_canvas()
        draw = ImageDraw.Draw(canvas)
        self.draw_header(draw)
        
        self.draw_text_centered(draw, "WELLNESS INGREDIENTS", 160, 45, self.colors["accent"])
        
        y = 300
        for ing, ben in ingredients_with_benefits[:4]:
            # Circle for icon
            cx, cy = 180, y + 40
            draw.ellipse([cx-40, cy-40, cx+40, cy+40], fill=self.colors["accent"])
            self.draw_text_at_pos(draw, ing[0].upper(), (cx, cy), 45, self.colors["white"])
            
            self.draw_text_at_pos(draw, ing, (260, y), 45, center=False)
            self.draw_text_at_pos(draw, ben, (260, y + 50), 30, color=(120, 120, 120), center=False)
            y += 160
        return canvas

    def generate_frame_4_how_to_use(self, steps):
        canvas = self.create_canvas(self.colors["bg_light"])
        draw = ImageDraw.Draw(canvas)
        self.draw_header(draw)
        self.draw_text_centered(draw, "HOW TO USE", 180, 55, self.colors["accent"])
        
        y = 350
        for i, (icon_text, instruction) in enumerate(steps[:3]):
            # Step circle
            cx, cy = 200, y + 40
            draw.ellipse([cx-45, cy-45, cx+45, cy+45], outline=self.colors["accent"], width=3)
            # Correctly centered step number
            self.draw_text_at_pos(draw, str(i+1), (cx, cy), 45, self.colors["accent"])
            
            # Instruction text
            self.draw_text_at_pos(draw, instruction, (300, y+20), 40, center=False)
            y += 180
        return canvas

    def generate_frame_5_ingredient_list(self, full_list):
        canvas = self.create_canvas()
        draw = ImageDraw.Draw(canvas)
        self.draw_header(draw)
        self.draw_text_centered(draw, "PURE INGREDIENTS", 180, 55, self.colors["accent"])
        
        y = 350
        for item in full_list:
            self.draw_text_centered(draw, f"• {item}", y, 45)
            y += 80
        return canvas

    def generate_frame_6_offer_solution(self, product_image_path):
        canvas = self.create_canvas()
        draw = ImageDraw.Draw(canvas)
        self.draw_header(draw)
        
        self.paste_product_image(canvas, product_image_path, size=(550, 550), position=((self.width-550)//2, 180))
        
        self.draw_text_centered(draw, self.product_name, 750, 60)
        self.draw_text_centered(draw, f"MRP: {self.price}", 830, 70, self.colors["accent"])
        
        self.draw_rounded_button(draw, "Shop Now", (540, 960))
        return canvas
