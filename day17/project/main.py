from quiz_brain import Quiz
from data import question_data


while True:
    quiz = Quiz(question_list=question_data)
    quiz.start_quiz()
    if input('want to start again : "yes" ot "no') == 'no':
        break
