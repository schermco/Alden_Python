from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
try:
    blockType = int(input("Select a block type: "))
#blockType = int(blockType)
    mc.setBlock(x, y, z, blockType)
except:
    mc.postToChat("A number is required.  Please try again next time.")
