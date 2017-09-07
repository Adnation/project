import json
from .models import Question
from user.models import User
from answer.models import Answer
from tenant.models import Tenant
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import QustionSerializer
from answer.serializers import AnswerSerializer

# Create your views here.
def get_question_answer(request, question_column):

    # Retrieve question object
    try:
        question = Question.objects.get(column_title=question_column)
    except Question.DoesNotExist:
        return HttpResponse(json.dumps({'error': 'Invalid Question Id'}), status=400)

    # Check if the question is private or not
    if question.is_private:
        return HttpResponse(json.dumps({'error': 'Private Question Access Denied'}), status=403)

    # Retrive corresponding answer object
    answer = list(Answer.objects.filter(question__column_title=question_column))

    # If not the answer available
    if not len(answer):
        return HttpResponse(json.dumps({'error': 'Answer Not Available Now.'}), status=400)

    # Response data
    response = {
        'answer': answer[0].column_body,
        'question': question.column_title,
        'id': question.id,
        'user': question.user.name
    }

    # Return
    return HttpResponse(json.dumps(response), status=200)


# Method to search questions with specific search term
def search_questions(request, search_term):

    # Extract list of questions
    questions = list(Question.objects.filter(column_title__icontains=search_term, is_private=False))
    
    # List to store output quesions list
    opt_question_list = []

    # Iterate on each question and get its quesion, id and user's name
    for question in questions:
        opt_question_list.append({
            'question': question.column_title,
            'id': question.id,
            'user': question.user.name
            })

    # Return
    return HttpResponse(json.dumps({'questions': opt_question_list, 'total_questions': len(opt_question_list)}), status=200)


def render_index_html(request):
    return render(request, "question/index.html")

# Method to preapre dashboard data
def preapre_dashboard_data(request):
    
    today_top_tenants = list(Tenant.objects.all().order_by("-daily_request_counter")[0:6])
    overall_top_tenants = list(Tenant.objects.all().order_by("-total_request_counter")[0:6])

    opt_today_top_tenants = []
    opt_overall_top_tenants = []

    for tenant in today_top_tenants:
        opt_today_top_tenants.append({'api_key': tenant.api_key, 'counter': tenant.daily_request_counter})

    for tenant in overall_top_tenants:
        opt_overall_top_tenants.append({'api_key': tenant.api_key, 'counter': tenant.total_request_counter})

    # prepare data
    response = {
        'total_questions': Question.objects.all().count(),
        'total_public_questions': Question.objects.filter(is_private=False).count(),
        'total_private_questions': Question.objects.filter(is_private=True).count(),
        'total_answers': Answer.objects.all().count(),
        'total_users': User.objects.all().count(),
        'total_tenants': Tenant.objects.all().count(),
        'today_consumers': opt_today_top_tenants,
        'overall_consumers': opt_overall_top_tenants
    }

    # Return data
    return HttpResponse(json.dumps({'dashboard_data': response}), status=200)
