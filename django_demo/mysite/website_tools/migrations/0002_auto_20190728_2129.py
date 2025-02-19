# Generated by Django 2.2.3 on 2019-07-28 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website_tools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_tex',
            field=models.CharField(max_length=200, verbose_name='新增选项'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question_text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website_tools.Question', verbose_name='选择问题'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='票数'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='问题'),
        ),
    ]
