class Quiz_brain:
    def __init__(self, list):
        self.number = 0
        self.list = list

    def still_has_question(self):
        if self.number < len(self.list):
            print(self.number, len(self.list))
            return True
        else:
            print('Game finished')
            return False

    def ask_question(self):
        question = self.list[self.number]
        self.number += 1
        ans = input(f'No{self.number}: {question.text}?(True or False) \n Answer: ')
        return question.answer, ans