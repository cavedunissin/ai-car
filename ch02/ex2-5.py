import cv2

img = cv2.imread('./example.png')
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
