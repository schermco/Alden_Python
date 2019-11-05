from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -148
y = 70
z = 239
blockType = 103
mc.setBlock(x, y, z, blockType)
y = y + 1
mc.setBlock(x, y, z, blockType)
