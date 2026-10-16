from django.db import models
from django.core.validators import MinValueValidator

class Local(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    endereco = models.CharField()
    capacidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]

class Evento(models.Model):
    local = models.ForeignKey(
        "Local",
        on_delete = models.PROTECT,
        related_name = "eventos",
    )
    categoria = models.ManyToManyField(
        "Categoria",
        related_name="eventos",
        blank=True,
    )

    titulo = models.CharField()
    descricao = models.TextField()
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def vagas_restantes(self):
        return self.local.capacidade - self.inscricoes.count()

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["inicio"]

class Atividade(models.Model):
    evento = models.ForeignKey(
        "Evento",
        on_delete=models.CASCADE,
        related_name="atividades",
    )

    titulo = models.CharField()
    palestrante = models.CharField()
    horario = models.DateTimeField()

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["horario"]

class Inscricao(models.Model):
    evento = models.ForeignKey(
        "Evento",
        on_delete=models.CASCADE,
        related_name="inscricoes",
    )

    nome = models.CharField(max_length=200)
    email = models.EmailField()
    inscrito_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Relatorio(models.Model):
    evento = models.OneToOneField(
        "Evento",
        on_delete=models.CASCADE,
        related_name="relatorios",
    )

    presente = models.PositiveIntegerField()
    observacoes = models.TextField(blank=True)
