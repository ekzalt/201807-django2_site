from django.shortcuts import render
# from django.http import HttpResponse

from news.models import Article


def index(request):
    queryList = Article.objects.order_by('-date')[:20]
    return render(request, 'news/news.html', {'articles': queryList})

def detail(request, reqId):
    # return HttpResponse(str('Article with id:' + str(reqId)))
    try:
        query = Article.objects.get(pk=reqId)
    except Article.DoesNotExist:
        raise Http404(str('Article with id:' + str(reqId) + 'does not exist'))
    return render(request, 'news/news-detail.html', {'detail': query})
