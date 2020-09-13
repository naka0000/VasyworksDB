"""
System Name: Vasyworks
Project Name: vacancy_model
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ElementarySchool(models.Model):
    """
    小学校区
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    pref_id = models.IntegerField(_('pref_id'), db_column='pref_id', db_index=True, default=0)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    kana = models.CharField(_('kana'), db_column='kana', db_index=True, max_length=100, null=True, blank=True)
    lat = models.FloatField(_('lat'), db_column='lat', db_index=True, default=0)
    lng = models.FloatField(_('lng'), db_column='lng', db_index=True, default=0)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'elementary_school'
        ordering = ['pref_id', 'kana', 'id']
        verbose_name = _('elementary_school')
        verbose_name_plural = _('elementary_schools')
