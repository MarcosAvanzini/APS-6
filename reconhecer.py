from xml.sax.handler import feature_namespaces
import face_recognition as fr



def reconhece_rosto(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if (len(rostos) > 0):
        return True, rostos
    
    return False, []

def cria_rostos():
    faces_conhecidas = []
    nomes_faces = []

    Marcos1 = reconhece_rosto("APSREAL\imagens\Marcos1.jpg")
    if (Marcos1[0]):
        faces_conhecidas.append(Marcos1[1][0])
        nomes_faces.append("Marcos1")

    Marcos2 = reconhece_rosto("APSREAL\imagens\Marcos2.jpg")
    if (Marcos2[0]):
        faces_conhecidas.append(Marcos2[1][0])
        nomes_faces.append("Marcos2")
    
    return faces_conhecidas, nomes_faces