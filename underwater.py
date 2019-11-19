from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

blockType = mc.getBlock(x, y, z)
blockType2 = mc.getBlock(x, y + 1, z)
underwater = blockType == 9 and blockType2 == 9
mc.postToChat("The player is underwater: " + str(underwater))
