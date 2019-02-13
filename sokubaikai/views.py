from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django import forms
from .models import DoujinMarketsM
from .forms import DoujinMarketsMForm
from django.urls import reverse, reverse_lazy


class MyView(View):
    # rest向き？
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
        # myview = MyView.as_view()


# 　topページ
class IndexView(TemplateView):
    template_name = 'index.html'


index = IndexView.as_view()


# def get(self, request, *args, **kwargs):
# return HttpResponse('トップページ')
# indexview = IndexView.as_view()

# Listviewで一覧表示
class SokubaikaiListView(ListView):
    model = DoujinMarketsM
    template_name = 'sokubaikai-list.html'


class SokubaikaiCreateView(CreateView):
    model = DoujinMarketsM()
    print(model)
    template_name = "sokubaikai-detail.html"
    # form_class = DoujinMarketsMForm(initial={'market_memo': '2017-11-11'})
    form_class = DoujinMarketsMForm
    success_url = reverse_lazy("sokubaikai:list")  # 成功時にリダイレクトするURL
    #initial = {'market_date': '2017-11-11'}


class SokubaikaiDetailView(DetailView):
    model = DoujinMarketsM
    template_name = 'sokubaikai-detail.html'

    # def get(self, request, *args, **kwargs):
    # self.form = PostForm()
    #   return render(request, 'sokubaikai-detail.html', {'form': self.form})

    def render(self, request):
        form = DoujinMarketsMForm()
        return render(request, 'sokubaikai-detail.html', {'form': form})

    def post(self, request, *args, **kwargs):
        aa = request.POST['market_name']
        print(aa)
        bb = request.POST
        print(bb)
        # self.form = PostForm(request.POST)
        # if self.form.is_valid():
        #     self.form.save()
        market_id = request.POST['id']
        # モデルクラスのインスタンスを主キーで取得し代入することで更新
        model = DoujinMarketsM.objects.get(pk=market_id)

        # if文消したい
        if 'update_market' in request.POST:
            print('更新')
            form = DoujinMarketsMForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
            return redirect('sokubaikai:detail', pk=market_id)
        elif 'delete_market' in request.POST:
            model.delete()
            print('削除')
            return redirect('sokubaikai:list')
        elif 'cancel_market' in request.POST:
            print('戻る')
            return redirect('sokubaikai:list')

# index = IndexView.as_view()
