from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q


class Unidade(models.Model):
    sigla = models.CharField(max_length=5)
    descricao = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'unidade'
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"

    def __str__(self):
        return self.sigla


class Segmento(models.Model):
    descricao = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'segmento'
        verbose_name = "Segmento"
        verbose_name_plural = "Segmentos"

    def __str__(self):
        return self.descricao


class MercadoriaIngredienteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q (tipo='INGREDIENTE') | Q (tipo='COMERCIALIZACAO'))


class MercadoriaEmbalagemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='EMBALAGEM')


class Mercadoria(models.Model):
    tipo_mercadoria = (
        ('INGREDIENTE', 'Ingrediente'),
        ('EMBALAGEM', 'Embalagem'),
        ('LIMPEZA', 'Limpeza'),
        ('COMERCIALIZACAO', 'Comercialização')
    )
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    ativo = models.BooleanField()
    segmento = models.ForeignKey(Segmento, models.DO_NOTHING)
    quantidade = models.IntegerField()
    unidade = models.ForeignKey(Unidade, models.DO_NOTHING)
    tipo = models.CharField(max_length=20, choices=tipo_mercadoria, default='Ingrediente')

    class Meta:
        managed = False
        db_table = 'mercadoria'
        verbose_name = "Mercadoria"
        verbose_name_plural = "Mercadorias"

    def __str__(self):
        return self.descricao


class MercadoriaIngrediente(Mercadoria):
    objects = MercadoriaIngredienteManager()

    class Meta:
        proxy = True


class MercadoriaEmbalagem(Mercadoria):
    objects = MercadoriaEmbalagemManager()

    class Meta:
        proxy = True


class Categoria(models.Model):
    descricao = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categoria'
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.descricao

class Tipo(models.Model):
    descricao = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo'
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"

    def __str__(self):
        return self.descricao


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    contato = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    contato = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'fornecedor'
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.nome

class ContaAnaliticaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='ANALITICA')

class Conta(models.Model):
    tipo_natureza = (
        ('DEBITO', 'Débito'),
        ('CREDITO', 'Crédito'),
    )
    tipo_conta = (
        ('SINTETICA', 'Sintética'),
        ('ANALITICA', 'Analítica'),
    )
    tipo_contabil = (
        ('PATRIMONIAL', 'Patrimonial'),
        ('RESULTADO', 'Resultado')
    )
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=50)
    natureza = models.CharField(max_length=20, choices=tipo_natureza, default='Débito')
    nivel = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])
    tipo = models.CharField(max_length=20, choices=tipo_conta, default='Sintética')
    saldoinicial = models.DecimalField(max_digits=10, decimal_places=2)
    contabil = models.CharField(max_length=20, choices=tipo_contabil, default='Patrimonial')

    class Meta:
        managed = False
        db_table = 'conta'
        verbose_name = "Conta"
        verbose_name_plural = "Contas"

    def __str__(self):
        return f"{self.codigo}-{self.descricao}"

class ContaAnalitica(Conta):
    objects = ContaAnaliticaManager()

    class Meta:
        proxy = True

class OperacaoContasaReceberManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(areceber=True)

class OperacaoContasaPagarManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(apagar=True)

class Operacao(models.Model):
    sigla = models.CharField(max_length=10)
    descricao = models.CharField(max_length=50)
    debito = models.ForeignKey(ContaAnalitica, models.DO_NOTHING, db_column='debito')
    credito = models.ForeignKey(ContaAnalitica, models.DO_NOTHING, db_column='credito', related_name='operacao_credito_set')
    apagar = models.BooleanField()
    areceber = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'operacao'
        verbose_name = "Operação"
        verbose_name_plural = "Operações"

    def __str__(self):
        return self.descricao

class OperacaoContasaReceber(Operacao):
    objects = OperacaoContasaReceberManager()

    class Meta:
        proxy = True

class OperacaoContasaPagar(Operacao):
    objects = OperacaoContasaPagarManager()

    class Meta:
        proxy = True



class Acessorio(models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    ativo = models.BooleanField()
    quantidade = models.IntegerField()
    unidade = models.ForeignKey(Unidade, models.DO_NOTHING)
    porcao = models.IntegerField(default=1)
    modopreparo = models.TextField()

    class Meta:
        managed = False
        db_table = 'acessorio'
        verbose_name = "Acessório"
        verbose_name_plural = "Acessórios"

    def __str__(self):
        return self.descricao

class Componente(models.Model):
    acessorio = models.ForeignKey(Acessorio, models.DO_NOTHING)
    mercadoria = models.ForeignKey(MercadoriaIngrediente, models.DO_NOTHING)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'componente'
        verbose_name = "Componente"
        verbose_name_plural = "Componentes"

    def __str__(self):
        return f"{self.mercadoria}"

class Produto(models.Model):
    sigla = models.CharField(max_length=10)
    descricao = models.CharField(max_length=50)
    estoque = models.IntegerField()
    ativo = models.BooleanField()
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    quantidade = models.IntegerField()
    unidade = models.ForeignKey(Unidade, models.DO_NOTHING)
    porcao = models.IntegerField(default=1)
    modopreparo = models.TextField()

    class Meta:
        managed = False
        db_table = 'produto'
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.sigla}-{self.descricao}"

class Composicao(models.Model):
    produto = models.ForeignKey(Produto, models.DO_NOTHING)
    mercadoria = models.ForeignKey(MercadoriaIngrediente, models.DO_NOTHING)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'composicao'
        verbose_name = "Composição"
        verbose_name_plural = "Composições"

    def __str__(self):
        return f"{self.mercadoria}-{self.produto}"

class Formacao(models.Model):
    produto = models.ForeignKey(Produto, models.DO_NOTHING)
    acessorio = models.ForeignKey(Acessorio, models.DO_NOTHING)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'formacao'
        verbose_name = "Formação"
        verbose_name_plural = "Formações"

    def __str__(self):
        return f"{self.acessorio}-{self.produto}"


class Preco(models.Model):
    tipo = models.ForeignKey(Tipo, models.DO_NOTHING)
    produto = models.ForeignKey(Produto, models.DO_NOTHING)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'preco'
        verbose_name = "Preço"
        verbose_name_plural = "Preços"

    def __str__(self):
        return f"{self.tipo}-{self.produto}"

class Embalagem(models.Model):
    produto = models.ForeignKey(Produto, models.DO_NOTHING)
    mercadoria = models.ForeignKey(MercadoriaEmbalagem, models.DO_NOTHING)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'embalagem'
        verbose_name = "Embalagem"
        verbose_name_plural = "Embalagens"

    def __str__(self):
        return f"{self.mercadoria}-{self.produto}"

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
    anterior = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo'
        verbose_name = "Período"
        verbose_name_plural = "Períodos"

    def __str__(self):
        return self.sigla

class Compra(models.Model):
    tipo_pago = (
        ('ABERTA', 'Aberta'),
        ('FECHADA', 'Fechada'),
        ('PAGA', 'Paga'),
    )
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, models.DO_NOTHING)
    situacao = models.CharField(max_length=20, choices=tipo_pago, default='Aberto')
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'compra'
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return f"{self.fornecedor}-{self.data}"

class Volume(models.Model):
    compra = models.ForeignKey(Compra, models.DO_NOTHING)
    mercadoria = models.ForeignKey(Mercadoria, models.DO_NOTHING)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'volume'
        verbose_name = "Volume"
        verbose_name_plural = "Volumes"

    def __str__(self):
        return f"{self.mercadoria}-{self.compra}"


class Producao(models.Model):
    tipo_producao = (
        ('PROGRAMADO', 'Programado'),
        ('REALIZADO', 'Realizado'),
    )
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)
    produto = models.ForeignKey(Produto, models.DO_NOTHING)
    data = models.DateField()
    quantidade = models.IntegerField()
    produzido = models.IntegerField()
    situacao = models.CharField(max_length=20, choices=tipo_producao, default='Programado')

    class Meta:
        managed = False
        db_table = 'producao'
        verbose_name = "Produção"
        verbose_name_plural = "Produções"

    def __str__(self):
        return f"{self.produto}-{self.data}"


class Manufatura(models.Model):
    tipo_producao = (
        ('PROGRAMADO', 'Programado'),
        ('REALIZADO', 'Realizado'),
    )
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)
    acessorio = models.ForeignKey(Acessorio, models.DO_NOTHING)
    data = models.DateField()
    quantidade = models.IntegerField()
    produzido = models.IntegerField()
    situacao = models.CharField(max_length=20, choices=tipo_producao, default='Programado')

    class Meta:
        managed = False
        db_table = 'manufatura'
        verbose_name = "Manufatura"
        verbose_name_plural = "Manufaturas"

    def __str__(self):
        return f"{self.acessorio}-{self.data}"

class Pedido(models.Model):
    tipo_pedido = (
        ('ABERTO', 'Aberto'),
        ('FECHADO', 'Fechado'),
        ('PAGO', 'Pago'),
    )
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)
    numero = models.CharField(max_length=10)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    situacao = models.CharField(max_length=20, choices=tipo_pedido, default='Aberto')

    class Meta:
        managed = False
        db_table = 'pedido'
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"{self.cliente}-{self.data}-{self.numero}"

class Item(models.Model):
    pedido = models.ForeignKey(Pedido, models.DO_NOTHING)
    produto = models.ForeignKey(Produto, models.DO_NOTHING)
    quantidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'
        verbose_name = "Item"
        verbose_name_plural = "Itens"

    def __str__(self):
        return f"{self.produto}-{self.pedido}"

class Lancamento(models.Model):
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    operacao = models.ForeignKey(Operacao, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lancamento'
        verbose_name = "Lançamento"
        verbose_name_plural = "Lançamentos"

    def __str__(self):
        return self.descricao

class Contaapagar(models.Model):
    tipo_pago = (
        ('ABERTO', 'Aberto'),
        ('PAGO', 'Pago'),
        ('PARCIAL', 'Parcial')
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
    valorpago = models.DecimalField(max_digits=10, decimal_places=2)
    operacao = models.ForeignKey(OperacaoContasaPagar, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contaapagar'
        verbose_name = "Contas a Pagar"
        verbose_name_plural = "Contas a Pagar"


class Contasareceber(models.Model):
    tipo_pago = (
        ('ABERTO', 'Aberto'),
        ('PAGO', 'Pago'),
        ('PARCIAL', 'Parcial')
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
    valorpago = models.DecimalField(max_digits=10, decimal_places=2)
    operacao = models.ForeignKey(OperacaoContasaReceber, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contasareceber'
        verbose_name = "Contas a Receber"
        verbose_name_plural = "Contas a Receber"

class Movimento(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    natureza = models.CharField(max_length=20)
    conta = models.ForeignKey(ContaAnalitica, models.DO_NOTHING)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    lancamento = models.ForeignKey(Lancamento, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movimento'
        verbose_name = "Movimento"
        verbose_name_plural = "Movimentos"

class Devolucao(models.Model):
    tipo_pedido = (
        ('ABERTO', 'Aberto'),
        ('FECHADO', 'Fechado'),
        ('PAGO', 'Pago'),
    )
    numero = models.CharField(max_length=10)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    situacao = models.CharField(max_length=20, choices=tipo_pedido, default='Aberto')
    periodo = models.ForeignKey(Periodo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'devolucao'
        verbose_name = "Devolução"
        verbose_name_plural = "Devoluções"

    def __str__(self):
        return f"{self.cliente}-{self.data}-{self.numero}"

class Elemento(models.Model):
    devolucao = models.ForeignKey(Devolucao, models.DO_NOTHING)
    produto = models.ForeignKey('Produto', models.DO_NOTHING)
    quantidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elemento'
        verbose_name = "Elemento"
        verbose_name_plural = "Elementos"

    def __str__(self):
        return f"{self.produto}-{self.devolucao}"


class VendasPeriodoAtual(models.Model):
    id = models.IntegerField(primary_key=True)
    periodo = models.CharField(max_length=10)
    situacao = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'vendas_periodo_atual'

class AreceberPeriodoAtual(models.Model):
    id = models.IntegerField(primary_key=True)
    aberto = models.DecimalField(max_digits=10, decimal_places=2)
    inadimplencia = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'areceber_periodo_atual'

class VendasTipoCliente(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=20)
    cliente = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'vendas_tipo_cliente'

class VendasTipoCategoria(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    produto = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'vendas_tipo_categoria'

class VendasCategoriaTipo(models.Model):
    id = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    produto = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'vendas_categoria_tipo'

class ClientesRFM(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente = models.CharField(max_length=50)
    recente = models.IntegerField()
    frequencia = models.IntegerField()
    pago = models.DecimalField(max_digits=10, decimal_places=2)
    montante = models.DecimalField(max_digits=10, decimal_places=2)
    pct = models.DecimalField(max_digits=10, decimal_places=2)
    rec = models.IntegerField()
    frq = models.IntegerField()
    pag = models.IntegerField()
    mnt = models.IntegerField()
    rf = models.IntegerField()
    pm = models.IntegerField()
    rfpm = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente_rfm'

class IndicadoresEstoque(models.Model):
    id = models.IntegerField(primary_key=True)
    conta = models.CharField(max_length=25)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'indicadores_estoque'

class VendasCurvaABC(models.Model):
    id = models.IntegerField(primary_key=True)
    produto = models.CharField(max_length=25)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    porcentagem = models.DecimalField(max_digits=10, decimal_places=2)
    cumulativo = models.DecimalField(max_digits=10, decimal_places=2)
    curva = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'vendas_curva_abc'

class CategoriaProduto(models.Model):
    id = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=20)
    produto = models.CharField(max_length=25)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'categoria_produto'

class CustosCurvaABC(models.Model):
    id = models.IntegerField(primary_key=True)
    produto = models.CharField(max_length=25)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    porcentagem = models.DecimalField(max_digits=10, decimal_places=2)
    cumulativo = models.DecimalField(max_digits=10, decimal_places=2)
    curva = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'custos_curva_abc'

class ProducaoQuantidade(models.Model):
    id = models.IntegerField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'producao_quantidade'

class ProducaoValor(models.Model):
    id = models.IntegerField(primary_key=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'producao_valor'

class ProducaoCusto(models.Model):
    id = models.IntegerField(primary_key=True)
    custo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'producao_custo'

class ProducaoCategoria(models.Model):
    id = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=20)
    produto = models.CharField(max_length=25)
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'producao_categoria'

class ProducaoDiaria(models.Model):
    id = models.IntegerField(primary_key=True)
    dia = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'producao_diaria'

class ProducaoDiariaCategoria(models.Model):
    id = models.IntegerField(primary_key=True)
    dia = models.IntegerField()
    categoria = models.CharField(max_length=20)
    produto = models.CharField(max_length=25)
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'producao_diaria_categoria'

class IndicadoresCompra(models.Model):
    id = models.IntegerField(primary_key=True)
    compras_mes = models.DecimalField(max_digits=10, decimal_places=2)
    compras_abertas = models.DecimalField(max_digits=10, decimal_places=2)
    inadimplencia = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'indicadores_compras'

class MercadoriaCurvaABC(models.Model):
    id = models.IntegerField(primary_key=True)
    ingrediente = models.CharField(max_length=25)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    porcentagem = models.DecimalField(max_digits=10, decimal_places=2)
    cumulativo = models.DecimalField(max_digits=10, decimal_places=2)
    curva = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mercadoria_abc'

class ComprasSegmento(models.Model):
    id = models.IntegerField(primary_key=True)
    segmento = models.CharField(max_length=20)
    ingrediente = models.CharField(max_length=25)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'compras_segmento'

class ConsumoMercadoria(models.Model):
    id = models.IntegerField(primary_key=True)
    segmento = models.CharField(max_length=20)
    ingrediente = models.CharField(max_length=25)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'consumo_mercadoria'

class ResultadoAtual(models.Model):
    id = models.IntegerField(primary_key=True)
    conta = models.CharField(max_length=20)
    natureza = models.CharField(max_length=10)
    valor_original = models.DecimalField(max_digits=10, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'resultados_atual'

class ResultadoGeral(models.Model):
    id = models.IntegerField(primary_key=True)
    nivel1 = models.CharField(max_length=30)
    nivel2 = models.CharField(max_length=30)
    nivel3 = models.CharField(max_length=30)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'resultado_geral'

class ResultadoGeralAtual(models.Model):
    id = models.IntegerField(primary_key=True)
    nivel1 = models.CharField(max_length=30)
    nivel2 = models.CharField(max_length=30)
    nivel3 = models.CharField(max_length=30)
    natureza = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'resultado_geral_atual'

class FinanceiroReceber(models.Model):
    id = models.IntegerField(primary_key=True)
    aberto = models.DecimalField(max_digits=10, decimal_places=2)
    inadimplencia = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'financeiro_receber'

class FinanceiroPagar(models.Model):
    id = models.IntegerField(primary_key=True)
    aberto = models.DecimalField(max_digits=10, decimal_places=2)
    inadimplencia = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'financeiro_pagar'

class FinanceiroOperacao(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.DateField()
    dia = models.IntegerField()
    operacao = models.CharField(max_length=40)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'financeiro_operacao'

class FinanceiroLancamento(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.DateField()
    pessoa = models.CharField(max_length=40)
    operacao = models.CharField(max_length=40)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valor_original = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'financeiro_lancamento'

class DisponibilidadeCaixa(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.DateField()
    descricao = models.CharField(max_length=80)
    debito = models.DecimalField(max_digits=10, decimal_places=2)
    credito = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'disponibilidades_caixa'

class DisponibilidadeCartao(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.DateField()
    descricao = models.CharField(max_length=80)
    debito = models.DecimalField(max_digits=10, decimal_places=2)
    credito = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'disponibilidades_cartao'

class DisponibilidadeBanco(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.DateField()
    descricao = models.CharField(max_length=80)
    debito = models.DecimalField(max_digits=10, decimal_places=2)
    credito = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'disponibilidades_banco'

class InicioEconomico(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=10)
    data = models.DateField()
    dia = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'inicio_economico'

class InicioFinanceiro(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=10)
    data = models.DateField()
    dia = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'inicio_financeiro'