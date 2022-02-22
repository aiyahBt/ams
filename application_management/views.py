from django.db import IntegrityError, transaction


from django.shortcuts import render, redirect
from .forms import ApplicationForm, ApplicationRoundForm
from .models import ApplicationRound, ImageUploadingTest

# Create your views here.
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        form._meta.model.user = request.user

        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'upload/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ApplicationForm()


    return render(request, 'upload/upload.html', {'form': form})

def application_announcement_view(request):

    stuff_for_frontend = {
        'application_round_list': ApplicationRound.objects.filter(visible=True, active=True)
    }

    return render(request, 'application-announcement/announce.html', stuff_for_frontend)

def announce_new_application_round_view(request):

    if request.method == 'POST':
        form = ApplicationRoundForm(request.POST)

        form._meta.model.user = request.user

        if form.is_valid():
            form.save()

            # return render(request, 'application-announcement/announce.html', {})
            return redirect('/application-announcement')
    else:
        form = ApplicationRoundForm()

    return render(request, 'application-announcement/announce-new-application-round.html', {'form': form})

def application_form_view(request, application_round_id):


    if request.method == 'POST':

        if not(request.user.is_authenticated):
            return redirect('/home')

        application_info = ImageUploadingTest.objects.filter(application_round_id=application_round_id, user=request.user.id).first()
        application_round = ApplicationRound.objects.filter(id=application_round_id).first()

        print(type(application_info), type(application_round))
        form = ApplicationForm(request.POST, request.FILES)
        try:
            with transaction.atomic():

                if application_info is None:
                    if form.is_valid():
                        application_info = ImageUploadingTest.objects.create(application_round=application_round,
                                                                             user=request.user,
                                                                             title=form.cleaned_data['title'],
                                                                             image=form.cleaned_data['image'],
                                                                             doc=form.cleaned_data['doc'])
                        # application_info = ImageUploadingTest.objects.create()
                        application_info.save()
                        print(application_info)
                else:
                    form.instance = application_info

                    if form.is_valid():
                        form.save()

                        return redirect('/home')
        except IntegrityError:
            return redirect('/home')

        return redirect('/application-announcement')


    else:
        obj = ImageUploadingTest.objects.filter(
            application_round_id=application_round_id,
            user=request.user.id).first()

        if obj is not None:
            form = ApplicationForm(instance=obj)
        else:
            form = ApplicationForm()

    return render(request, 'application-announcement/application-form.html', {'form': form})
