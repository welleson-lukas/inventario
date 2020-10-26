# Generated by Django 2.2.16 on 2020-10-15 19:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='garantia',
            options={'verbose_name': 'Garantia', 'verbose_name_plural': 'Garantia'},
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='ano_fab',
            field=models.DateField(blank=True, null=True, verbose_name='Ano de Fabricação'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='atualizado',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='data_aquisicao',
            field=models.DateField(blank=True, null=True, verbose_name='Data de aquisição'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='data_cadastro',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Data de cadastro'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='end_ip',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Endereço IP'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='memoria_mb',
            field=models.CharField(blank=True, choices=[('2GBb', '2Gb'), ('4GBb', '4Gb'), ('6GBb', '6Gb'), ('8GBb', '8Gb'), ('10GBb', '10Gb'), ('12GBb', '12Gb'), ('16GBb', '16Gb')], max_length=20, null=True, verbose_name='Memoria em GB'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='n_invent',
            field=models.CharField(max_length=5, verbose_name='Nº Patrimônio'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='n_serie',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Nº Série'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='nome_host',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Nome do Host'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='processdor_ghz',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Processador em Ghz'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='so_instalado',
            field=models.CharField(blank=True, choices=[('Windows 7', 'Windows 7'), ('Windows 8', 'Windows 8'), ('Windows 10', 'Windows 10'), ('Linux', 'Linux')], max_length=20, null=True, verbose_name='Sistema Operacional'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='tipo_memoria',
            field=models.CharField(blank=True, choices=[('DDR', 'DDR'), ('DDR2', 'DDR2'), ('DDR3', 'DDR3'), ('DDR4', 'DDR4'), ('DDR5', 'DDR5')], max_length=20, null=True, verbose_name='Tipo de memoria'),
        ),
        migrations.AlterField(
            model_name='garantia',
            name='descricao',
            field=models.CharField(max_length=700, verbose_name='Descrição da garantia'),
        ),
    ]
