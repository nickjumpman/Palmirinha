from django.contrib import admin

from django.utils.html import mark_safe


from ReceitaApp.models import Receita,Categoria

# Register your models here.
class ReceitaAdmin(admin.ModelAdmin):
    list_display= ['id', 'nome', 'categoria' ]
    # colunas com link pra editar
    list_display_links= ['id', 'nome']
    
    # colunas para filtro
    list_filter=['nome', 'categoria']

    search_fields=['nome']
    


class CategoriaAdmin(admin.ModelAdmin):
    list_display=['id', 'nome']
    list_display_links=['id','nome']
    search_fields=['nome']

admin.site.register(Receita,ReceitaAdmin)
admin.site.register(Categoria,CategoriaAdmin)
