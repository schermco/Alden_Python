import time
import math
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

time.sleep(5)
mc.postToChat("Go!")

position1 = mc.player.getTilePos()
x1 = position1.x
y1 = position1.y
z1 = position1.z

time.sleep(10)

position2 = mc.player.getTilePos()
x2 = position2.x
y2 = position2.y
z2 = position2.z

distanceX = x2 - x1
distanceY = y2 - y1
distanceZ = z2 - z1

distance2D = math.sqrt(distanceX ** 2 + distanceZ ** 2)

mc.postToChat("I've traveled X: " + str(distanceX) + " distance, and Y: " + str(distanceY) + " distance, and Z: " + str(distanceZ) + " distance.")
mc.postToChat("I've also traveled " + str(distance2D) + " distance diagonally.")
