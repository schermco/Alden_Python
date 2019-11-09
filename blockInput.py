from mcpi.minecraft import Minecraft
mc = Minecraft.create()
blockType = input("Select a block type: ")
blockType = int(blockType)
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

mc.setBlock(x, y, z, blockType)
