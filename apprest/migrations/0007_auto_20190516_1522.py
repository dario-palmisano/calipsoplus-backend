# Generated by Django 2.1.3 on 2019-05-16 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0006_auto_20190327_1017'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CalipsoFacility',
        ),
        migrations.RemoveField(
            model_name='historicalcalipsofacility',
            name='history_user',
        ),
        migrations.AddField(
            model_name='calipsocontainer',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apprest.CalipsoAvailableImages'),
        ),
        migrations.AddField(
            model_name='historicalcalipsocontainer',
            name='image',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='apprest.CalipsoAvailableImages'),
        ),
        migrations.DeleteModel(
            name='HistoricalCalipsoFacility',
        ),
    ]