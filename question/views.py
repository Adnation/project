import json
from .models import Question
from answer.models import Answer
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
