from django.db import models

"""CREATE TABLE posts(id serial primary key autoincrement, title varchar(256), content varchar(856), rate int);"""

class Post(models.Model):
    title = models.CharField(max_length=356)
    content = models.CharField(max_length=856)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f"{self.title} {self.content} {self.id}"
    



# Create your models here.
