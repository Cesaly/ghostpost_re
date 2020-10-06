from django.shortcuts import render, reverse, HttpResponseRedirect

from ghostpost.models import GhostPost
from ghostpost.forms import newPost


def index(request):
    all_posts = GhostPost.objects.all().order_by('-posted_time')
    return render(request, 'index.html', {'all_posts': all_posts})


def addPost(request):
    if request.method == 'POST':
        form = newPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostPost.objects.create(
                is_boast=data['is_boast'],
                content=data['content'],
            )
        return HttpResponseRedirect(reverse('home'))

    form = newPost()
    return render(request, 'newPost.html', {'form': form})


def onlyBoasts(request):
    boasts = GhostPost.objects.filter(is_boast=True).order_by('-posted_time')
    return render(request, 'boasts.html', {'boasts': boasts})


def onlyRoasts(request):
    roasts = GhostPost.objects.filter(is_boast=False).order_by('-posted_time')
    return render(request, 'roasts.html', {'roasts': roasts})


def filterVotes(request):
    # post = GhostPost.objects.get(id=id)
    # vote_score = post.up_votes - post.down_votes
    all_posts = GhostPost.objects.all()
    for post in all_posts:
        total = post.up_votes - post.down_votes
        print(total)

    return render(request, 'index.html', {'all_posts': all_posts})


def addLike(request, id):
    post = GhostPost.objects.get(id=id)
    post.up_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))


def minusLike(request, id):
    post = GhostPost.objects.get(id=id)
    post.down_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))
