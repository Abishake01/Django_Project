from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
 
def cal(request):
    return render(request,'index.html')
 
def submitquery(request):
    q=request.GET['query']
    return HttpResponse(q)

''' q=request.GET['query']
    jsondic={
        'q':q
    }
    return JsonResponse(jsondic) 
    It is a Json Dictionary
'''