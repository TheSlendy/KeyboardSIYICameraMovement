import cv2
from camera_mover import Mover


def track_people():
    mover = Mover()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    yaw, pitch = 0, 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        square = 0
        face_index, i = 0, 0
        for (x, y, w, h) in faces:
            if w * h > square:
                face_index = i
            i += 1
        x, y, w, h = faces[face_index]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 127, 255), 2)

        if x < cap.get(3) - w / 2:
            yaw -= 5
        elif x > cap.get(3) + w / 2:
            yaw += 5
        if y < cap.get(4) - h / 2:
            pitch -= 3
        elif y > cap.get(4) + h / 2:
            pitch += 3
        mover.rotate(yaw, pitch)

        if abs(yaw) > 60:
            mover.center()
            yaw = 0
            pitch = 0

        cv2.imshow('Face tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    track_people()
