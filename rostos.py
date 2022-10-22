import face_recognition as fr
from reconhecer import reconhece_rosto, cria_rostos

desconhecido = reconhece_rosto('APSREAL\imagens\Marcos.png')
if(desconhecido[0]):
    foto_desconhecido = desconhecido[1][0]
    faces_conhecidos, nomes_faces = cria_rostos()
    resultados = fr.compare_faces(foto_desconhecido,faces_conhecidos)
    print(resultados)

    for i in (range(len(nomes_faces))):
        resultado = resultados[i]
        if (resultado):
            print("Rosto do", nomes_faces[i], "foi reconhecido")


else:
    print("Não foi encontrado nenhum rosto")