from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(verbose_name='标签',max_length=12)

    def __str__(self):
        return self.name


class BlogManage(models.Manager):
    def category_count(self, keyword):
        return self.filter(category__icontains=keyword).count()


class Blog(models.Model):
    title = models.CharField('标题',max_length=32)
    category = models.CharField(max_length = 50, blank = True,verbose_name='分类')
    content = models.TextField('正文')
    create = models.DateTimeField(verbose_name='发布时间',auto_now_add=True)
    tag = models.ManyToManyField(Tag,verbose_name='标签')
    Author = models.CharField(blank=True,null=True,max_length=16)
    objects = BlogManage()

    def __str__(self):
        return self.title

    class Meta(object):
        ordering = ['-create']


class Comment(models.Model):
    blog = models.ForeignKey(Blog,verbose_name='博客')
    name = models.CharField('名字',max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('评论',max_length=50)
    create = models.DateTimeField(verbose_name='评论时间',auto_now_add=True)





