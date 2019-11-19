from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

blockType = mc.getBlock(x, y, z)
mc.postToChat(blockType == 0)
