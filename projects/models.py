import uuid

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)

    # blank is for Django to allow posting forms with empty values
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2002, null=True, blank=True)
    source_line = models.CharField(max_length=2000, null=True, blank=True)

    # timestamp of creation auto
    created = models.DateTimeField(auto_now_add=True)

    # editable false: cannot be changed
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
