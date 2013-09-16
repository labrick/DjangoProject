# Create your views here.
from django.db.models import Q
from django.shortcuts import render_to_response
from models import Book

from forms import ContactForm
from django.core.mail import send_mail

def search(request):
    query = request.GET.get('req','')
    if query:
        qset = (
            Q(title__icontains=query)  |
            Q(authors__first_name__icontains=query) | 
            Q(authors__last_name__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("books/search.html",{
        "results":results,
        "query":query
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #Process form data
            topic = form.clean_data['topic']
            message = form.clean_data['message']
            sender = form.clean_data.get('sender','noreply@example.com') 
            def clean_message(self):
                message = self.clean_data.get('message', '')
                num_words = len(message.split())
                if num_words < 4:
                    raise forms.ValidationError("Not enough words!")
                return message
            send_mail(
                'Feedback from your site, topic: %s' % topic,
                message, sender,
                ['administrator@example.com']
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'sender':'yananback@gmail.com'})
    return render_to_response('books/contact.html',{'form':form})
