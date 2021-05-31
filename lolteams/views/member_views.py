from django.shortcuts import render
from ..models import Member, Entry
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..forms import MemberForm, MemberModify

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


def member_detail(request, member_id):
    """
    lolteams 내용 출력
    """
    member = get_object_or_404(Member, pk=member_id)
    print("member_id : ",member_id)
    if request.method == "POST":
        form = MemberModify(request.POST, instance=member)
        if form.is_valid():
            member = form.save()
            member.save()
            return redirect('lolteams:member_detail', member_id=member_id)
    else :
        form = MemberModify()
    entry_list = Entry.objects.filter(member=member)
    context = {'member': member, 'entry_list' : entry_list, 'form' : form}
    return render(request, 'lolteams/member_detail.html', context) 