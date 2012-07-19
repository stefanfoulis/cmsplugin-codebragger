#-*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin
from codebragger.models import Project


class CodebraggerProjectTeaser(CMSPlugin):
    project = models.ForeignKey(Project)
    show_subprojects = models.BooleanField(default=False)
    show_contributors = models.BooleanField(default=False)
