class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def is_answer_right(self, user_answer):
        if self.answer == user_answer:
            print("You got it right!")
        else:
            print("That's wrong.")
        return self.answer == user_answer
