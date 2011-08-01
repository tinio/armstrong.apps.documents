from django.db import models
from django.conf import settings

from armstrong.apps.content.models import Content
from armstrong.core.arm_content.mixins.publication import PublishedManager


class Document(Content):
    file = models.FileFieled(upload_to=settings.DOCUMENTS_PATH)
     
    published = PublishedManager()
