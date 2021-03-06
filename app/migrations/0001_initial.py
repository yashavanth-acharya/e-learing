# Generated by Django 3.0.5 on 2021-09-11 19:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('contactusid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', models.CharField(max_length=14)),
                ('msg', models.CharField(max_length=600)),
                ('create_At', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('courseid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('icon', models.TextField()),
                ('coursename', models.CharField(max_length=200, unique=True)),
                ('course_Descriptions', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('create_At', models.DateTimeField(auto_now_add=True)),
                ('updated_At', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('topicid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('icon', models.TextField()),
                ('topicname', models.CharField(max_length=200, unique=True)),
                ('topic_Descriptions', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
                ('marks_for_pre_question', models.FloatField()),
                ('minimum_mark', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('create_At', models.DateTimeField(auto_now_add=True)),
                ('updated_At', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('userid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', models.CharField(max_length=14)),
                ('date_of_birth', models.DateTimeField()),
                ('address', models.CharField(max_length=500)),
                ('pincode', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('user_role', models.CharField(default='user', max_length=100)),
                ('create_At', models.DateTimeField(auto_now_add=True)),
                ('updated_At', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topicsdocuments',
            fields=[
                ('documentid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('document', models.TextField()),
                ('create_At', models.DateTimeField(auto_now_add=True)),
                ('updated_At', models.DateTimeField(auto_now=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Topics')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('Resultid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=200)),
                ('totalmark', models.CharField(max_length=200)),
                ('outof', models.CharField(max_length=200)),
                ('submitted_time', models.DateTimeField()),
                ('feedback_status', models.BooleanField(default=False)),
                ('create_At', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='app.Userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('questions', models.CharField(max_length=1000)),
                ('options', models.TextField()),
                ('correct_answer', models.CharField(max_length=500)),
                ('create_At', models.DateTimeField(auto_now_add=True)),
                ('updated_At', models.DateTimeField(auto_now=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Topics')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('Feedbackid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.UUIDField()),
                ('Feedback', models.CharField(max_length=600)),
                ('create_At', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Topics')),
            ],
        ),
    ]
