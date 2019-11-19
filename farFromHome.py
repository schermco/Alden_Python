from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import math

homeX = 10
homeZ = 10

position = mc.player.getTilePos()
x = position.x
#y = position.y
z = position.z

distance = math.sqrt((homeX - x) ** 2 + (homeZ - z) ** 2)

mc.postToChat("I'm this far from home: " + str(distance))
