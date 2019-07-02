import RPi.GPIO as GPIO
import time
from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2
import http.client, urllib, base64
import json

# initialize the video streams and allow them to warmup
print("[INFO] starting cameras...")
#vs = VideoStream(src=0).start()
cap = cv2.VideoCapture(0)
cap.set(3, 360)
cap.set(4, 240)

try:
	while True:
		ret, frame = cap.read()
		cv2.imshow('frame',frame)
        #cv2.imwrite('/home/pi/logs/test6.jpg',frame)

		k=cv2.waitKey(1) & 0xFF
		if k == 48:
			print("break")
			break
		elif k== 49:
			cv2.imwrite('/home/pi/logs/test6_1.jpg',frame)
			img = cv2.imread('/home/pi/logs/test6_1.jpg')
			cv2.imshow('snapshop',img)
			f = open('/home/pi/logs/test6_1.jpg', 'rb')
			jpgdata = f.read()
			f.close()
			
			# Request header
			headers = {
			# Request headers
			'Content-Type': 'application/octet-stream',
			'Ocp-Apim-Subscription-Key': '3364b122b6784ef49c81bc61d6bc2595',
			}

			params = urllib.parse.urlencode({
			# Request parameters
			'returnFaceId': 'true',
			'returnFaceLandmarks': 'false',
			'returnFaceAttributes': 'age,gender,smile,facialHair,headPose,glasses',
			})

			body = {
			# Request body
			#'url': image_url

			}

			try:
				conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
				#conn.request("POST", "/face/v1.0/detect?%s" % params, json.dumps(body), headers)
				conn.request("POST", "/face/v1.0/detect?%s" % params, jpgdata, headers)
				response = conn.getresponse()
				data = json.loads(response.read().decode('utf-8'))
				print(json.dumps(data, indent=4))
				a = data[0]['faceAttributes']['gender']
				print(data[0]['faceAttributes']['gender'])
				conn.close()
				text = a
				#y = startY - 10 if startY - 10 > 10 else startY + 10
				cv2.rectangle(img, (data[0]['faceRectangle']['top'], data[0]['faceRectangle']['left']), (data[0]['faceRectangle']['top']+data[0]['faceRectangle']['height'], data[0]['faceRectangle']['left']+data[0]['faceRectangle']['width']),
					(0, 0, 255), 2)
				cv2.putText(img, text, (0, 0),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
				cv2.imshow('result',img)
			except Exception as e:
				print("[Errno {0}] {1}".format(e.errno, e.strerror))
				cv2.destroyAllWindows()

except KeyboardInterrupt:
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()

