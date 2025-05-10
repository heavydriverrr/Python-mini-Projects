from quiz_brain import QuizBrain
from q_model import Questions
from data import questions

question_bank = []
for question in questions:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Questions(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has():
    quiz.next_question()

print("You've completed the quiz")
print(f"your final score is: {quiz.score}/{quiz.question_number}")