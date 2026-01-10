from django.contrib import admin

admin.site.site_header = 'Biano Alimentos'  # set header
admin.site.site_title = 'Biano Alimentos'   # set title
admin.site.index_title = 'Delivery'

from administrativo.models import *

@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
    list_display = ('descricao', )
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 15

@admin.register(Unidade)
class Unidade(admin.ModelAdmin):
    list_display = ('sigla', 'descricao', )
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 15

@admin.register(Segmento)
class Segmento(admin.ModelAdmin):
    list_display = ('descricao', )
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 15

@admin.register(Tipo)
class Tipo(admin.ModelAdmin):
    list_display = ('descricao', )
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 15

@admin.register(Cliente)
class Cliente(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'tipo', )
    list_filter = ('tipo',)
    search_fields = ('nome',)
    ordering = ('nome',)
    list_per_page = 15

@admin.register(Fornecedor)
class Fornecedor(admin.ModelAdmin):
    list_display = ('nome', 'contato')
    search_fields = ('nome',)
    ordering = ('nome',)
    list_per_page = 15

@admin.register(Indicador)
class Indicador(admin.ModelAdmin):
    list_display = ('descricao', 'formula')
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 15

@admin.register(Conta)
class Conta(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'natureza', 'nivel', 'tipo', 'saldoinicial')
    list_filter = ('natureza', 'nivel', 'tipo',)
    search_fields = ('descricao',)
    ordering = ('codigo',)
    list_per_page = 15

@admin.register(Operacao)
class Operacao(admin.ModelAdmin):
    list_display = ('sigla', 'descricao', 'debito', 'credito')
    list_filter = ('debito', 'credito',)
    search_fields = ('descricao',)
    ordering = ('sigla',)
    list_per_page = 15

@admin.register(Ingrediente)
class ingrediente(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'estoque', 'ativo', 'segmento', 'quantidade', 'unidade')
    list_filter = ('segmento',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 15

class ComponenteInline(admin.StackedInline):
    model = Componente
    extra = 0

@admin.register(Acessorio)
class Acessorio(admin.ModelAdmin):
    list_display = ('sigla', 'descricao', 'valor', 'estoque', 'ativo', 'quantidade', 'unidade', 'porcao', )
    search_fields = ('descricao',)
    ordering = ('descricao',)
    inlines = [ComponenteInline]
    list_per_page = 15


class ComposicaoInline(admin.StackedInline):
    model = Composicao
    extra = 0

class FormacaoInline(admin.StackedInline):
    model = Formacao
    extra = 0

class PrecoInline(admin.StackedInline):
    model = Preco
    extra = 0

@admin.register(Produto)
class Produto(admin.ModelAdmin):
    list_display = ('sigla', 'descricao', 'estoque', 'ativo', 'categoria', 'quantidade', 'unidade', 'porcao',)
    list_filter = ('categoria',)
    search_fields = ('descricao',)
    ordering = ('descricao',)
    inlines = [ComposicaoInline, FormacaoInline, PrecoInline]
    list_per_page = 15

@admin.register(Periodo)
class Periodo(admin.ModelAdmin):
    list_display = ('sigla', 'inicio', 'final', 'situacao')
    search_fields = ('sigla',)
    ordering = ('-inicio',)
    list_per_page = 12

class InsumoInline(admin.StackedInline):
    model = Insumo
    extra = 0

@admin.register(Compra)
class Compra(admin.ModelAdmin):
    list_display = ('data', 'valor', 'fornecedor', 'situacao', 'periodo')
    list_filter = ('fornecedor',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    inlines = [InsumoInline]
    list_per_page = 15

@admin.register(Producao)
class Producao(admin.ModelAdmin):
    list_display = ('periodo', 'data', 'produto', 'quantidade')
    list_filter = ('periodo', 'produto')
    ordering = ('-data',)
    date_hierarchy = 'data'
    list_per_page = 15

@admin.register(Manufatura)
class Manufatura(admin.ModelAdmin):
    list_display = ('periodo', 'data', 'acessorio', 'quantidade')
    list_filter = ('periodo', 'acessorio')
    ordering = ('-data',)
    date_hierarchy = 'data'
    list_per_page = 15

class ItemInline(admin.StackedInline):
    model = Item
    extra = 0

@admin.register(Pedido)
class Pedido(admin.ModelAdmin):
    list_display = ('data', 'valor', 'cliente', 'previsao', 'entrega', 'situacao', 'periodo')
    list_filter = ('cliente',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    inlines = [ItemInline]
    list_per_page = 15

class PacoteInline(admin.StackedInline):
    model = Pacote
    extra = 0

@admin.register(Carga)
class Carga(admin.ModelAdmin):
    list_display = ('data', 'periodo')
    ordering = ('-data',)
    date_hierarchy = 'data'
    inlines = [PacoteInline]
    list_per_page = 15

@admin.register(Lancamento)
class Lancamento(admin.ModelAdmin):
    list_display = ('data', 'valor', 'descricao', 'periodo', 'operacao')
    list_filter = ('operacao',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    list_per_page = 15

@admin.register(Contaapagar)
class Contaapagar(admin.ModelAdmin):
    list_display = ('periodo', 'data', 'valor', 'vencimento', 'pagamento', 'fornecedor', 'compra', 'descricao', 'situacao', 'operacao')
    list_filter = ('fornecedor', 'situacao')
    ordering = ('-data',)
    date_hierarchy = 'data'
    list_per_page = 15

@admin.register(Contasareceber)
class Contasareceber(admin.ModelAdmin):
    list_display = ('periodo', 'data', 'valor', 'vencimento', 'pagamento', 'cliente', 'pedido', 'descricao', 'situacao', 'operacao')
    list_filter = ('cliente', 'situacao')
    ordering = ('-data',)
    date_hierarchy = 'data'
    list_per_page = 15

