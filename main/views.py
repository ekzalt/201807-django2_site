from django.shortcuts import render

contactsContent = {
    'text': 'Call us',
    'phone': '+38 097 123 45 67',
}


def index(request):
    return render(request, 'main/main.html')


def contacts(request):
    return render(request, 'main/contacts.html', contactsContent)
