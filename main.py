from question import Question
from data import question_data
from quiz_brain import Quiz_brain

questions_list = []

for d in question_data:
    q = Question(d['text'], d['answer'])
    questions_list.append(q)

# print(question_list[0].text)

game = Quiz_brain(questions_list)

while game.still_has_question():
    question_ans, ans = game.ask_question()
    game.check_ans(question_ans, ans)
print(f'Your score: {game.score} / {len(questions_list)}')

