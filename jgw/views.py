from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'test.html')

def query(request):
    return HttpResponse("甲骨文查询")

def radical(request):
    return HttpResponse("部首匹配")

def evolution(request):
    return HttpResponse("演变分析")

def visualization(request):
    return HttpResponse("可视化")
