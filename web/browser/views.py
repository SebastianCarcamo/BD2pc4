from django.views.decorators.http import require_http_methods
from django.core.files.storage import default_storage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import Context, loader

import datetime

AUX_MEDIA_DIR = 'store/aux/'

def index(request):
	template = loader.get_template("index.html")
	return HttpResponse(template.render())


@require_http_methods(["POST"])
def search(request):
	image = request.FILES.get('file')

	file_path = AUX_MEDIA_DIR + str(datetime.datetime.now().time()) + '.png'
	filename = default_storage.save(file_path, image)

	default_storage.delete(file_path)

	return JsonResponse({'status' : 'success'})

