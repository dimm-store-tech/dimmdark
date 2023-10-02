from django.shortcuts import render
import os
import whisper
from  django.core.files.storage import FileSystemStorage

from server.settings import MEDIA_ROOT
from .functions.Openai import openaiResponse
# Create your views here.
def indexView(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    
    if request.method == 'POST' and 'file' in request.FILES:
        text_prompt = str(request.POST['text_promt'])
        file = request.FILES['file']
        fs=FileSystemStorage()
        file = fs.save(file.name,file)
        model = whisper.load_model("base")
        file_path = os.path.join(MEDIA_ROOT, file)
        file_path = file_path.replace("\\", "/")
        text_audio = model.transcribe("C:/Users/Duberly/Desktop/whisper/api/uploads/"+file,fp16=False)
        # print(text_audio['text'])
        inter_text = "Esta es la conversacion completa del entrevistador y el entrevistado.Puedes dar formato a la información proporcionada utilizando HTML para mejorar su presentación solo el contenido que debo pegar dentro del elemento <body> de mi página HTML osea dame la respuesta en html"
        result=openaiResponse(text_prompt + inter_text + text_audio['text'] )['choices'][0]['message']['content']
        os.remove(file_path)#Eliminamos el archivo una ves convertido
        return render(request, 'index.html',{'text_response':result})
    return render(request, 'index.html',{'text_response':"Error al subir archivo"})
    

def LoginView():
    pass