from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, Imageform
from .models import ImageModel, MyUser


def index(request):
    """
    view for home page of site
    """
    num_images = 0
    user = None
    gallery = None

    # find gallery
    if request.user.is_authenticated:
        num_images = ImageModel.objects.filter(user=request.user).count()
        user = request.user
        gallery = ImageModel.objects.filter(user=request.user)

    context = {
        'gallery': gallery,
        'user': user,
        'num_images': num_images,
    }

    return render(request, 'index.html', context=context)


def upload_to_user(request):
    """
    to upload an image to database, saving the user information and description
    as per specified in ImageForm
    :param request:
    :return: rendered webpage
    """

    if request.method == "POST":
        form = Imageform(request.POST, request.FILES)

        if form.is_valid():
            image_obj = ImageModel()
            image_obj.img_text = form.cleaned_data['img_text']
            image_obj.img = form.cleaned_data['img']
            image_obj.user = request.user
            image_obj.save()
            return render(request, 'upload.html')
    else:
        form = Imageform()
    # pictures = ImageModel.objects.filter(user=request.user)
    return render(request, 'upload.html', {'form': form})


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
