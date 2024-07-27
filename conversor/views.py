from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import pandas as pd
import os
import base64

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
        uploaded_file = request.FILES['document']
        caminho_xls = os.path.join('media', uploaded_file.name)

        provided_footer_text = request.POST.get('footer_text')
        if provided_footer_text is None:
            return HttpResponseBadRequest("Nao e permitido este formato.")
        
        try:
            decoded_footer_text = base64.b64decode(provided_footer_text).decode()
        except Exception:
            return HttpResponseBadRequest("Código modificado ")

        if decoded_footer_text != FOOTER_TEXT:
            return HttpResponseBadRequest("Erro no código.")

        with open(caminho_xls, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        
        caminho_csv = caminho_xls.replace('.xlsx', '.csv')
        converter_xls_para_csv(caminho_xls, caminho_csv)
        
        with open(caminho_csv, 'rb') as csv_file:
            response = HttpResponse(csv_file.read(), content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(caminho_csv)}'
            return response
    
    return render(request, 'conversor/upload.html')

def converter_xls_para_csv(caminho_xls, caminho_csv):
    df = pd.read_excel(caminho_xls, engine='openpyxl')
    df.to_csv(caminho_csv, index=False)
