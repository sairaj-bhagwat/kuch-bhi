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

    def generate_frame_1_product_shot(self, product_image_path):
        canvas = self.create_canvas()
        draw = ImageDraw.Draw(canvas)
        self.draw_header(draw)
        self.paste_product_image(canvas, product_image_path, size=(700, 700))
        self.draw_text_centered(draw, self.product_name, 850, 60)
        return canvas

    def generate_frame_2_wellness_benefit(self, benefit_headline):
        canvas = self.create_canvas(self.colors["bg_light"])
        draw = ImageDraw.Draw(canvas)
        self.draw_header(draw)
        
        # Central square for visual
        draw.rectangle([200, 200, 880, 700], fill=self.colors["white"], outline=self.colors["accent"])
        self.draw_text_centered(draw, "Wellness Focus", 400, 40, (180, 180, 180))
        
        self.draw_text_centered(draw, benefit_headline, 800, 50)
        return canvas

    def generate_frame_3_ingredient_benefit(self, ingredients_with_benefits):
        canvas = self.create_canvas()
        draw = ImageDraw.Draw(canvas)
        self.draw_header(draw)
        
        y = 250
        for ing, ben in ingredients_with_benefits[:4]:
            # Simple icon placeholder
            draw.ellipse([150, y, 210, y+60], fill=self.colors["accent"])
            font_bold = self.get_font(40)
            font_reg = self.get_font(30)
            draw.text((250, y), ing, font=font_bold, fill=self.colors["text"])
            draw.text((250, y + 45), ben, font=font_reg, fill=(100, 100, 100))
            y += 180
        return canvas

    def generate_frame_4_how_to_use(self, steps):
        canvas = self.create_canvas(self.colors["bg_light"])
        draw = ImageDraw.Draw(canvas)
        self.draw_header(draw)
        self.draw_text_centered(draw, "HOW TO USE", 180, 45, self.colors["accent"])
        
        y = 300
        for i, (icon_text, instruction) in enumerate(steps[:3]):
            # Step circle
            draw.ellipse([150, y, 250, y+100], outline=self.colors["accent"], width=3)
            self.draw_text_centered(draw, str(i+1), y+25, 50, self.colors["accent"]) # Approximate centering
            
            draw.text((300, y+30), instruction, font=self.get_font(35), fill=self.colors["text"])
            y += 200
        return canvas

    def generate_frame_5_ingredient_list(self, full_list):
        canvas = self.create_canvas()
        draw = ImageDraw.Draw(canvas)
        self.draw_header(draw)
        self.draw_text_centered(draw, "PURE INGREDIENTS", 180, 50, self.colors["accent"])
        
        text = "\n".join(full_list)
        # Use draw_text_centered variant for multiline if needed, but here we just list
        y = 300
        font = self.get_font(40)
        for item in full_list:
            bbox = draw.textbbox((0, 0), item, font=font)
            tw = bbox[2] - bbox[0]
            draw.text(((self.width - tw)//2, y), item, font=font, fill=self.colors["text"])
            y += 70
        return canvas

    def generate_frame_6_offer_solution(self, product_image_path):
        canvas = self.create_canvas()
        draw = ImageDraw.Draw(canvas)
        self.draw_header(draw)
        
        self.paste_product_image(canvas, product_image_path, size=(500, 500), position=(290, 200))
        
        self.draw_text_centered(draw, self.product_name, 720, 55)
        self.draw_text_centered(draw, f"Price: {self.price}", 800, 65, self.colors["accent"])
        
        self.draw_rounded_button(draw, "Shop Now", (540, 950))
        return canvas
