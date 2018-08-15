from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
import markdown
from django.views.generic import ListView

# 首页
def handmadeView(request):
    return render(request, 'handmade/index.html', context={})
