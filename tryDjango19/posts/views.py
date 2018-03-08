from django.contrib import messages
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

# def post_home(request):
# 	return HttpResponse("<h1>Home</h1>")
from .models import Post
from .forms import PostForm

def post_Create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	# code to have default validation on POST data
	form=PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		# message success
		messages.success(request,"Successfully created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.success(request,"Successfully not created")
	# code to have the post data without validation
	# form=PostForm()
	# if(request.method == "POST"):
	# 	# printing in the console
	# 	print(request.POST) 
	context={
	"form": form,
	}
	# return HttpResponse("<h1>Create</h1>")
	return render(request, "post_form.html", context)

# def post_home(request):
# 	context = {
# 	"title": "Home2"
# 	}
# 	return render(request, "index.html", context)
def post_home(request):

	querySet = Post.objects.all()
	query= request.GET.get("q")
	if (query):
		querySet= querySet.filter(title__icontains=query)
	if request.user.is_authenticated():
		context = {
		"object_list": querySet,
		"title": "Welcome"
		}
	else:
		context = {
		"object_list": querySet,
		"title":"Home4"
		}

	return render(request, "post_list.html", context)

def post_details(request, id=None):

	instance = get_object_or_404(Post, id=id)

	context = {
	"title": "Details",
	"instance": instance
	}

	return render(request, "post_detail.html", context)


def post_Update(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	form=PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		# message success
		messages.success(request,"Successfully saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
	# 	messages.success(request,"Successfully not saved")
	context = {
	"title": "Details",
	"instance": instance,
	"form": form,
	}
	return render(request, "post_form.html", context)

def post_Retrieve(request):
	return HttpResponse("<h1>Retrieve</h1>")

def post_Delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404		
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Deleted")
	return redirect("posts:list")