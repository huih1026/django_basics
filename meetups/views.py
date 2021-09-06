import meetups
from django.shortcuts import render
from .models import Location, Meetup, Participant
from .forms import RegisterForm
# Create your views here.


def meetups(request):
    meetups = Meetup.objects.all()

    context = {
        'meetups': meetups
    }

    return render(request, 'meetups/index.html', context)


def meetup_detail(request, slug):
    try:
        meetup = Meetup.objects.get(slug=slug)
        return render(request, 'meetups/meetup_detail.html', {
            'meetup': meetup,
        })

    except Exception as exc:
        return render(request, 'meetups/meetup_detail.html', {
            'meetup': meetup
        })


def register_success(request, slug):
    print("i am in the register view now")
    try:
        meetup = Meetup.objects.get(slug=slug)
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            print("i wrapped the POST data")
            if form.is_valid():
                email = form.cleaned_data['email']
                print(email)
                # get_or_create() if found obj, then return obj and False
                # get_or_create() if NO found obj, then return created obj and True
                participant, created = Participant.objects.get_or_create(
                    email=email)

                if created:
                    print("i am .................***************")
                    print(participant)
                    print(form.cleaned_data['firstname'])
                    participant.firstname = form.cleaned_data['firstname']
                    participant.lastname = form.cleaned_data['lastname']
                    print('participate', participant)

                meetup.participants.add(participant)
                print(' i am in the database')
                return render(request, 'meetups/register_success.html', {
                    'meetup': meetup,
                    'success': True
                })

        return render(request, 'meetups/register_success.html', {
            'meetup': meetup,
            'form': form,
            'success': False
        })

    except Exception as e:
        return render(request, 'meetups/register_success.html', {
            'message': "Something wrong with the meetups, try later!",
            'meetup': meetup
        })
