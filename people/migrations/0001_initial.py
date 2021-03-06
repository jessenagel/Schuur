# Generated by Django 3.0.6 on 2020-05-11 19:20

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('license_type', multiselectfield.db.fields.MultiSelectField(choices=[('AM', 'AM (Very lightweight motorbike)'), ('A1', 'A1 (Lightweight motorbike)'), ('A2', 'A2 (Middleweight motorbike)'), ('A', 'A (All motorbikes)'), ('B1', 'B1 (Light cars)'), ('B', 'B (Cars)'), ('C1', 'C1 (Lightweight trucks)'), ('C', 'C (Trucks)'), ('D1', 'D1 (Lightweight touring cars'), ('D', 'D (Touring Cars)'), ('BE', 'BE (Trailers for cars)'), ('C1E', 'C1E (Trailers for lightweight trucks)'), ('CE', 'CE (Trailers for trucks)'), ('D1E', 'D1E (Trailers for lightweight touring cars)'), ('DE', 'DE (Trailers for touring cars)'), ('T', 'T (Agricultural vehicles)'), ('OC', 'Non-European car'), ('OM', 'Non-European motorbike'), ('OTR', 'Non-European truck'), ('OTC', 'Non-European touring car'), ('OA', 'Non-European touring agricultural')], max_length=70, verbose_name='License Type(s)')),
            ],
        ),
    ]
