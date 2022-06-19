from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .forms import EmailPostForm
from .models import Post


# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'

    
# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3) # 3 posts per page
#     page = request.GET.get('page')
#     try:
#         post = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)

#     context = {
#         'page': page,
#         'posts': posts,
#     }
#     return render(request, 'list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)

    return render(request, 'list_detail.html', {'post': post})


def post_share(request, post_id):
    # Retrieve posts by 'post_id'
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields are valid && passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n \n {cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@myblog.com',[cd['to']])

            sent = True

    
    else:
        form = EmailPostForm()

    context = {
        'post': post,
        'form': form,
        'sent': sent,
    }
    
    return render(request, 'share.html', context)
    
