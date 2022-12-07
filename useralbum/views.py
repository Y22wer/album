from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect, render
from .models import *
from .forms import *
import os

class test(View):
    def get(self, request):
        form = UserForm()
        return render (request,"test.html",locals())
    def post(self, request):
        formed =UserForm( request.POST)
        if formed.is_valid():
            formed.save()
        else:
            formed.erros
      
    
class index(View):
    def get(self, request):
        print(request.session.get("user") ) 
        #print(request.session["id"])  #這樣取值如果沒有安排，就會抱錯
        print(request.session.get("id") )   # 所以呢 如果傳回空，則進行網頁跳轉 
        return render (request,"cover.html",locals())
    

class start(View):
    def get(self, request):
        yilong=User.objects.get(id=1)
        photos=Photo.objects.filter(user=yilong)
        for i in photos   :
            print( i.user_id)
            print( i.user.usermail)
            print( i.user) #默認主見
            
        
        return render (request,"albumcopy.html",locals())
    
class addpicture(View):
    yilong=User.objects.get(id=1)
    photos=Photo.objects.filter(user=yilong)
    def get(self, request):
        photoform=PhotoForm()
        return render (request,"addphoto.html",locals())
    
    def post(self, request):
        if request.POST.get("mypassword") != "嫩嫩XD哈哈" :
            print( request.POST.get("mypassword") )
            return redirect ('/start')
        print( request.POST.get("desc") )
        Photo.objects.create( user=User.objects.get(id=1)  , photo=request.FILES.get("photo") , desc=request.POST.get("desc"))
        return redirect ('/start')    #重定向回首頁
from album.settings import MEDIA_Root
class delete(View):
    yilong=User.objects.get(id=1)
    photos=Photo.objects.filter(user=yilong)
    def get(self, request ,iid):
        Photo.objects.get(id = iid).delete()
        return  redirect ('/start')
class update(View):
    def get(self, request ,iid):
        photo=Photo.objects.get(id = iid)
        url= "http://127.0.0.1:8000/"+str(photo.photo)
        print(url)
        
        return  render (request,"update.html",locals())
    def post(self, request,iid):
        updatedesc=request.POST.get("updatedesc")
        print( request.POST.get("updatedesc") )
        Photo.objects.filter( user=User.objects.get(id=1), id=iid).update(desc =updatedesc )
        return redirect ('/start')




class register(View):
    def get(self, request):
        userform =UserForm()
        return render (request,"register.html",locals())
    def post(self, request):
        postform=UserForm(request.POST)
        
        if postform.is_valid():
            nwe_user_data=postform.cleaned_data # {'username': 'QQ', 'usermail': 'asdzxc@asdasd.cdfas', 'password': '3212313'}
        else:    
            return render (request,"register.html",{"userform":postform})
        
        if User.objects.filter(usermail=nwe_user_data['usermail']):
            error="此信箱已經註冊"
            return render (request,"register.html",{"userform":postform ,"error":error })
           
        User.objects.create(**nwe_user_data) #好像可以調用表格的SAVE方法
       
        return redirect ('/login')# 重定向回新的相簿
         
class login(View):
    def get(self, request):
        if request.session.get("user") != None  :
            # print(request.session.get("user"))
            print("目前已登入")
            return redirect ('../')
        return render (request,"login.html",locals())
    def post(self,request):
        user_mail=request.POST["usermail"] 
        pass_word=request.POST["password"] 
        if User.objects.filter(usermail=user_mail , password=pass_word):
            user=User.objects.get(usermail=user_mail , password=pass_word)
            request.session["user"]= {'name':user.username , "id":user.id , "mail" :user.usermail}
            request.session.set_expiry(60*60*24)
            return redirect ('../')
        else:
            usererror="信箱或密碼錯誤"
            return render (request,"login.html",locals())

class logout (View):
    def get(self, request):
        request.session.flush()
        return redirect ('../')
