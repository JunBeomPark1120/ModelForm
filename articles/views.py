from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
    }
    
    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    
    context = {
        'article': article,
    }
    
    return render(request, 'detail.html', context)

def create(request):
    # 모든 경우의 수
    # 1. GET : Form 만들어서 html 문서를 사용자에게 리턴
    # 2. POST : invalid data : 데이터 검증에 실패한 경우
    #   => 검증에 성공한 데이터를 가지고 html 문서를 사용자에게 리턴
    # 3. POST valid data : 데이터 검증에 성공한 경우
    #   => DB에 데이터 저장 후 detail로 redirect
    
    # ============================================================
    
    # create 기능
    # 사용자가 입력한 데이터를 DB에 저장
    # 5. POST요청 (데이터가 잘못 들어온 경우)
    # 10. POST요청 (데이터가 잘들어온 경우)
    if request.method == 'POST':
        # 6. Form에 사용자가 입력한 정보(X)를 담아 Form을 생성
        # 11. Form에 사용자가 입력한 정보(O)를 담아서 Form을 생성
        form = ArticleForm(request.POST)
        # 7. Form을 검증(검증에 실패)
        # 12. Form을 검증(검증에 성공)
        if form.is_valid():
            # 13. Form을 저장하고 그 결과를 article 변수에 저장
            article = form.save()
            # 14. detail 페이지로 redirect
            return redirect('articles:detail',id=article.id)

    # new에 해당하는 기능
    # 사용자가 데이터를 입력할 수 있도록 빈 종이를 리턴
    # 1. GET 요청
    else:
        # 2. 비어있는 From을 만들어서
        form = ArticleForm()
    
    # 3. comtext dict에 담고
    # 8. 검증에 실패한 Form을 context dict에 담고
    context = {
        'form': form,
    }
    
    # 4. create.html을 랜더링
    # 9. crate. html을 랜더링
    return render(request, 'create.html', context)
