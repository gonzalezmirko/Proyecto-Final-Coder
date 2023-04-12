# Generated by Django 4.1.7 on 2023-04-08 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_mueble_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='mueble',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='\\core\\images\\media'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='core.mueble')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
    ]
