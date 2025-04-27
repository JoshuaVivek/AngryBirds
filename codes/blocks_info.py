from blocks_class import * 

def initiate_blocks():
    if __name__ == "__main__":
        # Define images for different health ranges for each block type
        
        # Wood block images
        wood_images = {
            range(0, 30): "images\wood__(30_0).png",
            range(30, 70): "images\wood__(70_30).png",
            range(70, 100): "images\wood__(100_70).png"
        }
        
        # Stone block images
        stone_images = {
            range(0, 30): "images\stone__(30_0).png",
            range(30, 70): "images\stone__(70_30).png",
            range(70, 100): "images\stone__(100_70).png"
        }
        
        # Ice block images
        ice_images = {
            range(0, 30): "images\ice__(30_0).png",
            range(30, 70): "images\ice__(70_30).png",
            range(70, 100): "images\ice__(100_70).png"
        }
        
        # Create instances of each block type
        wood_block = Block(block_type="wood", max_health=100, images=wood_images)
        stone_block = Block(block_type="stone", max_health=100, images=stone_images)
        ice_block = Block(block_type="ice", max_health=100, images=ice_images)
        
