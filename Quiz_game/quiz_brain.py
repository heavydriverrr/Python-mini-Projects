from operator import truediv


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answers = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answers, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's Wrong.")
            print(f"the correct answer was: {correct_answer}.")
        print(f"Your Score is: {self.score}/{self.question_number}")
        print("\n")