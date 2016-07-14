#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import connection

from .models import Blog
from .models import Category
from .models import Friend


def tag_list(request):
    """
    获取每个标签的文章数量，sqlite不支持right join on
    """
    cursor = connection.cursor()
    sql = "SELECT title, c FROM (\
                        SELECT tag_id AS tid, COUNT(*) AS c \
                        FROM blog_blog_tags GROUP BY tag_id) AS t2 \
                        LEFT JOIN blog_tag ON blog_tag.id=t2.tid";
    cursor.execute(sql)
    tags = cursor.fetchall()
    ctx = {'tags': [tag[0] for tag in tags]}
    return ctx


def google_analytics(request):
    from django.conf import settings
    return {'ga_id': settings.GOOGLE_ANALYTICS_ID, 'disqus_name': settings.DISQUS_NAME}


def recent_blog_list(request):
    """
    最近文章列表
    """

    # 最近发布的文章列表
    recent_blogs = Blog.objects.filter(status='p', is_public=True).order_by('-publish_time')[:10]

    # 分类
    categories = Category.objects.all()

    # 友情链接
    friends = Friend.objects.filter(active=True).order_by('position')

    return {'recent_blogs': recent_blogs, 'categories': categories, 'friends': friends}
