from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display= ["title","updated", "timestamp"]
	list_display_links= ["updated"]
	list_editable= ["title"]
	list_filter=["updated","timestamp"]
	search_fields=["title","content"]
	class Meta:
		"""docstring for ClassName"""
		model=Post
			
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg
		

admin.site.register(Post, PostModelAdmin)
