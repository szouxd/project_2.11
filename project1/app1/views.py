from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
import time
# Create your views here.

def index(request):
    try:
        context = {'title':'测试模板处理数据'}
        return render(request,'index.html')
    except Exception as e:
        print(e)

def json(request):
    # time.sleep(5)
    try:
        a = request.GET
        time.sleep(5)
        print(a, time.time())
        return JsonResponse({'data': {'a': 1,'b':2,'c':3}})
    except Exception as e:
        print(e)


