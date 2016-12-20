from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

flower = 1

while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, 1)
    mc.setBlock(x+1, y, z-1, 1)
    mc.setBlock(x+2, y, z-1, 1)
    mc.setBlock(x+3, y, z-1, 1)
    mc.setBlock(x+4, y, z-1, 1)
    mc.setBlock(x-1, y, z-1, 1)
    mc.setBlock(x-2, y, z-1, 1)
    mc.setBlock(x-3, y, z-1, 1)
    mc.setBlock(x-4, y, z-1, 1)
    mc.setBlock(x-4, y+1, z, 1)
    mc.setBlock(x-4, y+2, z, 1)
    mc.setBlock(x+4, y+1, z, 1)
    mc.setBlock(x+4, y+2, z, 1)
    sleep(0.01)
