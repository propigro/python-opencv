import cv2

for i in range(1, 6):
    rasm = cv2.imread(f"rasm{i}.jpg")
    oqqora = cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
    cv2.imshow(f"Oq qora {i}", oqqora) 

cv2.waitKey(0)
cv2.destroyAllWindows() 
