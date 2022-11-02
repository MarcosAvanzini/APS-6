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

    Administrador = reconhece_rosto("APSREAL\imagens\Marcos1.jpg")
    if (Administrador[0]):
        faces_conhecidas.append(Administrador[1][0])
        nomes_faces.append("Administrador")

    Operario = reconhece_rosto("APSREAL\imagens\Captura de tela 2022-10-31 161711.jpg")
    if (Operario[0]):
        faces_conhecidas.append(Operario[1][0])
        nomes_faces.append("Operario")
    
    Gerente = reconhece_rosto("APSREAL\imagens\Captura de tela 2022-11-01 184759.jpg")
    if (Gerente[0]):
        faces_conhecidas.append(Gerente[1][0])
        nomes_faces.append("Gerente")

    return faces_conhecidas, nomes_faces