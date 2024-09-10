from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
        return reverse('pro_detail', args=[self.id])



# class ActiveCommentManager(models.Manager):
#     def get_queryset(self):
#         return super(ActiveCommentManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
            ('1', _("VERY BAD")),
            ('1', _("BAD")),
            ('1', _("Normal")),
            ('1', _("Good")),
            ('1', _( "VERY Good")),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name= _('comment text'))
    stars = models.CharField(max_length=10, choices= PRODUCT_STARS, verbose_name=_("your's score"))
    active = models.BooleanField(default=True)

    #manager
    # objects = models.Manager()
    # active_comments_manager = ActiveCommentManager()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('pro_detail', args = [self.product.id])
    



    
    


