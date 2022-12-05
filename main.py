#pip install opencv-python
#python3 -m pip install opencv-python
import cv2

def camera():
    # Включаем первую камеру
    cap = cv2.VideoCapture(0)

    # "Прогреваем" камеру, чтобы снимок не был тёмным
    #for i in range(5):
    #   cap.read()
    [cap.read() for i in range(5)]
    # Делаем снимок
    ret, frame = cap.read()

    # Записываем в файл
    cv2.imwrite('cam.png', frame)

    # Отключаем камеру
    cap.release()

print('start')
camera()