def arithmetic_arranger(problems, results=False):
    arranged_problems = ""

    top_number = "{:>{size}}    "
    bot_number = "{} {:>{size}}    "
    result_symbol = "{:-^{size}}    "
    operation_result = "{:>{size}}    "

    numbers_signs_size = list()

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        try:
            if '+' in problem:
                for number in problem.split('+'):
                    int(number)
                    if len(number.strip()) > 4:
                        return "Error: Numbers cannot be more than four digits."
            elif '-' in problem:
                for number in problem.split('-'):
                    int(number)
                    if len(number.strip()) > 4:
                        return "Error: Numbers cannot be more than four digits."
            else:
                return "Error: Operator must be '+' or '-'."
        except ValueError:
            return "Error: Numbers must only contain digits."

        problem = problem.split(" ")
        problem.append(max(len(problem[0]), len(problem[2])))
        numbers_signs_size.append(problem)
    top_format = ""
    bot_format = ""
    result_format = ""
    result = ""
    operation_result_format = ""
    for elements in numbers_signs_size:
        top_format += top_number.format(elements[0], size=elements[3] + 2)
        bot_format += bot_number.format(
            elements[1], elements[2], size=elements[3])
        result_format += result_symbol.format("-", size=elements[3] + 2)
        if results:
            if '+' in elements[1]:
                result = int(elements[0]) + int(elements[2])
            else:
                result = int(elements[0]) - int(elements[2])

            operation_result_format += operation_result.format(
                result, size=elements[3] + 2)
    top_format = top_format.rstrip()
    bot_format = bot_format.rstrip()
    result_format = result_format.rstrip()
    all_together = "{}\n{}\n{}\n{}".format(top_format, bot_format,
                                           result_format, operation_result_format)
    arranged_problems = all_together.rstrip()
    return arranged_problems
