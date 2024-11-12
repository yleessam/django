from django.db import models

# Create your models here.
class Post(models.Model):  #1
    title = models.CharField("포스트 제목", max_length=100)
    content = models.TextField("포스트 내용")
    thumbnail = models.ImageField("썸네일이미지", upload_to='post', blank=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model): #N - 1의 id 를 가져야 한다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")
    
    def __str__(self):
        return f'{self.post.title} 의 댓글 (id: {self.id})'