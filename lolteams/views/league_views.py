from ..models import League, Entry
from django.shortcuts import render
from django.core.paginator import Paginator

def league_list(request):
    """
    league_list
    """
    page = request.GET.get('page', '1')
    
    league_list = League.objects.order_by('-create_date')
    entry_list = Entry.objects.all()
    paginator = Paginator(league_list, 10)
    page_obj = paginator.get_page(page)

    context = {'league_list': page_obj, 'entry_list': entry_list}
    return render(request, 'lolteams/league_list.html', context)