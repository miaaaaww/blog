from django.shortcuts import render

def post_list(request):
    return render(request, 'blogg/post_list.html', {})
