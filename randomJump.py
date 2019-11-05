from mpci.minecraft import Minecraft
mc = Minecraft.create()
import random

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x = x + random.randint(-10, 10)
y = y + random.randint(-5, 5)
z = z * random.randint(-3, 3)
mc.player.setPos(x, y, z)
