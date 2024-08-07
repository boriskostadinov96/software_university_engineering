from django.db import migrations
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_zoodisplayanimal'),
    ]

    operations = [
        migrations.AddField(
            model_name='veterinarian',
            name='availability',
            field=main_app.models.BooleanChoiceField(choices=[(True, 'Available'), (False, 'Not Available')], default=True),
        ),
    ]