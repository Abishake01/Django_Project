from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
arr=['Python','Java','C','C++','Mysql','DataBase','HTML','CSS','JavaScript','TailwindCss','Django','React','Node.JS']
def vote(request):
    mydic={
        'arr': arr
    }
    return render(request,'main.html',context=mydic)
def getquery(request):
    q=request.GET['languages']
    return HttpResponse(q)