from django.shortcuts import render

from contact_us.forms import ContactUsForm


def contact_us_view(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            data = {
                'name': form.data['name'],
                'email': form.data['email'],
            }
            return render(request, 'pages/contact_complete.html', {'data': data})

    else:
        form = ContactUsForm()
    return render(request, 'pages/contact.html', {'form': form})
