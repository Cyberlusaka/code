# Generated by Django 2.2.1 on 2024-01-16 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='账号')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.CreateModel(
            name='xiangmu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='新能源汽车名称')),
                ('c2', models.CharField(max_length=255, verbose_name='价格')),
                ('c3', models.CharField(max_length=255, verbose_name='地区')),
                ('c4', models.DateField(verbose_name='上架日期')),
                ('c5', models.CharField(max_length=1024, verbose_name='新能源汽车评分')),
                ('c6', models.IntegerField(verbose_name='评价数')),
                ('c7', models.CharField(max_length=255, verbose_name='新能源汽车评分')),
                ('c8', models.TextField(verbose_name='描述')),
                ('c9', models.IntegerField(default=0, verbose_name='新能源汽车浏览量')),
                ('c10', models.TextField(verbose_name='图片')),
                ('c11', models.TextField(verbose_name='图片')),
                ('c12', models.TextField(verbose_name='图片')),
                ('collect', models.ManyToManyField(blank=True, to='item.User', verbose_name='收藏者')),
                ('tags', models.ManyToManyField(blank=True, to='item.Tags', verbose_name='标签')),
            ],
            options={
                'verbose_name': '新能源汽车',
                'verbose_name_plural': '新能源汽车',
            },
        ),
        migrations.CreateModel(
            name='UserTagPrefer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Tags', verbose_name='标签名')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='item.User', verbose_name='用户id')),
            ],
            options={
                'verbose_name': '用户偏好',
                'verbose_name_plural': '偏好',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.FloatField(verbose_name='新能源汽车评分')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='item.xiangmu', verbose_name='新能源汽车id')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='item.User', verbose_name='用户id')),
            ],
            options={
                'verbose_name': '评分信息',
                'verbose_name_plural': '评分信息',
            },
        ),
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Comment', verbose_name='评论')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论点赞',
                'verbose_name_plural': '评论点赞',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.xiangmu', verbose_name='新能源汽车'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.User', verbose_name='用户'),
        ),
    ]
