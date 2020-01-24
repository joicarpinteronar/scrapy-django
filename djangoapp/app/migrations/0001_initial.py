
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mercado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('precio', models.TextField()),
                ('envio', models.TextField()),
                ('vendido', models.TextField()),
                ('opiniones', models.TextField()),
            ],
        ),
    ]
