import cv2
import requests
import io

img = cv2.imread("img.jpg")   # or file, Path, PIL, OpenCV, numpy, list

data = { 'image': img.tolist()}
url = "http://127.0.0.1:5000"
response = requests.post(url, json=data).json()
print(response["bbox"])
print(response["class"])
