from django.db import models
from django.urls import reverse
from accounts.models import User


# Create your models here.


# 북마크
class Bookmark(models.Model):
    name = models.CharField(max_length=50, help_text="북마크")

    def __str__(self):
        return self.name


# 폴더
class Folder(models.Model):
    name = models.CharField(max_length=100, help_text="폴더")

    def __str__(self):
        return self.name


# 글(제목, 작성일, 내용, 북마크, 폴더)
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)    # 작성일자동입력
    updateDate = models.DateTimeField(auto_now_add=True)    # 수정일자동입력
    # 북마크와 글은 1:N 관계이므로 ForeignKey 사용
    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE)
    # 폴더와 글은 다대다 관계이므로 ManyToManyField 사용 (M2M에선 on_delete 옵션을 사용하지 않는다고 함)
    # 폴더를 설정하지 않을 수 있고 폴더가 삭제되더라도 포스트는 삭제되지 않음
    folder = models.ManyToManyField(Folder, blank=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.pk)])

    class Meta:
        db_table = 'forum_post'
        verbose_name = '게시물'
        verbose_name_plural = '게시물'
