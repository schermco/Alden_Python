from mcpi.minecraft import Minecraft
mc = Minecraft.create()
username = input("Enter your username: ")
message = input("Enter your message here:")
mc.postToChat(username + ": " + message)
