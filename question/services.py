def check_answer(questions:list,answers:list):
    points = 0

    for index,obj in enumerate(questions):
        user_answer = answers[index].get('user_answer')
        if user_answer == obj.answer:
            points += 1

    return points