from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreatePoll
from .models import Poll

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'polls/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePoll(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePoll()
    context = {
        'form' : form
    }
    return render(request, 'polls/create.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.op_one_count += 1
        elif selected_option == 'option2':
            poll.op_two_count += 1
        elif selected_option == 'option3':
            poll.op_three_count += 1
        elif selected_option == 'option4':
            poll.op_four_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'polls/vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'polls/results.html', context)