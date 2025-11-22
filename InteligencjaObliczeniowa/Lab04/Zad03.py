import os

import cv2
import numpy as np

def iterate_images(folder_path = "bird_miniatures"):
    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)
        img = cv2.imread(image_path)

        img = img.astype('uint8')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)

        img_eq = cv2.equalizeHist(gray)

        blur = cv2.GaussianBlur(enhanced, (5, 5), 0)

        thresh = cv2.adaptiveThreshold(blur, 255,
                                       cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY_INV,
                                       blockSize=5, C=2)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
        clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        contours, _ = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        min_area = 7
        max_area = 50
        small_blobs = [cnt for cnt in contours if min_area <= cv2.contourArea(cnt) <= max_area]

        output = img.copy()

        cv2.drawContours(output, small_blobs, -1, (0, 0, 255), 1)

        cv2.imshow("Detected blobs", output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        bird_count = len(small_blobs)
        print("Number of birds detected:", bird_count)

iterate_images()