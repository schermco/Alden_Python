from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

height = 2
blockType = 1

#spire sildes: should be the same as height

sideHeight = height
mc.setBlocks(x + 1, y, z + 1, x + 3, y + sideHeight - 1 , z + 3, blockType)

# spire point: should be 2 times height
pointHeight = height * 2
mc.setBlocks(x + 2, y, z + 2, x + 2, y + pointHeight - 1 , z + 2, blockType)

#spire base: should be half the height

baseHeight = height / 2
mc.setBlocks(x, y, z, x + 4, y + baseHeight - 1 , z + 4, blockType)
