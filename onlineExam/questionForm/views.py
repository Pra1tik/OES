from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Choices, Questions, Answer, Form, Responses
import json
import random
import string

# Create your views here.

def index(request): #TODO:only teacher
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.user.isStudent:
        forms = Form.objects.all()
        return render(request, "stream/lobby.html", {
            "usr_name": request.user.username
        })

    if request.user.isTeacher:
        forms = Form.objects.filter(creator = request.user)
        return render(request, "questionForm/index.html", {
            "forms": forms
        })

def create_form(request):
    # Creator must be authenticated
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    # Create a blank form API
    if request.method == "POST":
        data = json.loads(request.body)
        title = data["title"]
        code = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(30))
        choices = Choices(choice = "Option 1")
        choices.save()
        question = Questions(question_type = "multiple choice", question= "Untitled", required= False)
        question.save()
        question.choices.add(choices)
        question.save()
        form = Form(code = code, title = title, creator=request.user)
        form.save()
        form.questions.add(question)
        form.save()
        return JsonResponse({"message": "Sucess", "code": code})

def edit_form(request, code):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse("404"))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    return render(request, "questionForm/form.html", {
        "code": code,
        "form": formInfo
    })

def edit_title(request, code):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse("404"))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if request.method == "POST":
        data = json.loads(request.body)
        if len(data["title"]) > 0:
            formInfo.title = data["title"]
            formInfo.save()
        else:
            formInfo.title = formInfo.title[0]
            formInfo.save()
        return JsonResponse({"message": "Success", "title": formInfo.title})

def edit_description(request, code):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse("404"))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if request.method == "POST":
        data = json.loads(request.body)
        formInfo.description = data["description"]
        formInfo.save()
        return JsonResponse({"message": "Success", "description": formInfo.description})

def edit_setting(request, code):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse("404"))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if request.method == "POST":
        data = json.loads(request.body)
        formInfo.collect_email = data["collect_email"]
        formInfo.is_quiz = data["is_quiz"]
        formInfo.authenticated_responder = data["authenticated_responder"]
        formInfo.confirmation_message = data["confirmation_message"]
        formInfo.edit_after_submit = data["edit_after_submit"]
        formInfo.allow_view_score = data["allow_view_score"]
        formInfo.save()
        return JsonResponse({'message': "Success"})

def delete_form(request, code):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse("404"))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if request.method == "DELETE":
        #Delete all questions and choices
        for i in formInfo.questions.all():
            for j in i.choices.all():
                j.delete()
            i.delete()
        for i in Responses.objects.filter(response_to = formInfo):
            for j in i.response.all():
                j.delete()
            i.delete()
        formInfo.delete()
        return JsonResponse({'message': "Success"})

def edit_question(request, code):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if request.method == "POST":
        data = json.loads(request.body)
        question_id = data["id"]
        question = Questions.objects.filter(id = question_id)
        if question.count() == 0:
            return HttpResponseRedirect(reverse("404"))
        else: question = question[0]
        question.question = data["question"]
        question.question_type = data["question_type"]
        question.required = data["required"]
        if(data.get("score")): question.score = data["score"]
        if(data.get("answer_key")): question.answer_key = data["answer_key"]
        question.save()
        return JsonResponse({'message': "Success"})

def edit_choice(request, code):
    if not request.user.is_authenticated or  not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if request.method == "POST":
        data = json.loads(request.body)
        choice_id = data["id"]
        choice = Choices.objects.filter(id = choice_id)
        if choice.count() == 0:
            return HttpResponseRedirect(reverse("404"))
        else: choice = choice[0]
        choice.choice = data["choice"]
        if(data.get('is_answer')): choice.is_answer = data["is_answer"]
        choice.save()
        return JsonResponse({'message': "Success"})

def add_choice(request, code):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if request.method == "POST":
        data = json.loads(request.body)
        choice = Choices(choice="Option")
        choice.save()
        formInfo.questions.get(pk = data["question"]).choices.add(choice)
        formInfo.save()
        return JsonResponse({"message": "Success", "choice": choice.choice, "id": choice.id})

def remove_choice(request, code):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if request.method == "POST":
        data = json.loads(request.body)
        choice = Choices.objects.filter(pk = data["id"])
        if choice.count() == 0:
            return HttpResponseRedirect(reverse("404"))
        else: choice = choice[0]
        choice.delete()
        return JsonResponse({"message": "Success"})

def get_choice(request, code, question):
    if not request.user.is_authenticated or  not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if request.method == "GET":
        question = Questions.objects.filter(id = question)
        if question.count() == 0: return HttpResponseRedirect(reverse('404'))
        else: question = question[0]
        choices = question.choices.all()
        choices = [{"choice":i.choice, "is_answer":i.is_answer, "id": i.id} for i in choices]
        return JsonResponse({"choices": choices, "question": question.question, "question_type": question.question_type, "question_id": question.id})

def add_question(request, code):
    if not request.user.is_authenticated or  not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if request.method == "POST":
        choices = Choices(choice = "Option 1")
        choices.save()
        question = Questions(question_type = "multiple choice", question= "Untitled Question", required= False)
        question.save()
        question.choices.add(choices)
        question.save()
        formInfo.questions.add(question)
        formInfo.save()
        return JsonResponse({'question': {'question': "Untitled Question", "question_type": "multiple choice", "required": False, "id": question.id}, 
        "choices": {"choice": "Option 1", "is_answer": False, 'id': choices.id}})

def delete_question(request, code, question):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if request.method == "DELETE":
        question = Questions.objects.filter(id = question)
        if question.count() == 0: return HttpResponseRedirect(reverse("404"))
        else: question = question[0]
        for i in question.choices.all():
            i.delete()
            question.delete()
        return JsonResponse({"message": "Success"})

def score(request, code):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if not formInfo.is_quiz:
        return HttpResponseRedirect(reverse("edit_form", args = [code]))
    else:
        return render(request, "questionForm/score.html", {
            "form": formInfo
        })

def edit_score(request, code):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if not formInfo.is_quiz:
        return HttpResponseRedirect(reverse("edit_form", args = [code]))
    else:
        if request.method == "POST":
            data = json.loads(request.body)
            question_id = data["question_id"]
            question = formInfo.questions.filter(id = question_id)
            if question.count() == 0:
                return HttpResponseRedirect(reverse("edit_form", args = [code]))
            else: question = question[0]
            score = data["score"]
            if score == "": score = 0
            question.score = score
            question.save()
            return JsonResponse({"message": "Success"})

def answer_key(request, code):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if not formInfo.is_quiz:
        return HttpResponseRedirect(reverse("edit_form", args = [code]))
    else:
        if request.method == "POST":
            data = json.loads(request.body)
            question = Questions.objects.filter(id = data["question_id"])
            if question.count() == 0: return HttpResponseRedirect(reverse("edit_form", args = [code]))
            else: question = question[0]
            if question.question_type == "short" or question.question_type == "paragraph":
                question.answer_key = data["answer_key"]
                question.save()
            else:
                for i in question.choices.all():
                    i.is_answer = False
                    i.save()
                if question.question_type == "multiple choice":
                    choice = question.choices.get(pk = data["answer_key"])
                    choice.is_answer = True
                    choice.save()
                else:
                    for i in data["answer_key"]:
                        choice = question.choices.get(id = i)
                        choice.is_answer = True
                        choice.save()
                question.save()
            return JsonResponse({'message': "Success"})

def feedback(request, code):
    if not request.user.is_authenticated or not request.user.isTeacher:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if not formInfo.is_quiz:
        return HttpResponseRedirect(reverse("edit_form", args = [code]))
    else:
        if request.method == "POST":
            data = json.loads(request.body)
            question = formInfo.questions.get(id = data["question_id"])
            question.feedback = data["feedback"]
            question.save()
            return JsonResponse({'message': "Success"})

def view_form(request, code):
   
    if request.user.is_authenticated:
        formInfo = Form.objects.filter(code = code)
        #Checking if form exists
        if formInfo.count() == 0:
            return HttpResponseRedirect(reverse('404'))
        else: formInfo = formInfo[0]
        if formInfo.authenticated_responder: #TODO
           
            if not request.user.is_authenticated:
                return HttpResponseRedirect(reverse("login"))

        return render(request, "questionForm/view_form.html", {
            "form": formInfo
        })
    else:
        return HttpResponseRedirect(reverse("login"))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def submit_form(request, code):
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    if formInfo.authenticated_responder:
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
        code = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(20))
        if formInfo.authenticated_responder: #
            response = Responses(response_code = code, response_to = formInfo, responder_ip = get_client_ip(request), responder = request.user)
            response.save()
        else:
            if not formInfo.collect_email:
                response = Responses(response_code = code, response_to = formInfo, responder_ip = get_client_ip(request),responder = request.user)
                response.save()
            else:
                response = Responses(response_code = code, response_to = formInfo, responder_ip = get_client_ip(request), responder_email=request.POST["email-address"])
                response.save()
        for i in request.POST:
            #Excluding csrf token
            if i == "csrfmiddlewaretoken" or i == "email-address":
                continue
            question = formInfo.questions.get(id = i)
            for j in request.POST.getlist(i):
                answer = Answer(answer=j, answer_to = question)
                answer.save()
                response.response.add(answer)
                response.save()
        return render(request, "questionForm/form_response.html", {
            "form": formInfo,
            "code": code
        })

def responses(request, code):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]

   
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    return render(request, "questionForm/responses.html", {
        "form": formInfo,
        "responses": Responses.objects.filter(response_to = formInfo),
        # "students":Student.objects.filter(user=)
    })

def response(request, code, response_code):
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if not formInfo.allow_view_score:
        if formInfo.creator != request.user:
            return HttpResponseRedirect(reverse("403"))
    total_score = 0
    score = 0
    responseInfo = Responses.objects.filter(response_code = response_code)
    if responseInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: responseInfo = responseInfo[0]
    if formInfo.is_quiz:
        for i in formInfo.questions.all():
            total_score += i.score
        for i in responseInfo.response.all():
            #TODO:
            if i.answer_to.question_type == "short" or i.answer_to.question_type == "paragraph":
                if i.answer == i.answer_to.answer_key: score += i.answer_to.score
            elif i.answer_to.question_type == "multiple choice":
                answerKey = None
                for j in i.answer_to.choices.all():
                    if j.is_answer: answerKey = j.id
                if answerKey is not None and int(answerKey) == int(i.answer):
                    score += i.answer_to.score
        #
    return render(request, "questionForm/response.html", {
        "form": formInfo,
        "response": responseInfo,
        "score": score,
        "total_score": total_score
    })

def edit_response(request, code, response_code):
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    response = Responses.objects.filter(response_code = response_code, response_to = formInfo)
    if response.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: response = response[0]
    if formInfo.authenticated_responder:
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        if response.responder != request.user:
            return HttpResponseRedirect(reverse('403'))
    if request.method == "POST":
        if formInfo.authenticated_responder and not response.responder:
            response.responder = request.user
            response.save()
        if formInfo.collect_email:
            response.responder_email = request.POST["email-address"]
            response.save()
        #Deleting all existing answers
        for i in response.response.all():
            i.delete()
        for i in request.POST:
            #Excluding csrf token and email address
            if i == "csrfmiddlewaretoken" or i == "email-address":
                continue
            question = formInfo.questions.get(id = i)
            for j in request.POST.getlist(i):
                answer = Answer(answer=j, answer_to = question)
                answer.save()
                response.response.add(answer)
                response.save()
        if formInfo.is_quiz:
            return HttpResponseRedirect(reverse("response", args = [formInfo.code, response.response_code]))
        else:
            return render(request, "questionForm/form_response.html", {
                "form": formInfo,
                "code": response.response_code
            })
    return render(request, "questionForm/edit_response.html", {
        "form": formInfo,
        "response": response
    })


def delete_responses(request, code):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    formInfo = Form.objects.filter(code = code)
    #Checking if form exists
    if formInfo.count() == 0:
        return HttpResponseRedirect(reverse('404'))
    else: formInfo = formInfo[0]
    #Checking if form creator is user
    if formInfo.creator != request.user:
        return HttpResponseRedirect(reverse("403"))
    if request.method == "DELETE":
        responses = Responses.objects.filter(response_to = formInfo)
        for response in responses:
            for i in response.response.all():
                i.delete()
            response.delete()
        return JsonResponse({"message": "Success"})

# Error handler
def FourZeroThree(request):
    return render(request, "questionForm/403.html")

def FourZeroFour(request):
    return render(request, "questionForm/404.html")
