# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import MessageForm
# Create your views here.


def post_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        print request.POST
        if form.is_valid():
            form.save()
            print "save ok"
            return HttpResponseRedirect('/success/')
    else:
        form = MessageForm()

    return render_to_response('messages/upload.html', {'form': form})
