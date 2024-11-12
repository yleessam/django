from django.shortcuts import render, redirect
from blog.models import Post, Comment

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post_list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    #comment 생성
    if request.method == 'POST':
        comment_content = request.POST["comment"]
        Comment.objects.create(post=post, content=comment_content,)

       
    
    #detail 조회해서 출력
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)

def post_add(request):
    if request.method == 'POST': #포스트의 내용을 입력하고 작성 버튼을 눌렀을 때
        title = request.POST.get('title')
        content = request.POST.get('content')

        thumbnail = request.FILES.get('thumbnail')
        post = Post.objects.create(title=title, content=content, thumbnail=thumbnail,) #173페이지 
        

        #return redirect('/posts/')
        return redirect(f"/posts/{post.id}") #post_detail 페이지로 이동
    
    else: #GET 처음 페이지 호출
        print(request.method)

    return render(request, 'post_add.html')