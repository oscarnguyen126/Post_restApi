# Generated by Django 4.2.6 on 2023-10-14 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0002_rename_posttype_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, help_text='name', max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='meta_keyword',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.ForeignKey(blank=True, help_text='post type', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post', to='post_app.category'),
        ),
    ]
