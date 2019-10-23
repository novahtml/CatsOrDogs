from django.shortcuts import render

from .forms import FileUploadForm

from .data.functions import dog_cat_predict

def index(request):
    return render(request, 'main/mainForm.html')

def add_image(request):
	return



def upload_view(request):
	if request.method == 'POST':
		resultCatOrDog = '123'
		form = FileUploadForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			resultCatOrDog1 = dog_cat_predict('static/image/dog_test.jpg')
			resultCatOrDog = '123'
		else:
			print ('invalid form')
			print (form.errors)
	return render(request, 'main/mainForm.html', {'resultCatOrDog':resultCatOrDog})