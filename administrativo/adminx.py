from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from import_export import resources
from import_export.admin import ExportMixin

from .models import *


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


@admin.register(Tipo)
class TipoAdmin(ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 12


@admin.register(Cliente)
class ClienteAdmin(ModelAdmin):
    list_display = ('nome', 'contato', 'tipo',)
    list_filter = ('tipo',)
    search_fields = ('nome',)
    ordering = ('nome',)
    list_per_page = 12


@admin.register(Fornecedor)
class FornecedorAdmin(ModelAdmin):
    list_display = ('nome', 'contato')
    search_fields = ('nome',)
    ordering = ('nome',)
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


@admin.register(Mercadoria)
class MercadoriaAdmin(ModelAdmin):
    list_display = ('descricao', 'valor', 'estoque', 'ativo', 'segmento', 'quantidade', 'unidade', 'tipo')
    list_filter = ('segmento',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 12


class ComponenteInline(TabularInline):
    model = Componente
    raw_id_fields = ('acessorio',)
    extra = 0
    tab = True


@admin.register(Acessorio)
class AcessorioAdmin(ModelAdmin):
    list_display = ('descricao', 'valor', 'estoque', 'ativo', 'quantidade', 'unidade', 'porcao',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    inlines = [ComponenteInline]
    list_per_page = 12


class ComposicaoInline(TabularInline):
    model = Composicao
    raw_id_fields = ('produto',)
    extra = 0
    tab = True


class FormacaoInline(TabularInline):
    model = Formacao
    raw_id_fields = ('produto',)
    extra = 0
    tab = True


class PrecoInline(TabularInline):
    model = Preco
    raw_id_fields = ('produto',)
    extra = 0
    tab = True


class EmbalagemInline(TabularInline):
    model = Embalagem
    raw_id_fields = ('produto',)
    extra = 0
    tab = True


@admin.register(Produto)
class ProdutoAdmin(ModelAdmin):
    list_display = ('sigla', 'descricao', 'estoque', 'ativo', 'categoria', 'quantidade', 'unidade', 'porcao',)
    list_filter = ('categoria',)
    search_fields = ('sigla', 'descricao',)
    ordering = ('sigla',)
    inlines = [ComposicaoInline, FormacaoInline, PrecoInline, EmbalagemInline]
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


@admin.register(Compra)
class CompraAdmin(ModelAdmin):
    list_display = ('data', 'valor', 'fornecedor', 'situacao', 'periodo')
    list_filter = ('situacao', 'periodo', 'fornecedor',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    inlines = [VolumeInline]
    list_per_page = 12


@admin.register(Producao)
class ProducaoAdmin(ModelAdmin):
    list_display = ('periodo', 'data', 'produto', 'quantidade', 'produzido', 'situacao')
    list_filter = ('periodo', 'situacao', 'produto')
    ordering = ('-data',)
    date_hierarchy = 'data'
    list_per_page = 12


@admin.register(Manufatura)
class ManufaturaAdmin(ModelAdmin):
    list_display = ('periodo', 'data', 'acessorio', 'quantidade', 'produzido', 'situacao')
    list_filter = ('periodo', 'situacao', 'acessorio')
    ordering = ('-data',)
    date_hierarchy = 'data'
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
    list_display = (
    'periodo', 'data', 'valor', 'vencimento', 'pagamento', 'fornecedor', 'compra', 'descricao', 'situacao', 'valorpago',
    'operacao')
    list_select_related = ('fornecedor', 'periodo', 'compra', 'operacao')
    list_filter = ('situacao', 'fornecedor',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    list_per_page = 6
    resource_classes = [ContasaPagarResource]


class ContasaReceberResource(resources.ModelResource):
    class Meta:
        model = Contasareceber


@admin.register(Contasareceber)
class ContasareceberAdmin(ExportMixin, ModelAdmin):
    list_display = (
    'periodo', 'data', 'valor', 'vencimento', 'pagamento', 'cliente', 'pedido', 'descricao', 'situacao', 'valorpago',
    'operacao')
    list_select_related = ('periodo', 'cliente', 'pedido', 'operacao')
    list_filter = ('situacao', 'cliente',)
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


