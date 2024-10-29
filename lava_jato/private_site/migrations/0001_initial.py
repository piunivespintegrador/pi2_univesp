# Generated by Django 4.2.16 on 2024-10-29 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_inicio', models.DateTimeField()),
                ('datetime_fim', models.DateTimeField()),
                ('disponivel', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'agendamento',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email_contato_1', models.EmailField(max_length=254)),
                ('email_contato_2', models.EmailField(blank=True, max_length=20, null=True)),
                ('telefone_contato_1', models.CharField(max_length=20)),
                ('telefone_contato_2', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='FormaContato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'forma_contato',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField(blank=True, null=True)),
                ('valor_servico', models.DecimalField(decimal_places=2, max_digits=10)),
                ('agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='private_site.agendamento')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='private_site.cliente')),
            ],
            options={
                'db_table': 'servico',
            },
        ),
        migrations.CreateModel(
            name='TipoServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_servico', models.CharField(max_length=100)),
                ('valor_servico', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'tipo_servico',
            },
        ),
        migrations.CreateModel(
            name='TipoVeiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_veiculo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tipo_veiculo',
            },
        ),
        migrations.CreateModel(
            name='ServicoFormaContato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_contato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='private_site.formacontato')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='private_site.servico')),
            ],
            options={
                'db_table': 'servico_forma_contato',
            },
        ),
        migrations.AddField(
            model_name='servico',
            name='tipo_servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='private_site.tiposervico'),
        ),
        migrations.AddField(
            model_name='servico',
            name='tipo_veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='private_site.tipoveiculo'),
        ),
    ]
