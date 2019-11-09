from mcpi.minecraft import Minecraft
mc = Minecraft.create()
message = input("Enter your message here:")
mc.postToChat(message)
