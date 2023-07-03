from question_model import Question
from data import question_data

# class Question:
#     def __init__(self,text,correct):
#         self.text=text
#         self.answer=correct


question_bank=[]

question_bank=[Question(question["text"],question["answer"]) for question in question_data]
for pair in question_bank:
    print(pair.text,pair.answer)

print(len(question_bank))