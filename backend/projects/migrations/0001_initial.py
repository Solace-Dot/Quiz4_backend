from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('project_description', models.TextField()),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('IN PROGRESS', 'In Progress'), ('OVERDUE', 'Overdue'), ('COMPLETED', 'Completed')], default='CREATED', max_length=20)),
                ('hours_consumed', models.PositiveIntegerField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
