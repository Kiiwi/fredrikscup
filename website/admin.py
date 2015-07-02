# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Registration, Team


class RegistrationAdmin(admin.ModelAdmin):
    class Meta:
        model = Registration

admin.site.register(Registration, RegistrationAdmin)


class TeamAdmin(admin.ModelAdmin):
    class Meta:
        model = Team

admin.site.register(Team, TeamAdmin)