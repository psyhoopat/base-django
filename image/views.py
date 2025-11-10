from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required
def load_image(request):
    return HttpResponse("Page load image.")