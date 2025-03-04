import cv2
import numpy as np
from keras.models import load_model

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    h, w, _ = frame.shape[:3]

    w_center = w//2
    h_center = h//2

    cv2.rectangle(frame, (w_center-71, h_center-71), (w_center+71, h_center+71), (255, 0, 0))
    cv2.imshow("frame", frame)

    k = cv2.waitKey(1)

    if k == ord("q"):
        break

    elif k == ord("s"):
        im = frame[h_center-70:h_center+70, w_center-70:w_center+70]
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        _, th = cv2.threshold(im, 0, 255, cv2.THRESH_OTSU)
        th = cv2.bitwise_not(th)
        th = cv2.GaussianBlur(th, (9, 9), 0)
        cv2.imwrite("img/capture.jpg", th)
        break


cap.release()
cv2.destroyAllWindows()

Xt = []
img = cv2.imread("img/capture.jpg", 0)
img = cv2.resize(img, (28, 28), cv2.INTER_CUBIC)

Xt.append(img)
Xt = np.array(Xt)/255

model = load_model("MNIST.h5")

result = model.predict_classes(Xt)
print(result[0])
