from django.db import models
from uuid import uuid4 as UUID4
from django.utils.timezone import now as djnow
from account.models import Account


class Country(models.Model):
    uuid = models.UUIDField(default=UUID4,
                            editable=False,
                            primary_key=True)
    name = models.CharField(max_length=100,
                            unique=True,
                            blank=True,
                            null=True)
    code = models.CharField(max_length=256, unique=True)
    active = models.BooleanField(default=False)
    description = models.TextField(max_length=100,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="description")
    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text="created at")
    updated_at = models.DateTimeField(default=djnow,
                                      help_text="updated at")

    create_by =  models.ForeignKey(Account, related_name="create_country",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="created by")
    updated_by = models.ForeignKey(Account, related_name="update_country",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="updated by")

    def __str__(self):
        return self.name


class Language(models.Model):
    uuid = models.UUIDField(default=UUID4,
                            editable=False,
                            primary_key=True)
    name = models.CharField(max_length=100,
                            unique=True,
                            blank=True,
                            null=True)
    code = models.CharField(max_length=256, unique=True)
    description = models.TextField(max_length=100,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="description")
    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text="created at")
    updated_at = models.DateTimeField(default=djnow,
                                      help_text="updated at")

    create_by =  models.ForeignKey(Account, related_name="create_language",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="created by")
    updated_by = models.ForeignKey(Account, related_name="update_language",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="updated by")

    def __str__(self):
        return self.name