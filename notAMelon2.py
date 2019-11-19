from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

melon = 103
block = mc.getBlock(x, y - 1, z)
noMelon = block != melon
mc.postToChat(str(block))
mc.postToChat("You need to get some food: " + str(noMelon))
