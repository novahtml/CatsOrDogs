import os
from CatsOrDogs.settings import BASE_DIR

def handle_uploaded_file(f):
	dir=os.path.join(BASE_DIR, 'main\\static\\image\\')
	with open(dir + f['file'].name, 'wb+') as destination:
		for chunk in f['file'].chunks():
			destination.write(chunk)
	return dir + f['file'].name