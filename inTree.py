from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

blockType = mc.getBlock(x, y - 1, z)
inTree = blockType == 18 or blockType == 11
mc.postToChat("The player is in a tree: " + str(inTree))
