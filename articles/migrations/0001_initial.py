# Generated by Django 4.1.2 on 2022-10-19 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_sub_title', models.CharField(max_length=200)),
                ('article_body', models.TextField()),
                ('article_pub_date', models.DateTimeField()),
                ('article_banner', models.ImageField(upload_to='media/images/')),
                ('article_votes', models.IntegerField(default=1)),
            ],
        ),
    ]
