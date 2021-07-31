class Quizbrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score=0

    def next_question(self):

        
        current_question = self.question_list[self.question_number]
        current_answer=current_question.answer
        self.question_number += 1
        user_answer=input(f"Q.{self.question_number}: {current_question.text} (true/false): ").capitalize()
        if user_answer==current_answer:
            self.score+=1
            print(f"you are right your score is {self.score}")
        else:
            print(f"you are wrong your score is {self.score}")

    def still_has_questions(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False
