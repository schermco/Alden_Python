from mcpi.minecraft import Minecraft
mc = Minecraft.create()
message = "Alden, this was sent via a variable."
mc.postToChat(message)
