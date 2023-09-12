from django.db import models

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nomecompleto = models.CharField(max_length=160, null=True)
    nascimento = models.DateField(null=True)
    cpf = models.CharField(max_length=11, null=True, unique=True)
    cep = models.CharField(max_length=8, null=True)
    numerocasa = models.CharField(max_length=4, null=True)
    uf = models.CharField(max_length=2, null=True)
    cidade = models.CharField(max_length=50, null=True)
    país = models.CharField(max_length=45, null=True)
    username = models.CharField(max_length=45, unique=True)
    senha = models.CharField(max_length=45)

class Campanha(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.CharField(max_length=45)
    titulocampanha = models.CharField(max_length=150)
    descricao = models.TextField()
    datainicio = models.DateTimeField()
    datatermino = models.DateTimeField()
    valormeta = models.IntegerField()
    imagem1 = models.CharField(max_length=250, null=True)
    imagem2 = models.CharField(max_length=250, null=True)
    imagem3 = models.CharField(max_length=250, null=True)
    imagem4 = models.CharField(max_length=250, null=True)
    imagem5 = models.CharField(max_length=250, null=True)
    imagem6 = models.CharField(max_length=250, null=True)
    imagem7 = models.CharField(max_length=250, null=True)
    imagem8 = models.CharField(max_length=250, null=True)
    background = models.CharField(max_length=250, null=True)
    logo = models.CharField(max_length=250, null=True)
    texto1 = models.CharField(max_length=450, null=True)
    texto2 = models.CharField(max_length=450, null=True)
    texto3 = models.CharField(max_length=450, null=True)
    texto4 = models.CharField(max_length=450, null=True)
    texto5 = models.CharField(max_length=450, null=True)
    usuario_iddoador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Doacao(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2)
    data = models.CharField(max_length=45)
    usuario_idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cartao_numerocartao = models.CharField(max_length=16)
    campanha_id = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, null=True)
    tipo = models.CharField(max_length=45)

class Configuracoes(models.Model):
    nomeinstituicao = models.CharField(max_length=45, primary_key=True)
    emailinstituicao = models.CharField(max_length=45)
    multas = models.CharField(max_length=45)