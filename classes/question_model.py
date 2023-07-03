from main import question_bank

class Question:
    def __init__(self,text,correct):
        self.text=text
        self.answer=correct



class QuizBrain:
    def __init__(self,lis):
        self.question_number=0
        self.question_list=lis
    def next_question(self):
        curr_question=self.question_list[self.question_number]
        input(f"{curr_question} True or False")
    def still_has_questions(self):
        curr_question=self.question_list[self.question_number]
        return bool(len(question_bank)-curr_question)
