from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import ContactForm 
from django.core.mail import send_mail, get_connection 
from . models import Page 

def index_pages(request, pagename): 
    pagename = '/' + pagename 
    pg = get_object_or_404(Page, permalink=pagename) 
    #pg = Page.objects.get(permalink=pagename) 
    context = { 
        'title': pg.title, 
        'content': pg.bodytext, 
        'last_updated': pg.update_date, 
        'page_list': Page.objects.all(), 
    } 
    # assert False 
    return render(request, 'pages/page.html', context) 


def contact(request): 
    submitted = False 
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            cd = form.cleaned_data 
            # assert False
            #-------------------------------------------------------------- 
            con = get_connection('django.core.mail.backends.console.EmailBackend') 
            send_mail(cd['subject'],cd['message'], cd.get('email', 'noreply@gmail.com'), ['lpglaasri@gmail.com'],connection = con) 
            #-------------------------------------------------------------- 
            return HttpResponseRedirect('/contact?submitted=True') 
    else: 
        form = ContactForm() 
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'pages/contact.html', {'form': form, 'page_list': Page.objects.all(),'submitted': submitted}) 