# Generated by Django 2.2.6 on 2020-04-30 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200430_0329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='books.Tag'),
        ),
    ]
