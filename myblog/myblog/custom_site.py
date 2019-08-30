# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = "我的博客"
    site_title = "我的博客 后台管理"
    index_title = '首页'

custom_site = CustomSite(name='cus_admin')