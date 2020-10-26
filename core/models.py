from django.db import models
from django.utils import timezone

class Equipamento(models.Model):

    STATUS_CHOICE = (
        ("A", "Ativo"),
        ("D", "Desativo"),
        ("N", "Nenhuma das opções")
    )

    CHOICE_FILIAL = (
        ("1", "Matriz"),
        ("2", "CD"),
        ("3", "Zerão"),
        ("4", "Congós"),
        ("5", "Buritizal"),
        ("6", "Sta Rita")
    )

    CHOICE_TIPO = (
        ("Desktop", "Desktop"),
        ("Laptop", "Laptop"),
        ("Monitor", "Monitor"),
        ("Nobreak", "Nobreak"),
        ("Roteador", "Roteador"),
        ("Switch", "Switch"),
        ("Smartphone", "Smartphone"),
        ("Outros", "Outros")
    )

    CHOICE_MEMORIA = (
        ("2GBb", "2Gb"),
        ("4GBb", "4Gb"),
        ("6GBb", "6Gb"),
        ("8GBb", "8Gb"),
        ("10GBb", "10Gb"),
        ("12GBb", "12Gb"),
        ("16GBb", "16Gb")
    )

    CHOICE_SO = (
        ("Windows XP", "Windows XP"),
        ("Windows 7", "Windows 7"),
        ("Windows 8", "Windows 8"),
        ("Windows 10", "Windows 10"),
        ("Linux", "Linux")
    )

    CHOICE_MEMORIA_TIPO = (
        ("DDR", "DDR"),
        ("DDR2", "DDR2"),
        ("DDR3", "DDR3"),
        ("DDR4", "DDR4"),
        ("DDR5", "DDR5")
    )

    n_invent = models.CharField(null=False, blank=False, max_length=5, verbose_name='Nº Patrimônio')
    tipo = models.CharField(null=False, blank=False, max_length=20, choices=CHOICE_TIPO)
    descricao = models.CharField(null=False, blank=False, max_length=700)
    modelo = models.CharField(null=True, blank=True, max_length=100,)
    fabricante = models.CharField(null=False, blank=False, max_length=20)
    filial = models.CharField(null=False, blank=False, max_length=1, choices=CHOICE_FILIAL)
    local = models.CharField(null=False, blank=False, max_length=20)
    n_serie = models.CharField(null=True, blank=True, max_length=30, verbose_name='Nº Série')
    end_ip = models.CharField(null=True, blank=True, max_length=16, verbose_name='Endereço IP')
    status = models.CharField(null=False, blank=False, max_length=1, choices=STATUS_CHOICE)
    ano_fab = models.DateField(null=True, blank=True, verbose_name='Ano de Fabricação')
    data_aquisicao = models.DateField(null=True, blank=True, verbose_name='Data de aquisição')
    data_cadastro = models.DateTimeField(default=timezone.now, verbose_name='Data de cadastro', editable=False)
    atualizado = models.DateTimeField(default=timezone.now, editable=False)
    so_instalado = models.CharField(null=True, blank=True, max_length=20, choices=CHOICE_SO, verbose_name='Sistema Operacional')
    tipo_memoria = models.CharField(null=True, blank=True, max_length=20, choices=CHOICE_MEMORIA_TIPO, verbose_name='Tipo de memoria')
    memoria_mb = models.CharField(null=True, blank=True, max_length=20, choices=CHOICE_MEMORIA, verbose_name='Memoria em GB')
    processador = models.CharField(null=True, blank=True, max_length=10)
    processdor_ghz = models.CharField(null=True, blank=True, max_length=4, verbose_name='Processador em Ghz')
    nome_host = models.CharField(null=True, blank=True, max_length=40, verbose_name='Nome do Host')
    imagem = models.ImageField(upload_to='equipamento_imagens/%Y/%m/', blank=True, null=True)

    def get_ano(self):
        return self.ano_fab.year

    def __str__(self):
        return self.n_invent

    class Meta:
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"

class Garantia(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    descricao = models.CharField(null=False, blank=False, max_length=700, verbose_name='Descrição da garantia')
    inicio_garantia = models.DateField(null=True, blank=True)
    fim_garantia = models.DateField(null=True, blank=True)
    atendimento = models.CharField(null=False, blank=False, max_length=700)


    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Garantia'
        verbose_name_plural = 'Garantia'
