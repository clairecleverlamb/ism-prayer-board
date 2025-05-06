from django.shortcuts import render, redirect, get_object_or_404
from .models import PrayerRequest
from .forms import PrayerRequestForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import PrayerRequestForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.template.loader import render_to_string

def home_view(request):
    featured_prayers = PrayerRequest.objects.order_by('-prayed_count')[:3]
    prayers = PrayerRequest.objects.order_by('-date_posted')
    form = PrayerRequestForm()
    return render(request, 'prayers/home.html', {
        'featured_prayers': featured_prayers,
        'prayers': prayers,
        'form': form
    })

@login_required
def submit_prayer(request):
    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            prayer = form.save(commit=False)
            prayer.user = request.user
            prayer.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('home')
    else:
        form = PrayerRequestForm()
    return render(request, 'prayers/submit.html', {'form': form})

@require_POST
@login_required
def create_prayer_ajax(request):
    form = PrayerRequestForm(request.POST)
    if form.is_valid():
        prayer = form.save(commit=False)
        prayer.user = request.user
        prayer.save()
        messages.success(request, "Prayer added successfully.")
        return JsonResponse({
            'message': 'Prayer added successfully',
            'student_name': prayer.student_name,
            'prayed_count': prayer.prayed_count,
        })
    return JsonResponse({'error': 'Invalid form data'}, status=400)

@login_required
def refresh_prayer_list(request):
    prayers = PrayerRequest.objects.order_by('-date_posted')
    html = render_to_string('prayers/prayer_list_partial.html', {'prayers': prayers})
    return JsonResponse({'html': html})

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