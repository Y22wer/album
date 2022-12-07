from django.db import models

# Create your models here.
class User(models.Model):
    usermail = models.EmailField(verbose_name="用戶信箱",max_length=100)
    username = models.CharField(verbose_name="用戶名稱",max_length=20)
    password = models.CharField(verbose_name="用戶密碼",max_length=20)

    def __str__(self):
        return self.usermail

    class Meta:
        db_table = 'tb_User'
        

class Photo (models.Model): 
    user= models.ForeignKey( User , to_field="id",on_delete=models.CASCADE )
    # 目前是 user 其實是上表的ID 不是用戶信箱 
    #.use 屬性可以關聯回去原表，可再用    i.user.usermail  取得  i 是photo 實力對象
    photo =models.ImageField(upload_to="static/media/")
    desc = models.TextField()
    upload_time=models.DateTimeField (auto_now_add=True) 
    def __str__(self):
        return self.desc
    