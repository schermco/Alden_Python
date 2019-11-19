from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

blockType = mc.getBlock(x, y, z)
notAir = blockType == 0
mc.postToChat("The player is not standing in air: " + str(notAir))
