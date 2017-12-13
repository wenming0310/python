# !/D:/github/PythonTest/TestCode/StarbuzzSupermarket/hfprog_sounds/
import pygame.mixer

sounds = pygame.mixer
sounds.init()

def wait_finish(channel):
    while channel.get_busy():
        pass

s = sounds.Sound("hfprog_sounds/heartbeat.wav")
wait_finish(s.play())
s2 = sounds.Sound("hfprog_sounds/buzz.wav")
wait_finish(s2.play())
s3 = sounds.Sound("hfprog_sounds/buzz.wav")
wait_finish(s3.play())
s4 = sounds.Sound("hfprog_sounds/buzz.wav")
wait_finish(s4.play())