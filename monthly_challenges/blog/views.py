from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def starting_page(request):
    all_post=Post.objects.all()
    latest_posts=all_post.order_by("-date")[:3]
    read_later_id=request.session.get('read_later')
    if read_later_id is None or len(read_later_id)==0:
        status=False
        read_later=[]
    else:
        read_later = all_post.filter(id__in=read_later_id)
        status=True
    return render(request,'blog/index.html',{
        'posts':latest_posts,
        'read_later':read_later,
        'status':status
    })

def posts(request):
    all_posts=Post.objects.all()
    return render(request,'blog/all-posts.html',{
        'all_posts':all_posts
    })
@login_required
def post_detail(request,slug):
    # post_d=Post.objects.get(slug=slug)
    post_d=get_object_or_404(Post,slug=slug)
    comments=post_d.comments.all().order_by('-id')[:3]
    stored_post=request.session.get('read_later')

    # p=list(filter(lambda x:x['slug']==slug ,all_posts))    ########### return a list such as[{name:'ali'}] for use from this in template should be unpack in template whit for loop such as all_poist
    # for key in all_posts:
    #     if key['slug']==slug:
    #         post_d=key
    if request.method=='POST':
        if 'obj_id' in request.POST:
            post_id=int(request.POST['obj_id'])
            # stored_post=request.session.get('read_later')
            if stored_post is None:
                stored_post=[]
                print('##############%%%%%%%%%######')
                print('stored_post is non')
            if post_id not in stored_post:
                stored_post.append(post_id)
                request.session['read_later']=stored_post
                print('##############%%%%%%%%%######')
                print('post is added to stored_post')
                return HttpResponseRedirect('/')
            else:
                stored_post.remove(post_id)
                request.session['read_later']=stored_post
                print(stored_post)
                print('############')
                print(request.session.get('read_later'))
                redirect=reverse('post-detail-page',args=[slug])
                return HttpResponseRedirect(redirect)
        form=CommentForm(request.POST)

        if form.is_valid():
            c_form=form.save(commit=False)
            c_form.post=post_d
            c_form.save()
            print('1####################')
            print(form.cleaned_data)
            print('2####################')
            # print(c_form.cleaned_data) comment obj has no attr cleaned_data
            print('end####################')
            redirect=reverse('post-detail-page',args=[slug])
            return HttpResponseRedirect(redirect)
    else:
        form=CommentForm()
        # stored_post=request.session.get('read_later')
        if stored_post is None or len(stored_post)==0:
            stored_post=[]
    return render(request,'blog/post-detail.html',{
        'post':post_d,
        'form':form,
        'comments':comments,
        'read_later':stored_post
    })