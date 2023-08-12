import os, random
from typing import List
from PIL import Image
from layer import Layer

class DragonGenerator:
    
    def __init__(self, images_path: str):
        self.layers: List[Layer] = self.load_image_layers(images_path)
        self.background_color = (120,150,180)
        self.output_path: str = "./output"  
        os.makedirs(self.output_path, exist_ok = True)


    #images_path = "png"
    def load_image_layers(self, images_path: str):
        sub_paths = [d for d in sorted(os.listdir(images_path)) if os.path.isdir(os.path.join(images_path, d))]
        layers : List[Layer] = []
        for sub_path in sub_paths:
            layers_path = os.path.join(images_path, sub_path)
            layer = Layer(layers_path)
            layers.append(layer)

        return layers


        
    def generate_image_sequence(self):
        image_path_sequence = []
        for layer in self.layers:
            if layer.should_generate():
                image_path = layer.get_random_image_path_rarity()
                image_path_los= image_path[0]
                image_path_sequence.append(image_path_los)
        print(image_path_sequence)
        return image_path_sequence

    def rander_dragon_image(self, image_path_sequence: List[str]):
        #background image
        folder = r"./background"
        a = random.choice([f for f in os.listdir(folder) if f.endswith(".png") and not f.startswith(".")])
        file = folder+'/'+a

        bg_image = Image.open(file)

        for image_path in image_path_sequence:
            layer_image = Image.open(image_path)
            layer_image = layer_image.resize(bg_image.size)
            bg_image = Image.alpha_composite(bg_image,layer_image)

        return bg_image


    def rarity_sum(self):
        rarity_sum = 0
        total_layers = 0
        for layer in self.layers:
            if layer.should_generate():
                image_rarity_path = layer.get_random_image_path_rarity()
                image_rarity = float(image_rarity_path[1])
                rarity_sum += image_rarity
                total_layers += 1
        if total_layers == 0:
            return 0  # Return a default value or handle this case appropriately
        return rarity_sum / total_layers


    def save_image(self, bg_image: Image.Image, i: int = 0):
        image_index = str(i).zfill(4)
        rarity = round(self.rarity_sum(),3)
        image_file_name = f"dragon_{image_index}_{rarity}.png"
        image_save_path = os.path.join(self.output_path,image_file_name)
        bg_image.save(image_save_path)

    def generate_dragon(self, n: int =1):        
        print("DragonGenerator: Generating Dragon!")
        for i in range(n):
            image_path_sequence = self.generate_image_sequence()
            image = self.rander_dragon_image(image_path_sequence)
            self.save_image(image,i)
