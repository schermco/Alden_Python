from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = -139
y = 71
z = 245

mc.player.setTilePos(x, y, z)

time.sleep(10)

x = -129
y = 70
z = 252

mc.player.setTilePos(x, y, z)
