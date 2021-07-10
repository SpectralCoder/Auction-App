# Generated by Django 3.2.3 on 2021-07-10 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('password1', models.CharField(max_length=255)),
                ('password2', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proname', models.CharField(max_length=255)),
                ('minbid', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.CharField(max_length=2000, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created', models.DateTimeField()),
                ('date', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_requests_created', to='mainapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('date', models.DateTimeField()),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.item')),
            ],
        ),
    ]