from django.shortcuts import render

from .forms import UploadFileForm

from .data.result import dog_cat_predict

from .functions import handle_uploaded_file


def index(request):
	form = UploadFileForm()
	return render(request, 'main\\mainForm.html',{'form':form})

def upload_view(request):
	if request.method == 'POST':
		resultCatOrDog = None
		form = UploadFileForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			image_adres = handle_uploaded_file(request.FILES)
			resultCatOrDog = dog_cat_predict(request.FILES['file'].name)
		else:
			print ('invalid form')
			print (form.errors)
			resultCatOrDog = 'ошибка'
			form = UploadFileForm()
	return render(request, 'main/mainForm.html', {'resultCatOrDog':resultCatOrDog,'form':form})