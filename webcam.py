import numpy as np
import face_recognition as fr
import cv2
from reconhecer import cria_rostos

faces_conhecidos, nomes_faces = cria_rostos()

captura_video = cv2.VideoCapture(1)
while True:
    ret, frame = captura_video.read()
    rgb_frame = frame [:,:,::-1]
    localiza_face = fr.face_locations(rgb_frame)
    face_encondings = fr.face_encodings(rgb_frame,localiza_face)

    for (top, right, bottom, left), face_encondings in zip(localiza_face, face_encondings):
        resultados = fr.compare_faces(face_encondings,faces_conhecidos)
        print(resultados)

        distancia = fr.face_distance(faces_conhecidos, face_encondings)

        melhor_resultado = np.argmin(distancia)
        if resultados[melhor_resultado]:
            nome = nomes_faces[melhor_resultado]
            if nome == "Administrador":
                print("Acesso concedido ao Adminstrador")
            if nome == "Operario":
                print("Acesso concedido ao Operario")
            if nome == "Gerente":
                print("Acesso concedido ao Gerente")
        else:
            nome = "desconhecido"


        cv2.rectangle(frame, (left,top), (right,bottom),(0,0,255), 2)

        cv2.rectangle(frame, (left,bottom - 35), (right,bottom),(0,0,255), cv2.FILLED)
        fonte = cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(frame, nome, (left + 7, bottom - 7),fonte,0.55,(255,255,255), 1)

        cv2.imshow('Webcam_facerecognition', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura_video.release()
cv2.destroyAllWindows()