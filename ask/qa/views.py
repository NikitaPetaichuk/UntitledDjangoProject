from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET
from django.urls import reverse
from qa.models import Question
from qa.forms import AskForm, AnswerForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, query_set):
    try:
        page_number = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(query_set, 10)
    try:
        page_object = paginator.page(page_number)
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)
    return page_object, paginator


@require_GET
def new_questions(request):
    page_object, paginator = paginate(request, Question.objects.new())
    paginator.base_url = reverse('question_list') + '?page='
    return render(request, 'question_list.html', {
        'questions': page_object.object_list,
        'page': page_object,
        'paginator': paginator
    })


@require_GET
def popular_questions(request):
    page_object, paginator = paginate(request, Question.objects.popular())
    paginator.base_url = reverse('popular') + '?page='
    return render(request, 'question_rating.html', {
        'questions': page_object.object_list,
        'page': page_object,
        'paginator': paginator
    })


def question_page(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answer_set.all()
    form = AnswerForm(initial={'question': str(pk)})
    return render(request, 'question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })


def question_ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            ask = form.save()
            url = reverse('question_detail', args=[ask.id])
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask_question.html', {
        'form': form
    })


def question_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = reverse('question_detail', args=[answer.question.id])
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')
