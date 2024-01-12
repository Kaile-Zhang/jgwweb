from django.shortcuts import render, HttpResponse, redirect
import os, json

def query(word):
    with open(os.path.join(os.getcwd(), 'jgw', 'static', 'Chars.json'), 'r', encoding='utf-8') as f:
        chars = json.loads(f.read())
    if word in chars:
        flag = True
        with open(os.path.join(os.getcwd(), 'jgw', 'static', 'EVOBC.json'), 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        for i in data:
            if i["character"] == word:
                images = i["images"]
        
        imgs = {}
        eras = ['甲骨文', '金文', '篆文', '春秋', '战国', '隶书']
        for i in eras:
            imgs[i] = []
        for image in images:
            imgs[eras[image["era"]]].append(f"http://27.18.7.167:7680/img/{word}/{image['file']}")
    else:
        flag = False
        imgs = {}
    
    return flag, imgs

# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request, 'index.html', {'flag': False})
    else:
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        message = request.POST.get('message','')
        with open(os.path.join(os.getcwd(), 'jgw', 'static', 'messages.txt'), "a") as file:
            file.write(name+','+email+','+message+'\n')
        return render(request, 'index.html', {'flag': True})

def Search(request):
    word = request.GET.get('q')
    flag, imgs = query(word)
    dic = {'word': word,
           'flag': flag,
           'imgs': imgs,}
    # print(imgs)
    return render(request, 'Search.html', dic)

def evolution(request):
    return HttpResponse("可视化")
