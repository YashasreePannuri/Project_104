import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mercury",
            (110,193),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (190,252),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Earth",
            (280,176),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mars",
            (380,252),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Jupiter",
            (500,104),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Saturn",
            (800,324),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Neptune",
            (957,140),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Uranus",
            (1115,290),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,255,255))

cv2.imshow("output" , img)
cv2.waitKey(0)

cv2.imwrite("Solar.jpg" , img)