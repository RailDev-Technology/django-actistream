from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actistream', '0002_notice_index_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='target_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='verb',
            field=models.CharField(max_length=200)
        ),
    ]