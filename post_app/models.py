from django.db import models
from uuid import uuid4 as UUID4
from django.utils.timezone import now as djnow
from account.models import Account


class PostStatus(models.Model):
    uuid = models.UUIDField(default=UUID4,
                            editable=False,
                            primary_key=True)
    code = models.CharField(max_length=256, unique=True)
    name =  models.CharField(max_length=100,
                            null=True,
                            blank=True,
                            help_text="name")
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

    create_by =  models.ForeignKey(Account, related_name="create_status",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="created by")
    updated_by = models.ForeignKey(Account, related_name="update_status",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="updated by")
    
    def __str__(self):
        return self.name

    # def save(self):
    #     self.updated_at = djnow()
    #     super().save(self)


class Category(models.Model):
    uuid = models.UUIDField(default=UUID4,
                            editable=False,
                            primary_key=True)
    code = models.CharField(max_length=256, unique=True)
    name =  models.CharField(max_length=100,
                            null=True,
                            blank=True,
                            unique=True,
                            help_text="name")
    description = models.TextField(max_length=100,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="description")
    url = models.CharField(max_length=256, null=True, blank=True, help_text='url')
    created_by = models.ForeignKey(Account, related_name="create_type",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="created by")
    updated_by = models.ForeignKey(Account, related_name="update_type",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="updated by")
    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text="created at")
    updated_at = models.DateTimeField(default=djnow,
                                      help_text="updated at")
    
    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     self.updated_at = djnow()
    #     super().save(self,  *args, **kwargs)
    

class Post(models.Model):
    uuid = models.UUIDField(default=UUID4,
                            editable=False,
                            primary_key=
                            True)
    code = models.CharField(max_length=256, unique=True)
    name =  models.CharField(max_length=100,
                            null=True,
                            blank=True,
                            help_text="name")
    title = models.CharField(max_length=256,
                             unique=True,
                             null=True,
                             blank=True,
                             editable=True,
                             help_text="title")
    description = models.TextField(max_length=2048,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="description")
    thumbnail = models.ImageField()
    meta_keyword = models.CharField(max_length=256)
    type = models.ForeignKey(Category, related_name='post_type',
                             null=True,
                             blank=True,
                             on_delete=models.SET_NULL,
                             help_text='post type')
    status = models.ForeignKey(PostStatus, related_name='post_status',
                               on_delete=models.SET_NULL,
                               null=True,
                               help_text='post status')
    keyword = models.CharField(max_length=256, null=True, blank=True, help_text="keyword")
    short_content = models.TextField(max_length=2048,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="short content")
    content = models.TextField(max_length=2048,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="short content")
    slug = models.SlugField(default="", null=False)
    created_by = models.ForeignKey(Account, related_name="create_post",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="created by")
    updated_by = models.ForeignKey(Account, related_name="update_post",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   help_text="updated by")
    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text="created at")
    updated_at = models.DateTimeField(default=djnow,
                                      help_text="updated at")
    
    IS_DELETE_CHOICES = (
        (0, 'no'),
        (1, 'yes'),
    )

    def __str__(self):
        return self.title

    def save(self):
        self.updated_at = djnow()
        super().save(self)
