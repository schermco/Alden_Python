from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#position = mc.player.getTilePos()
x = 10
y = 11
z = 12

melon = 103
block = mc.getBlock(x, y, z)
noMelon = block != melon
mc.postToChat("You need to get some food: " + str(noMelon))
