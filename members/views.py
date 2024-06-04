from .models import Members
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from django.urls import reverse_lazy
from django.http import HttpResponse

import openpyxl


# Create your views here.
class NewUser(TemplateView):
    template_name = "user.html"


class Login(TemplateView):
    template_name = "login.html"


class MembersListViwe(ListView):
    model = Members


class MembersCreateViwe(CreateView):
    model = Members
    fields = ["first_name", "last_name", "date_birth", "date_baptism", "address", "cep"]
    success_url = reverse_lazy("members_list")


class MembersUpdateViwe(UpdateView):
    model = Members
    fields = ["first_name", "last_name", "date_birth", "date_baptism", "address", "cep"]
    # Aqui estou falando para onde vou ser direcionado quando a tarefa for concluida
    success_url = reverse_lazy("members_list")


class MembersDeleteViwe(DeleteView):
    model = Members
    # Aqui estou falando para onde vou ser direcionado quando a tarefa for concluida
    success_url = reverse_lazy("members_list")


class ExcelDownloadView(View):
    def get(self, request, *args, **kwargs):
        # Cria um novo workbook do Excel
        wb = openpyxl.Workbook()
        ws = wb.active
        # Titulo da planilha
        ws.title = "Membros"

        # Definindo os cabeçalhos da planilha
        headers = [
            "id",
            "NOME",
            "SOBRE NOME",
            "DATA NASCIMENTO",
            "DATA BATISMO",
            "ENDEREÇO",
            "CEP",
        ]
        ws.append(headers)

        # Aqui estou pegando as informações do banco de dados
        membros = Members.objects.all()
        for membro in membros:
            ws.append(
                [
                    membro.id,
                    membro.first_name,
                    membro.last_name,
                    membro.date_birth,
                    membro.date_baptism,
                    membro.address,
                    membro.cep,
                ]
            )

        # Configurando a resposta para fazer o download como um arquivo Excel
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = 'attachment; filename="membros.xlsx"'

        # Salvando o workbook no buffer da resposta
        wb.save(response)

        return response
