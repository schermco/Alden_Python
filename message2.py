from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("Hello, Alden!  Slappy says hello!")
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
mc.postToChat("I'm currently at X: " + str(x) + " and at Y: " + str(y) + " and at Z: " + str(z))
