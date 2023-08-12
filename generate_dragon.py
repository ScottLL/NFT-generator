from dragon_generator import DragonGenerator
# from bg_generator import BackGround
def generate_dragon():
    generator = DragonGenerator("png")
    generator.generate_dragon(50)
    
# def background():
#     background = BackGround()
#     background.generate_art(f"test_image.png")

if __name__ == "__main__":
    generate_dragon() 
    # for i in range(2):
    #     background = BackGround()
    #     background.generate_art(f"test_image_{i}.png")
    