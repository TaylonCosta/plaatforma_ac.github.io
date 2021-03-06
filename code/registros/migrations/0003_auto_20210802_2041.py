# Generated by Django 2.2.14 on 2021-08-02 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registros', '0002_auto_20210802_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='doc_comprobatoria',
            field=models.TextField(max_length=250),
        ),
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=80)),
                ('descricao', models.TextField(blank=True, max_length=250, null=True)),
                ('total_de_horas', models.IntegerField()),
                ('horas_convertidas', models.FloatField(blank=True, null=True)),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.Atividade')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.Categoria')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='certificado_informer', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='certificado_updater', to=settings.AUTH_USER_MODEL)),
                ('nivel_participacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.NivelParticipacao')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'certificado',
                'verbose_name_plural': 'certificados',
            },
        ),
    ]
