# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models


class BaseModel(models.Model):
    """
    Base Model.

    This model is created the store the time of creation and update.
    """
    created = models.DateTimeField(verbose_name="Creacion", auto_now_add=True, default=datetime.now)
    updated = models.DateTimeField(verbose_name="Actualizacion", auto_now=True, default=datetime.now)

    class Meta:
        abstract = True


class OrderedModel(BaseModel):
    """
    OrderedModel.

    This model is created the store the order and to offer basic functionallity.
    See https://djangosnippets.org/snippets/2306/ for more info.
    """
    position = models.PositiveSmallIntegerField(verbose_name="Posicion")

    def save(self, *args, **kwargs):
        model = self.__class__
        if self.position is None or self.position == 0:
            try:
                last = model.objects.order_by("-position")[0]
                self.position = last.position + 1
            except IndexError:
                self.position = 0
        return super(OrderedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ("position",)