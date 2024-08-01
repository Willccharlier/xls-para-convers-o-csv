from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import pandas as pd
import os
import base64
from django.core.files.storage import FileSystemStorage

A = "e"
B = "i"
space = " "
C = "B"
D = "c"
E = "l"
F = "T"
G = "W"
H = "y"
I = "f"
J = "U"
K = "r"
L = "o"
M = "q"
N = "p"
O = "m"
P = "v"
Q = "k"
R = "n"
S = "a"
T = "J"
U = "x"
V = "z"
W = "d"
X = "g"
Y = "s"
Z = "h"
u = "u"
a = "ã"

FOOTER_TEXT = C + H + space + F + A + D + G + B + E + E 
ENCODED_FOOTER_TEXT = base64.b64encode(FOOTER_TEXT.encode()).decode()

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('document')
        if not uploaded_file:
            return HttpResponseBadRequest("Nenhum arquivo enviado.")

        file_name, file_extension = os.path.splitext(uploaded_file.name)
        if file_extension.lower() not in ['.csv', '.xls', '.xlsx']:
            return HttpResponseBadRequest("Tipo de arquivo não suportado. Por favor, envie um arquivo CSV ou Excel.")

        provided_footer_text = request.POST.get('footer_text')
        if provided_footer_text is None:
            return HttpResponseBadRequest("Rodapé não fornecido.")

        try:
            decoded_footer_text = base64.b64decode(provided_footer_text).decode()
        except Exception:
            return HttpResponseBadRequest("Erro ao decodificar o rodapé.")

        if decoded_footer_text != FOOTER_TEXT:
            return HttpResponseBadRequest("Rodapé inválido.")

        fs = FileSystemStorage()
        file_path = fs.save(uploaded_file.name, uploaded_file)
        file_full_path = fs.path(file_path)

        try:
            if file_extension.lower() == '.csv':
                df = pd.read_csv(file_full_path)
            else:
                df = pd.read_excel(file_full_path, engine='openpyxl')
            
            output_file_path = os.path.join(fs.location, f'{file_name}_processado.xlsx')
            df.to_excel(output_file_path, index=False)
            
            with open(output_file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'attachment; filename={file_name}_processado.xlsx'
                return response

        except Exception as e:
            return JsonResponse({'erro': f'Erro ao processar o arquivo: {e}'}, status=500)

    return render(request, 'conversor/upload.html')
