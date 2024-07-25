from siyi_sdk import SIYISDK


class Mover:
    def __init__(self):
        self.cam = SIYISDK(server_ip="192.168.144.25", port=8554)
        if not self.cam.connect():
            print("No connection ")
            exit(1)

    def rotate(self, x, y):
        self.cam.setGimbalRotation(x, y)

    def center(self):
        self.cam.setGimbalRotation(0, 0)

    def stop(self):
        self.cam.disconnect()


