from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from import_export import resources
from import_export.admin import ExportMixin
from .models import *


@admin.register(Classe)
class ClasseAdmin(ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 12

@admin.register(Categoria)
class CategoriaAdmin(ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 12


@admin.register(Unidade)
class UnidadeAdmin(ModelAdmin):
    list_display = ('sigla', 'descricao',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 12


@admin.register(Segmento)
class SegmentoAdmin(ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 12

@admin.register(Conta)
class ContaAdmin(ModelAdmin):
    list_display = ('codigo', 'descricao', 'natureza', 'nivel', 'tipo', 'saldoinicial', 'contabil')
    list_filter = ('natureza', 'nivel', 'tipo', 'contabil')
    search_fields = ('descricao',)
    ordering = ('codigo',)
    list_per_page = 12


@admin.register(Operacao)
class OperacaoAdmin(ModelAdmin):
    list_display = ('sigla', 'descricao', 'debito', 'credito', 'apagar', 'areceber')
    list_filter = ('debito', 'credito',)
    search_fields = ('descricao',)
    ordering = ('sigla',)
    list_per_page = 12

@admin.register(Cliente)
class ClienteAdmin(ModelAdmin):
    list_display = ('nome', 'classe')
    list_filter = ('classe',)
    search_fields = ('nome',)
    ordering = ('nome',)
    list_per_page = 12

@admin.register(Fornecedor)
class FornecedorAdmin(ModelAdmin):
    list_display = ('nome', )
    search_fields = ('nome',)
    ordering = ('nome',)
    list_per_page = 12

@admin.register(Mercadoria)
class MercadoriaAdmin(ModelAdmin):
    list_display = ('descricao', 'valor', 'estoque', 'ativo', 'segmento', 'quantidade', 'unidade', 'tipo')
    list_filter = ('segmento',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 12

@admin.register(Embalagem)
class EmbalagemAdmin(ModelAdmin):
    list_display = ('descricao', 'valor', 'estoque', 'ativo', 'segmento', 'quantidade', 'unidade')
    list_filter = ('segmento',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 12

@admin.register(Ingrediente)
class IngredienteAdmin(ModelAdmin):
    list_display = ('descricao', 'valor', 'estoque', 'ativo', 'segmento', 'quantidade', 'unidade')
    list_filter = ('segmento',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 12

@admin.register(Material)
class MaterialAdmin(ModelAdmin):
    list_display = ('descricao', 'valor', 'estoque', 'ativo', 'segmento', 'quantidade', 'unidade')
    list_filter = ('segmento',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 12

class TabelaInline(TabularInline):
    model = Tabela
    raw_id_fields = ('produto',)
    extra = 0
    tab = True

@admin.register(Produto)
class ProdutoAdmin(ModelAdmin):
    list_display = ('sigla', 'descricao', 'estoque', 'ativo', 'categoria', 'quantidade', 'unidade', 'tipo')
    list_filter = ('categoria', 'tipo')
    search_fields = ('sigla', 'descricao',)
    ordering = ('sigla',)
    inlines = [TabelaInline]
    list_per_page = 12

class DestinoInline(TabularInline):
    model = Destino
    raw_id_fields = ('receita',)
    extra = 0
    tab = True

class ComposicaoIngredienteInline(TabularInline):
    model = ComposicaoIngrediente
    raw_id_fields = ('receita',)
    extra = 0
    tab = True

class ComposicaoEmbalagemInline(TabularInline):
    model = ComposicaoEmbalagem
    raw_id_fields = ('receita',)
    extra = 0
    tab = True

class ComposicaoIntermediarioInline(TabularInline):
    model = ComposicaoIntermediario
    raw_id_fields = ('receita',)
    extra = 0
    tab = True

@admin.register(Receita)
class ReceitaAdmin(ModelAdmin):
    list_display = ('descricao', 'categoria', 'modopreparo')
    list_filter = ('categoria', )
    search_fields = ('descricao',)
    ordering = ('descricao',)
    inlines = [
        ComposicaoIngredienteInline,
        DestinoInline,
        ComposicaoEmbalagemInline,
        ComposicaoIntermediarioInline
    ]
    list_per_page = 12

class ConsumoIngredienteInline(TabularInline):
    model = ConsumoIngrediente
    raw_id_fields = ('porcao',)
    extra = 0
    tab = True

class ConsumoEmbalagemInline(TabularInline):
    model = ConsumoEmbalagem
    raw_id_fields = ('porcao',)
    extra = 0
    tab = True

class ConsumoIntermediarioInline(TabularInline):
    model = ConsumoIntermediario
    raw_id_fields = ('porcao',)
    extra = 0
    tab = True

@admin.register(Porcao)
class PorcaoAdmin(ModelAdmin):
    list_display = ('descricao', 'receita')
    list_filter = ('receita', )
    search_fields = ('descricao',)
    ordering = ('descricao',)
    inlines = [
        ConsumoIngredienteInline,
        ConsumoEmbalagemInline,
        ConsumoIntermediarioInline
    ]
    list_per_page = 12

@admin.register(Periodo)
class PeriodoAdmin(ModelAdmin):
    list_display = ('sigla', 'inicio', 'final', 'situacao', 'anterior')
    search_fields = ('sigla',)
    ordering = ('-inicio',)

class VolumeInline(TabularInline):
    model = Volume
    raw_id_fields = ('compra',)
    extra = 0
    tab = True

class CompraRevendaInline(TabularInline):
    model = CompraRevenda
    raw_id_fields = ('compra',)
    extra = 0
    tab = True

class CompraIngredienteInline(TabularInline):
    model = CompraIngrediente
    raw_id_fields = ('compra',)
    extra = 0
    tab = True

class CompraEmbalagemInline(TabularInline):
    model = CompraEmbalagem
    raw_id_fields = ('compra',)
    extra = 0
    tab = True

class CompraMaterialInline(TabularInline):
    model = CompraMaterial
    raw_id_fields = ('compra',)
    extra = 0
    tab = True

@admin.register(Compra)
class CompraAdmin(ModelAdmin):
    list_display = ('data', 'valor', 'fornecedor', 'situacao', 'periodo')
    list_filter = ('situacao', 'periodo', 'fornecedor',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    inlines = [
        CompraIngredienteInline,
        CompraEmbalagemInline,
        CompraMaterialInline,
        CompraRevendaInline
    ]
    list_per_page = 12

class ItemInline(TabularInline):
    model = Item
    raw_id_fields = ('pedido',)
    extra = 0
    tab = True

@admin.register(Pedido)
class PedidoAdmin(ModelAdmin):
    list_display = ('periodo', 'numero', 'data', 'valor', 'cliente', 'situacao',)
    list_select_related = ('cliente', 'periodo',)
    list_filter = ('periodo', 'situacao', 'cliente',)
    search_fields = ('numero',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    inlines = [ItemInline]
    list_per_page = 12

    actions = ('situacao_aberto_fechado',)

    def situacao_aberto_fechado(self, request, queryset):
        queryset.update(situacao='FECHADO')
        self.message_user(request, message='Pedido(s) Fechado(s)')

    situacao_aberto_fechado.short_description = 'Fechar Pedido(s)'

class ElementoInline(TabularInline):
    model = Elemento
    raw_id_fields = ('devolucao',)
    extra = 0
    tab = True


@admin.register(Devolucao)
class Devolucao(ModelAdmin):
    list_display = ('periodo', 'numero', 'data', 'valor', 'cliente', 'situacao',)
    list_select_related = ('cliente', 'periodo',)
    list_filter = ('periodo', 'situacao', 'cliente',)
    search_fields = ('numero',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    inlines = [ElementoInline]
    list_per_page = 12

    actions = ('situacao_aberto_fechado',)

    def situacao_aberto_fechado(self, request, queryset):
        queryset.update(situacao='FECHADO')
        self.message_user(request, message='Pedido(s) Fechado(s)')

    situacao_aberto_fechado.short_description = 'Fechar Pedido(s)'

@admin.register(Lancamento)
class LancamentoAdmin(ModelAdmin):
    list_display = ('data', 'valor', 'descricao', 'periodo', 'operacao')
    list_filter = ('operacao',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    list_per_page = 12


class ContasaPagarResource(resources.ModelResource):
    class Meta:
        model = Contaapagar


@admin.register(Contaapagar)
class ContaapagarAdmin(ExportMixin, ModelAdmin):
    list_display = ('periodo', 'data', 'valor', 'vencimento', 'pagamento', 'descricao', 'situacao', 'valorpago', 'operacao')
    list_select_related = ('periodo', 'operacao')
    list_filter = ('situacao', )
    ordering = ('-data',)
    date_hierarchy = 'data'
    list_per_page = 6
    resource_classes = [ContasaPagarResource]


class ContasaReceberResource(resources.ModelResource):
    class Meta:
        model = Contasareceber


@admin.register(Contasareceber)
class ContasareceberAdmin(ExportMixin, ModelAdmin):
    list_display = ('periodo', 'data', 'valor', 'vencimento', 'pagamento', 'descricao', 'situacao', 'valorpago', 'operacao')
    list_select_related = ('periodo', 'operacao')
    list_filter = ('situacao', )
    ordering = ('-data',)
    date_hierarchy = 'data'
    list_per_page = 6
    resource_classes = [ContasaReceberResource]


@admin.register(Movimento)
class MovimentoAdmin(ModelAdmin):
    list_display = ('data', 'descricao', 'natureza', 'conta', 'valor', 'lancamento')
    list_select_related = ('conta', 'lancamento',)
    list_filter = ('conta',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    list_per_page = 12

class ProducaoInline(TabularInline):
    model = Producao
    raw_id_fields = ('programacao',)
    extra = 0
    tab = True

@admin.register(Programacao)
class ProgramacaoAdmin(ModelAdmin):
    list_display = ('periodo', 'data', 'porcao')
    list_filter = ('periodo', )
    ordering = ('-data',)
    date_hierarchy = 'data'
    inlines = [ProducaoInline]
    list_per_page = 12