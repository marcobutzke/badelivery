from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Categoria(models.Model):
    descricao = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categoria'

    def __str__(self):
        return self.descricao

class Unidade(models.Model):
    sigla = models.CharField(max_length=5)
    descricao = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'unidade'

    def __str__(self):
        return self.sigla


class Segmento(models.Model):
    descricao = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'segmento'

    def __str__(self):
        return self.descricao


class Tipo(models.Model):
    descricao = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo'

    def __str__(self):
        return self.descricao


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    contato = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    contato = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'fornecedor'

    def __str__(self):
        return self.nome


class Indicador(models.Model):
    descricao = models.CharField(max_length=50)
    formula = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'indicador'

    def __str__(self):
        return self.descricao


class Conta(models.Model):
    tipo_natureza = (
        ('DEBITO', 'Débito'),
        ('CREDITO', 'Crédito'),
    )
    tipo_conta = (
        ('SINTETICA', 'Sintética'),
        ('ANALITICA', 'Analítica'),
    )
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=50)
    natureza = models.CharField(max_length=20, choices=tipo_natureza, default='Débito')
    nivel = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])
    tipo = models.CharField(max_length=20, choices=tipo_conta, default='Sintética')
    saldoinicial = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'conta'

    def __str__(self):
        return f"{self.codigo}-{self.descricao}"


class Operacao(models.Model):
    sigla = models.CharField(max_length=10)
    descricao = models.CharField(max_length=50)
    debito = models.ForeignKey(Conta, models.DO_NOTHING, db_column='debito')
    credito = models.ForeignKey(Conta, models.DO_NOTHING, db_column='credito', related_name='operacao_credito_set')

    class Meta:
        managed = False
        db_table = 'operacao'

    def __str__(self):
        return self.descricao

class Ingrediente(models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    ativo = models.BooleanField()
    segmento = models.ForeignKey(Segmento, models.DO_NOTHING)
    quantidade = models.IntegerField()
    unidade = models.ForeignKey(Unidade, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ingrediente'

    def __str__(self):
        return self.descricao

class Acessorio(models.Model):
    sigla = models.CharField(max_length=10)
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    ativo = models.BooleanField()
    quantidade = models.IntegerField()
    unidade = models.ForeignKey(Unidade, models.DO_NOTHING)
    porcao = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'acessorio'

    def __str__(self):
        return self.descricao

class Componente(models.Model):
    acessorio = models.ForeignKey(Acessorio, models.DO_NOTHING)
    ingrediente = models.ForeignKey(Ingrediente, models.DO_NOTHING)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'componente'


class Produto(models.Model):
    sigla = models.CharField(max_length=10)
    descricao = models.CharField(max_length=50)
    estoque = models.IntegerField()
    ativo = models.BooleanField()
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    quantidade = models.IntegerField()
    unidade = models.ForeignKey(Unidade, models.DO_NOTHING)
    porcao = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'produto'

    def __str__(self):
        return self.descricao

class Composicao(models.Model):
    produto = models.ForeignKey(Produto, models.DO_NOTHING)
    ingrediente = models.ForeignKey(Ingrediente, models.DO_NOTHING)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'composicao'

class Formacao(models.Model):
    produto = models.ForeignKey(Produto, models.DO_NOTHING)
    acessorio = models.ForeignKey(Acessorio, models.DO_NOTHING)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'formacao'

class Preco(models.Model):
    tipo = models.ForeignKey(Tipo, models.DO_NOTHING)
    produto = models.ForeignKey(Produto, models.DO_NOTHING)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'preco'

class Periodo(models.Model):
    situacao_periodo = (
        ('ABERTO', 'Aberto'),
        ('ATUAL', 'Atual'),
        ('FECHADO', 'Fechado'),
    )
    sigla = models.CharField(max_length=10)
    inicio = models.DateField()
    final = models.DateField()
    situacao = models.CharField(max_length=20, choices=situacao_periodo, default='Aberto')

    class Meta:
        managed = False
        db_table = 'periodo'

    def __str__(self):
        return self.sigla

class Compra(models.Model):
    tipo_pago = (
        ('ABERTO', 'Aberto'),
        ('PAGO', 'Pago'),
    )
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, models.DO_NOTHING)
    situacao = models.CharField(max_length=20, choices=tipo_pago, default='Aberto')
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'compra'

    def __str__(self):
        return f"{self.fornecedor}-{self.data}"

class Insumo(models.Model):
    compra = models.ForeignKey(Compra, models.DO_NOTHING)
    ingrediente = models.ForeignKey(Ingrediente, models.DO_NOTHING)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'insumo'

class Producao(models.Model):
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)
    produto = models.ForeignKey(Produto, models.DO_NOTHING)
    data = models.DateField()
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'producao'

class Manufatura(models.Model):
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)
    acessorio = models.ForeignKey(Acessorio, models.DO_NOTHING)
    data = models.DateField()
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'manufatura'

class Pedido(models.Model):
    tipo_pago = (
        ('ABERTO', 'Aberto'),
        ('PAGO', 'Pago'),
    )
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    previsao = models.DateTimeField(blank=True, null=True)
    entrega = models.DateTimeField(blank=True, null=True)
    situacao = models.CharField(max_length=20, choices=tipo_pago, default='Aberto')
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pedido'

    def __str__(self):
        return f"{self.cliente}-{self.data}"

class Item(models.Model):
    pedido = models.ForeignKey(Pedido, models.DO_NOTHING)
    produto = models.ForeignKey(Produto, models.DO_NOTHING)
    quantidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'

class Carga(models.Model):
    data = models.DateTimeField()
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'carga'

class Pacote(models.Model):
    carga = models.ForeignKey(Carga, models.DO_NOTHING)
    pedido = models.ForeignKey(Pedido, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pacote'

class Lancamento(models.Model):
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    operacao = models.ForeignKey(Operacao, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lancamento'

class Contaapagar(models.Model):
    tipo_pago = (
        ('ABERTO', 'Aberto'),
        ('PAGO', 'Pago'),
    )
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()
    pagamento = models.DateField(blank=True, null=True)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    fornecedor = models.ForeignKey(Fornecedor, models.DO_NOTHING, blank=True, null=True)
    compra = models.ForeignKey(Compra, models.DO_NOTHING, blank=True, null=True)
    situacao = models.CharField(max_length=20, choices=tipo_pago, default='Aberto')
    operacao = models.ForeignKey(Operacao, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contaapagar'

class Contasareceber(models.Model):
    tipo_pago = (
        ('ABERTO', 'Aberto'),
        ('PAGO', 'Pago'),
    )
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()
    pagamento = models.DateField(blank=True, null=True)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, models.DO_NOTHING, blank=True, null=True)
    situacao = models.CharField(max_length=20, choices=tipo_pago, default='Aberto')
    operacao = models.ForeignKey(Operacao, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contasareceber'

