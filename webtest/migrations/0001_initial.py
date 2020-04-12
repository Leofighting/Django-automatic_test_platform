# Generated by Django 2.0.13 on 2020-04-12 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_case_name', models.CharField(max_length=64, verbose_name='用例名称')),
                ('web_test_result', models.BooleanField(verbose_name='测试结果')),
                ('web_tester', models.CharField(max_length=24, verbose_name='测试负责人')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': 'web 测试用例',
                'verbose_name_plural': 'web 测试用例',
            },
        ),
        migrations.CreateModel(
            name='WebCaseStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_case_name', models.CharField(max_length=100, verbose_name='测试用例标题')),
                ('web_test_step', models.CharField(max_length=255, verbose_name='测试步骤')),
                ('web_test_obj_name', models.CharField(max_length=200, verbose_name='测试对象名称描述')),
                ('web_find_method', models.CharField(max_length=200, verbose_name='定位方式')),
                ('web_element', models.CharField(max_length=800, verbose_name='控件元素')),
                ('web_opt_method', models.CharField(max_length=200, verbose_name='操作方法')),
                ('web_test_data', models.CharField(max_length=200, null=True, verbose_name='测试数据')),
                ('web_assert_data', models.CharField(max_length=200, verbose_name='验证数据')),
                ('web_test_result', models.BooleanField(verbose_name='测试结果')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('web_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webtest.WebCase')),
            ],
        ),
    ]
