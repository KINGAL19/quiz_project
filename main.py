from question import Question
from data import question_data
# from quiz_brain import Quiz_brain

questions_list = []

for d in question_data:
    q = Question(d['text'], d['answer'])
    questions_list.append(q)

# print(question_list[0].text)