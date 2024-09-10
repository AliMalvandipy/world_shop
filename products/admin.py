from django.contrib import admin
from .models import Product,Comment

class CommentsInline(admin.TabularInline):
    model = Comment
    fields =['author', 'product', 'body', 'active',]
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['tittle','price', 'active', ]
    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =['author', 'product', 'body', 'active', ]

