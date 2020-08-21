from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostpost_app import models, forms


def index_view(request):
    ghostpost = models.BoastRoast.objects.all().order_by("-timeposted")
    return render(
        request,
        "index.html",
        {"headline": "Recent GhostPosts!", "ghostpost": ghostpost},
    )


def sort_by_votes_view(request):
    sorted_votes = sorted(
        models.BoastRoast.objects.all(), key=lambda x: x.totalvotes, reverse=True
    )
    return render(
        request,
        "sort_by_votes.html",
        {"headline": "Popular GhostPosts!", "sorted_votes": sorted_votes},
    )


def boast_view(request):
    boast = models.BoastRoast.objects.all().order_by("-timeposted")
    return render(
        request, "boasts.html", {"headline": "Boast GhostPosts!", "boast": boast}
    )


def roast_view(request):
    roast = models.BoastRoast.objects.all().order_by("-timeposted")
    return render(
        request, "roasts.html", {"headline": "Roast GhostPosts!", "roast": roast}
    )


def create_post_view(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            models.BoastRoast.objects.create(
                choices=data.get("choices"), user_post=data.get("user_post")
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = forms.PostForm()
    return render(
        request,
        "create_post.html",
        {"headline": "Create a New GhostPost!", "form": form},
    )


def upvote_view(request, upvote_id):
    post = models.BoastRoast.objects.filter(id=upvote_id).first()
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote_view(request, downvote_id):
    post = models.BoastRoast.objects.filter(id=downvote_id).first()
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
