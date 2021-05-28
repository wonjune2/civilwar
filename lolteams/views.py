from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, League, Entry
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import MemberForm
import itertools
import sys
# Create your views here.


def index(request):
    if request.method == 'POST':
        if len(request.POST.getlist('id')) == 10:
            entry_list = []
            for i in request.POST.getlist('id'):
                entry_list.append(Member.objects.get(id=i))
            cases = list(itertools.combinations(
                entry_list, int(len(entry_list)//2)))
            min_value = sys.maxsize
            blueTeams = []
            redTeams = []
            for case_a in cases:
                blue = 0
                red = 0
                for i in case_a:
                    red += i.winrate
                    redTeam = case_a
                case_b = [i for i in entry_list if i not in case_a]
                for i in case_b:
                    blue += i.winrate
                    blueTeam = case_b
                if abs(blue - red) < min_value:
                    blueTeams = case_b
                    redTeams = case_a
                min_value = min(min_value, abs(blue - red))
            print(min_value)
            blue_win_rate = 0
            red_win_rate = 0
            for i in blueTeams:
                blue_win_rate += i.winrate
            blue_win_rate = (blue_win_rate / 5) * 100
            for i in redTeams:
                red_win_rate += i.winrate
            red_win_rate = (red_win_rate / 5) * 100
            if(blue_win_rate < red_win_rate):
                context = {'blueTeams': blueTeams, 'redTeams': redTeams,
                           'blue_win_rate': blue_win_rate, 'red_win_rate': red_win_rate}
            else:
                context = {'redTeams': blueTeams, 'blueTeams': redTeams,
                           'red_win_rate': blue_win_rate, 'blue_win_rate': red_win_rate}
            return render(request, 'lolteams/league.html', context)
    else:
        member_list = Member.objects.order_by('name')
        context = {'member_list': member_list, 'count': range(10)}
        return render(request, 'lolteams/teams.html', context)


def member(request):
    """
    lolteams 목록 출력
    """
    # print(float(request.POST.get('winrate')))
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.create_date = timezone.now()
            member.save()
            form = MemberForm()
            return redirect('lolteams:member')
    else:
        form = MemberForm()
    member_list = Member.objects.order_by('-winrate', 'name')
    context = {'member_list': member_list, 'form': form}
    return render(request, 'lolteams/member_list.html', context)


def detail(request, member_id):
    """
    lolteams 내용 출력
    """
    member = get_object_or_404(Member, pk=member_id)
    context = {'member': member}
    return render(request, 'lolteams/member_detail.html', context)


def league(request):
    """
    league 등록
    """
    if request.method == 'POST':
        blue = int(request.POST.get('blue'))
        red = int(request.POST.get('red'))
        if blue > 0 or red > 0:
            for i in range(blue):
                league = League(blue="승", red="패", create_date=timezone.now())
                league.save()
                for id in request.POST.getlist('blueTeam'):
                    member = get_object_or_404(Member, pk=id)
                    league.entry_set.create(
                        member=member, name=member.name, result="승", camp="블루", create_date=timezone.now())
                    member.win = member.win + 1
                    member.total = member.total + 1
                    member.save()
                for id in request.POST.getlist('redTeam'):
                    member = get_object_or_404(Member, pk=id)
                    league.entry_set.create(
                        member=member, name=member.name, result="패", camp="레드", create_date=timezone.now())
                    member.lose = member.lose + 1
                    member.total = member.total + 1
                    member.save()
            for i in range(red):
                league = League(blue="패", red="승", create_date=timezone.now())
                league.save()
                for id in request.POST.getlist('blueTeam'):
                    member = get_object_or_404(Member, pk=id)
                    league.entry_set.create(
                        member=member, name=member.name, result="패", camp="블루", create_date=timezone.now())
                    member.lose = member.lose + 1
                    member.total = member.total + 1
                    member.save()
                for id in request.POST.getlist('redTeam'):
                    member = get_object_or_404(Member, pk=id)
                    league.entry_set.create(
                        member=member, name=member.name, result="승", camp="레드", create_date=timezone.now())
                    member.win = member.win + 1
                    member.total = member.total + 1
                    member.save()
            for i in request.POST.getlist('blueTeam'):
                member = get_object_or_404(Member, pk=i)
                member.winrate = member.win / member.total
                member.save()
            for i in request.POST.getlist('redTeam'):
                member = get_object_or_404(Member, pk=i)
                member.winrate = member.win / member.total
                member.save()
            return redirect('lolteams:league_list')
        else:  # 승점이 입력되지 않으면 에러
            blueTeams = []
            redTeams = []
            blue_win_rate = 0
            red_win_rate = 0
            for id in request.POST.getlist('blueTeam'):
                member = get_object_or_404(Member, pk=id)
                blueTeams.append(member)
                blue_win_rate += member.winrate * 100
            for id in request.POST.getlist('redTeam'):
                member = get_object_or_404(Member, pk=id)
                redTeams.append(member)
                red_win_rate += member.winrate * 100
            blue_win_rate = (blue_win_rate / 5)
            red_win_rate = (red_win_rate / 5)
            error = "승점을 꼭 선택해 주셔야 합니다."
            context = {'blueTeams': blueTeams, 'redTeams': redTeams, 'error': error,
                       'blue_win_rate': blue_win_rate, 'red_win_rate': red_win_rate}
            return render(request, 'lolteams/league.html', context)


def league_list(request):
    """
    league_list
    """
    league_list = League.objects.order_by('-create_date')
    entry_list = Entry.objects.all()

    context = {'league_list': league_list, 'entry_list': entry_list}
    return render(request, 'lolteams/league_list.html', context)
