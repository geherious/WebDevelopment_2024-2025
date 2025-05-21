from django.shortcuts import render, redirect

from main.forms import FeedbackForm


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = FeedbackForm()

    return render(request, 'main/feedback.html', {'form': form})

def thank_you(request):
    return render(request, 'main/thank_you.html')