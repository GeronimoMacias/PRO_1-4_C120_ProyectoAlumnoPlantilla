import cv2
import time
import math
#Actividad 1
#declara p1 y p2
p1 = 
p2 = 

xs = []
ys = []

video = cv2.VideoCapture("footvolleyball.mp4")
#Cargar rastreador 
tracker = cv2.TrackerCSRT_create()

#lee el primer fotograma del vídeo
success,img = video.read()

#selecciona el cuadro delimitador de la imagen
bbox = cv2.selectROI("Rastreando",img,False)

#inicializa el rastreador en el img y el cuadro delimitador
tracker.init(img,bbox)

def goal_track(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1 = x + int(w/2)
    c2 = y + int(h/2)

    #Actividad 2
    #Descomenta el código correcto 
    #cv2.circle(img,(c1,c2),2,(0,0,255),5)
    #cv2.circle(img,(c2,c1),2,(0,5,255),0)
    #cv2.circle(img,(c2,c1),2,(0,0,255),5)
    #cv2.circle(img,(c1,c2),2,(0,5,255),0)

    cv2.circle(img,(int(p1),int(p2)),2,(0,255,0),3)
    dist = math.sqrt(((c1-p1)**2) + (c2-p2)**2)
    print(dist)

    if(dist<=20):
        cv2.putText(img,"Canasta",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    xs.append(c1)
    ys.append(c2)

    for i in range(len(xs)-1):
        cv2.circle(img,(xs[i],ys[i]),2,(0,0,255),5)

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"Rastreando",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)


while True:
    check,img = video.read()   
    success,bbox = tracker.update(img)

    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img,"Perdido",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    #Actividad 3
    #llamar a la función de seguimiento de canasta

    cv2.imshow("resultado",img)
            
    key = cv2.waitKey(1)
    if key == ord('q'):
        print("Cerrando")
        break

video.release()
cv2.destroyALLwindows() 
