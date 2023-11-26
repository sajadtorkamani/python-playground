def possibly_perfect(correct_answers: list[str], student_answers: list[str]) -> bool:
    num_potential_correct_answers = 0
    num_potential_incorrect_answers = 0

    for index, student_answer in enumerate(student_answers):
        correct_answer = correct_answers[index]

        # Determine num potential correct answers
        if student_answer == correct_answer or correct_answer == '_':
            num_potential_correct_answers += 1

        # Determine num potential incorrect answers
        if student_answer != correct_answer or correct_answer == '_':
            num_potential_incorrect_answers += 1

    return num_potential_correct_answers == len(correct_answers) or num_potential_incorrect_answers == len(correct_answers)
