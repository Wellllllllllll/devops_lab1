from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class HelloView(View):
    def get(self, request):
        context = {}
        return render(request, 'devops/hello.html', context)
