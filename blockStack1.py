from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -140
y = 70
z = 244
blockType = 103
mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y + 1, z, blockType)
