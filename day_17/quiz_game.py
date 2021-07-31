from question_model import Question
from data import question_data
from quiz_brain import Quizbrain


question_bank=[]

for questions in question_data:
    question_text=questions['text']
    question_answer=questions['answer']
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
print(question_bank[0].answer)
quiz=Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("you have completed the quiz")
print(f"you final score is {quiz.score} / {quiz.question_number}")


