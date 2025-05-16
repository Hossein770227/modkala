from django.shortcuts import render

def mobile_list(request):
    return render(request, 'mobile/mobile_list.html')
