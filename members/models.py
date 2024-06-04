from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from localflavor.br.models import BRPostalCodeField
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# AQUI TEMOS UMA IMPORTAÇÃO DE UMA BIBLIOTÉCA PARA PADRONIZAR O CEP BRPostalCodeFildes


# ABAIXO ESTÃO AS INFROMAÇÕES QUE SERÃO SOLICITADA AO USUARIO, PARA CADASTRO NO BANCO.
# MAX_LENGTH = A QUANTIDADE DE CARACTERES QUE PODE SER DIGITADAS
# NULL = SIGNIFICA QUE É UMA CAMPO OBRIGATÓRIO E BLANK= NÃO PODE SER EM BRACO
# VERBOSE_NAME = É UM APELIDO PARA A VARIAVEL QUE ESTA INGLÊS (EX: FIRST_NAME) ENTTÃO PASSASMO NA VEBOSE UM NOME QUE SERÁ EXEBIDO PARA USUARIO.
# Create your models here.
class Members(models.Model):
    # VALIDADOR PARA NOMES
    name_validator = RegexValidator(
        r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$",  # Esta regex inclui espaços e caracteres acentuados comuns
        "Somente letras e espaços são permitidos.",
    )
    # NOME_MEMBRO
    first_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="NOME",
        validators=[name_validator],
    )
    # ÚLTIMO_NOME
    last_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="SOBRE NOME",
        validators=[name_validator],
    )
    # DATA_NASCIMENTO
    date_birth = models.DateField(
        null=False, blank=False, verbose_name="DATA DE NASCIMENTO"
    )
    # DATA_BATISMO
    date_baptism = models.DateField(
        null=False, blank=False, verbose_name="DATA DE BATÍSMO"
    )
    # ENDEREÇO
    address = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="ENDEREÇO"
    )
    # CEP
    cep = BRPostalCodeField(null=False, blank=True, verbose_name="CEP")

    # O CÓDIGO ABAIXO DEIXA O TEXTO ENVIADO PELO USUARIO EM MAIUSCULO ANTES DE SALVAR NO BD
    def save(self, *args, **kwargs):
        self.first_name = self.first_name.upper() if self.first_name else ""
        self.last_name = self.last_name.upper() if self.last_name else ""
        self.address = self.address.upper() if self.address else ""

        super(Members, self).save(*args, **kwargs)
