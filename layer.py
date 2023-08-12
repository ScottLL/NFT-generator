import os
import random
from typing import List



class Layer:
    def __init__ (self, path: str):
        self.path = path
        self.rarity: float = 1.0
    

    def randomweight(self):

        rarity_weight = {}
        randomlist = []
        image_file_names = os.listdir(self.path)
        #generate random number from 1-30 for each file. 
        for i in range(0,len(image_file_names)):
            n = random.randint(1,30)
            randomlist.append(n)
        # sum of all the random number in that file
        sum_weight = sum(randomlist)          
        # Calculate rarity 
        weights = [e/sum_weight for e in randomlist] 
        rarity_weight['image_file_names'] = image_file_names
        rarity_weight['weight'] = weights
        return image_file_names, weights




    def get_random_image_path_rarity(self):
        randomweight = self.randomweight()
        random_image_file_name = random.choice(random.choices(randomweight[0], weights = randomweight[1],k = 1))
        index_rarity = [ i for i, elem in enumerate(randomweight[0]) if random_image_file_name in elem][0]
        weight_list = randomweight[1]
        weight_list_length = len(weight_list)
        rarity_rate = str(weight_list[index_rarity])
        random_path = os.path.join(self.path, random_image_file_name)
        path_rarity = [random_path, rarity_rate,weight_list_length]
        return path_rarity






    def should_generate(self) -> bool:
        return random.random() < self.rarity
