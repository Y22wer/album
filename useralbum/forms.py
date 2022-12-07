from django.forms import *
from .models import *
# class userform(forms.ModelForm):
#     class Meta:
#         model = User
#         fields= ['all',]

class Bootstrap():
    def __init__(self , *args, **kwargs) :
            super().__init__(*args, **kwargs)
            for name , field in self.fields.items():    
                #原本的字段有其他屬性
                if field.widget.attrs:
                    field.widget.attrs["class"]='form-control'
                    field.widget.attrs['placeholder']=field.label
                    
                else:
                    field.widget.attrs={
                        "class": 'form-control' , 
                        'placeholder': field.label
                        }


class UserForm(Bootstrap,ModelForm):
    password = widgets.PasswordInput()
    class Meta:
        model = User
        fields= ['username', 'usermail','password', ]
        widgets = {
            'password': PasswordInput(attrs={'cols': 80, 'rows': 20}), # 关键是这一行
        }
        #<input type="text" name="username" maxlength="20" required="" id="id_username">
        # 實力化後對其循環，則會按照fields裡面的參數逐一顯示 form.username/password  .lebel 則會跑出資料庫的verbose_name 
        #循環所有場，並添加上class='form-control'
        

class PhotoForm(Bootstrap,ModelForm):
    class Meta:
        model = Photo
        fields= ['desc', 'photo' ]
        