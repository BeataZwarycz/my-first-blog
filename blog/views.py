from django.shortcuts import render

# Create your views here.
def post_list(request):
	#funkcja render "składa w całość" nasz szablon
    return render(request, 'blog/post_list.html', {})
