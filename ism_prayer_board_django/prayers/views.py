from django.shortcuts import render, redirect, get_object_or_404
from .models import PrayerRequest
from .forms import PrayerRequestForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def home_view(request):
    featured_prayers = PrayerRequest.objects.order_by('-prayed_count')[:3]
    prayers = PrayerRequest.objects.order_by('-date_posted')
    return render(request, 'prayers/home.html', {
        'featured_prayers': featured_prayers,
        'prayers': prayers
    })

@login_required
def submit_prayer(request):
    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            prayer = form.save(commit=False)
            prayer.user = request.user
            prayer.save()
            return redirect('home')
    else:
        form = PrayerRequestForm()
    return render(request, 'prayers/submit.html', {'form': form})

@login_required
def prayer_detail(request, pk):
    prayer = get_object_or_404(PrayerRequest, pk=pk)
    return render(request, 'prayers/detail.html', {'prayer': prayer})


@login_required
def pray_for_request(request, pk):
    prayer = PrayerRequest.objects.get(pk=pk)
    prayer.prayed_count += 1
    prayer.save()
    return JsonResponse({'prayed_count': prayer.prayed_count})