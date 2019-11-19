from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
width = 10
height = 5
length = 6
blockType = 4
air = 0

buildX = x - 20
buildY = y
buildZ = z - 20

mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)

mc.setBlocks(x + 1, y + 1, z +1, x + width, y + height - 1, z + length - 1, air)

inside = buildX < x < buildX + width and buildY < y < buildY + height and buildZ < z < buildZ + length

mc.postToChat("I'm inside: " + str(inside))

