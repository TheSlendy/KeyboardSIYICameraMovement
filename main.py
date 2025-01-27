from siyi_sdk import SIYISDK
import keyboard


class Mover:
    def __init__(self):
        self.cam = SIYISDK(server_ip="192.168.144.25")
        self.speed = 30
        if not self.cam.connect():
            print("No connection ")
            exit(1)

    def move(self, yaw, pitch):
        self.cam.requestGimbalSpeed(yaw, pitch)

    def listener(self):
        while True:
            if keyboard.is_pressed("up"):
                self.move(0, self.speed)
            if keyboard.is_pressed("down"):
                self.move(0, -self.speed)
            if keyboard.is_pressed("left"):
                self.move(-self.speed, 0)
            if keyboard.is_pressed("right"):
                self.move(self.speed, 0)
            if keyboard.is_pressed("c"):
                self.cam.requestCenterGimbal()
            self.move(0, 0)


mover = Mover()
mover.listener()
