# Dragon-NFTs Generator

## Overview
Dragon-NFTs Generator is a Python-based tool designed to generate unique and vibrant backgrounds and assemble distinct parts of a Dragon to produce a comprehensive NFT-ready artwork. NFTs (Non-fungible Tokens) have opened up new avenues for digital artists to represent and monetize their artworks. However, the consistent and large-scale generation of these NFTs can be demanding. This generator uses generative coding techniques to expedite this process.

## Dependencies
Python: The primary programming language used.
Pillow (PIL): A Python Imaging Library used for handling image-based operations.
```
pip3 install pillow
```



## Features
1. Background Generator (bg_generator.py):

* Generates an abstract background using connected lines of varying thickness and colors.
* Colors are determined using the HSV color model with random generation techniques to ensure uniqueness.

2. Dragon Generator: (Not included in provided code)

* Assembles various components of a dragon illustration.
* Uses artist-made segments of dragon components to generate a complete image.
* Takes into consideration the rarity and color variations of each dragon part.
* Uses Pillow's alpha_composite function to merge layers.

3. Rarity Algorithm: Assigns rarity weights to different components of the artwork to create NFTs with varying levels of rarity.

## Workflow
1. Art Piece Preparation:

* Dragon Illustration:
    * The dragon, a symbol rich in cultural significance and a hit among the younger generation, is chosen as the subject.
    * It's first sketched and then split into ten different parts like the horn, scales, etc.
    * These segments are colored differently and named as Bodypart_Color (e.g., Horn_Blue).
2. NFTs Generator Coding:
* Background Generator:

    * Generates backgrounds with algorithmically drawn, connected lines with changing colors and thicknesses.
    * Uses random_color() to initialize colors and an interpolation function to achieve smooth transitions.
* Dragon Generator:

    * Assembles dragon parts from the drawings.
    * Each part's rarity is determined using a random weighting system, ensuring diverse outputs.
    * Uses Python's Pillow package to combine different layers, resulting in the final artwork.
3. NFT Creation:
* With the generated art pieces, you can mint them into NFTs using platforms like OpenSea.



## How to Use
1. Run the bg_generator.py to generate ten unique backgrounds:
    ```
    python bg_generator.py
    ```

2. Use the Dragon Generator (not provided) to assemble various components and produce the final dragon NFT artwork.
    ```
    python generate_dragon.py
    ```


## About the Author
An individual artist exploring the exciting realm of NFTs. Apart from being an artist, also passionate about blogging, photography, diving, and being a foodie. Has a keen interest in understanding and demystifying the world of blockchain and NFTs. Believes in continuous learning and staying updated with the ever-evolving digital world.


## Future Steps:
1. Integrate with platforms like OpenSea to automate the minting process.
2. Add more customization options for the generated artworks, such as AI generator. 
3. Refine the rarity algorithm to add more nuances to art piece differentiation.




## Contributing:
We welcome contributions! Please create a new issue if you have ideas or submit a PR if you have improvements to propose.

## Disclaimer
NFTs are a new frontier in the art world. While this project aims to facilitate the creation process, artists are encouraged to explore, learn more about the blockchain, and understand the NFT market's nuances.