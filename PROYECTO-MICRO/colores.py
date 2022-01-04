import cv2
import numpy as np


def dibujar(mask,color):
  _,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE)
  for c in contornos:
    area = cv2.contourArea(c)
    if area > 3000:
      M = cv2.moments(c)
      if (M["m00"]==0): M["m00"]=1
      x = int(M["m10"]/M["m00"])
      y = int(M['m01']/M['m00'])


      nuevoContorno = cv2.convexHull(c)
      cv2.circle(frame,(x,y),7,(0,255,0),-1)
      cv2.putText(frame,'{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)

      cv2.drawContours(frame, [nuevoContorno], 0, color, 3)

      cv2.putText(frame ,'SELECCIONADOR DE JITOMATE',(10,30),0,1,(255,255,255),2)

  _,cnts1,_ = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE)
   
  for c in cnts1:
    area1 = cv2.contourArea(c)
    if area1 > 3000:
      
      a = cv2.contourArea(c)
      distance = 2*(10**(-7))* (a**2) - (0.0067 * a) + 83.487

      M =cv2.moments(c)
      x = int(M["m10"] / M["m00"])
      y = int(M["m01"] / M["m00"])
 
      image=cv2.imread('/home/pi/PROYECTO/VERDE.jpeg')
      cv2.imshow('Imagen',image)
      
      S= 'AREA: ' + str(a)
      cv2.putText(frame, S, (x-60, y-60),0, 1, (0,255,0), 2)
      

      if a>=3400 and a<=11330:
          cv2.putText(frame, "CHICO", (x-100, y-100),0, 1, (0,255,0), 2)

      if a>=12000 and a<=16300:
          cv2.putText(frame, "MEDIANO", (x-130, y-130),0, 1, (0,255,0), 2)
      
      if a>=18000 and a<=28000:
          cv2.putText(frame, "GRANDE", (x-160, y-160),0, 1, (0,255,0), 2)
      else:
         cv2.putText(frame, "", (x-120, y-120),0, 1, (0,255,0), 2)

      cv2.putText(frame, "VERDE      CAJA3", (x-20, y-20),0, 1, (0,255,0), 2)
     


  _,cnts2,_ = cv2.findContours(maskNaranja, cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE)

  for c in cnts2:
    area2 = cv2.contourArea(c)
    
    if area2 > 3000:
      
      a1 = cv2.contourArea(c)
      distance = 2*(10**(-7))* (a1**2) - (0.0067 * a1) + 83.487
      
      M =cv2.moments(c)
      x = int(M["m10"] / M["m00"])
      y = int(M["m01"] / M["m00"])
      
      image=cv2.imread('/home/pi/PROYECTO/NARANJA.jpeg')
      cv2.imshow('Imagen',image)

      S2= 'AREA: ' + str(a1)
      cv2.putText(frame, S2, (x-60, y-60),0, 1, (20,117,240), 2)

      if a1>=3400 and a1<=11330:
          cv2.putText(frame, "CHICO", (x-160, y-160),0, 1, (20,117,240), 2)

      if a1>=12000 and a1<=16300:
          cv2.putText(frame, "MEDIANO", (x-130, y-130),0, 1, (20,117,240), 2)
    
      if a1>=18000 and a1<=28000:
          cv2.putText(frame, "GRANDE", (x-100, y-100),0, 1, (20,117,240), 2)
    
      else:
         cv2.putText(frame, "", (x-120, y-120),0, 1, (20,117,240), 2)

      cv2.putText(frame, "NARANJA      CAJA2", (x-20, y-20),0 , 1, (20,117,240), 2)
     

  _,cnts3,_ = cv2.findContours(maskRed1, cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE)

  for c in cnts3:
    area3 = cv2.contourArea(c)
    if area3 > 3000:
      
      a2 = cv2.contourArea(c)
      distance = 2*(10**(-7))* (a2**2) - (0.0067 * a2) + 83.487

      M =cv2.moments(c)
      x = int(M["m10"] / M["m00"])
      y = int(M["m01"] / M["m00"])
      image=cv2.imread('/home/pi/PROYECTO/ROJO.jpeg')
      cv2.imshow('Imagen',image)

      S3= 'AREA: ' + str(a2)
      cv2.putText(frame, S3, (x-60, y-60),0, 1, (0,0,255), 2)

      if a2>=18000 and a2<=28000:
          cv2.putText(frame, "GRANDE", (x-100, y-100),0, 1, (0,0,255), 2)

      if a2>=12000 and a2<=16300:
          cv2.putText(frame, "MEDIANO", (x-130, y-130),0, 1, (0,0,255), 2)
      
      if a2>=3400 and a2<=11330:
          cv2.putText(frame, "CHICO", (x-160, y-160),0, 1, (0,0,255), 2)
      else:
         cv2.putText(frame, "", (x-120, y-120),0, 1, (0,0,255), 2)

      cv2.putText(frame, "ROJO         CAJA1", (x-20, y-20),0 , 1, (0,0,255), 2)
     

  _,cnts4,_ = cv2.findContours(maskRed2, cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE)

  for c in cnts4:
    area4 = cv2.contourArea(c)
    if area4 > 3000:
      
      a3 = cv2.contourArea(c)
      distance = 2*(10**(-7))* (a3**2) - (0.0067 * a3) + 83.487

      M =cv2.moments(c)
      x = int(M["m10"] / M["m00"])
      y = int(M["m01"] / M["m00"])
      image=cv2.imread('/home/pi/PROYECTO/ROJO.jpeg')
      cv2.imshow('Imagen',image)

      S4= 'AREA: ' + str(a3)
      cv2.putText(frame, S4, (x-60, y-60),0, 1, (0,0,255), 2)

      if a2>=18000 and a2<=28000:
          cv2.putText(frame, "GRANDE", (x-100, y-100),0, 1, (0,0,255), 2)

      if a2>=12000 and a2<=16300:
          cv2.putText(frame, "MEDIANO", (x-130, y-130),0, 1, (0,0,255), 2)
      
      if a2>=3400 and a2<=11330:
          cv2.putText(frame, "CHICO", (x-160, y-160),0, 1, (0,0,255), 2)
      else:
         cv2.putText(frame, "", (x-120, y-120),0, 1, (0,0,255), 2)    

      cv2.putText(frame, "ROJO         CAJA1", (x-20, y-20),0 , 1, (0,0,255), 2)
      


      

cap = cv2.VideoCapture(0)

verdeBajo = np.array([35,100,20],np.uint8)
verdeAlto = np.array([65,255,255],np.uint8)

naranjaBajo = np.array([11,100,20],np.uint8)
naranjaAlto = np.array([20,255,255],np.uint8)

redBajo1 = np.array([0,100,20],np.uint8)
redAlto1 = np.array([10,255,255],np.uint8)

redBajo2 = np.array([175,100,20],np.uint8)
redAlto2 = np.array([179,255,255],np.uint8)
  



font = cv2.FONT_HERSHEY_SIMPLEX
while True:

    ret,frame = cap.read()
    
    if ret == True:
      frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

      maskVerde = cv2.inRange(frameHSV,verdeBajo,verdeAlto)
      maskNaranja = cv2.inRange(frameHSV,naranjaBajo,naranjaAlto)
      maskRed1 = cv2.inRange(frameHSV,redBajo1,redAlto1)
      maskRed2 = cv2.inRange(frameHSV,redBajo2,redAlto2)
      

      maskRed = cv2.add(maskRed1,maskRed2)

      dibujar(maskVerde,(0,255,0))
      dibujar(maskNaranja,(20,117,240))
      dibujar(maskRed,(0,0,255))
      
      cv2.imshow('frame',frame)

    
      
      if cv2.waitKey(1) & 0xFF == ord('s'):
            break


         
cap.release()
cv2.destroyAllWindows()
