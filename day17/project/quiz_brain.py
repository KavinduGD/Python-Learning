from question_model import Question


class Quiz:

    def __init__(self, question_list):
        self.rounds = 0
        self.correct_answers = 0
        self.questions = []
        for question in question_list:
            self.questions.append(
                Question(question['text'], question['answer']))

    def next_question(self):
        return self.questions[self.rounds]

    def start_quiz(self):
        correct_answers = 0
        while self.rounds < 10:
            user_answer = input(f'{self.next_question().text} : ').capitalize()
            if self.next_question().is_answer_right(user_answer):
                self.correct_answers = self.correct_answers + 1
            print(f"""You answers {self.correct_answers} / {
                  self.rounds+1} correctly""")
            self.rounds = self.rounds+1
