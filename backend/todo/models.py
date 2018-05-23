#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models


class Tarefa(models.Model):
    descricao = models.CharField(max_length=100)
    concluido = models.BooleanField(default=False)
    excluido = models.BooleanField(default=False)
    data_concluido = models.DateTimeField(null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        concluido_str = 'concluido'
        if not self.concluido:
            concluido_str = 'pendente'

        return '{} ({})'.format(self.descricao, concluido_str)
