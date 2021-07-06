print('')
print('Multi-Number Common Factor/s Checker')
print('by: Marcko Pablo')
print('')
print('Please only input positive integers.')
print("Otherwise it will break and you'll need to start over.")
print('')

while True:
    all_input = []
    given_groups = {}
    answers_semi = []
    ans_dict = {}
    final_checker = []
    final_answers = []

    try:
        given = float(input('How many numbers do you want to check?'))
        print('')
        if given.is_integer():
            if given < 1:
                print('Please input a positive integer!')
                print('')
            else:
                given = int(given)
        else:
            print('Please input an integer!')
            print('')
    except ValueError:
        print("That's not a number!")
        print('')

    try:
        # noinspection PyUnboundLocalVariable
        for g in range(0, given):
            d = str(g + 1)
            if int(d[-1]) > -1:
                if int(d[-1]) == 1:
                    if len(d) > 1:
                        if int(d[-2]) == 1:
                            user_input = float(input('what is the ' + str(g + 1) + 'th number?'))
                        else:
                            user_input = float(input('what is the ' + str(g + 1) + 'st number?'))
                    else:
                        user_input = float(input('what is the ' + str(g + 1) + 'st number?'))
                elif int(d[-1]) == 2:
                    if len(d) > 1:
                        if int(d[-2]) == 1:
                            user_input = float(input('what is the ' + str(g + 1) + 'th number?'))
                        else:
                            user_input = float(input('what is the ' + str(g + 1) + 'nd number?'))
                    else:
                        user_input = float(input('what is the ' + str(g + 1) + 'nd number?'))
                elif int(d[-1]) == 3:
                    if len(d) > 1:
                        if int(d[-2]) == 1:
                            user_input = float(input('what is the ' + str(g + 1) + 'th number?'))
                        else:
                            user_input = float(input('what is the ' + str(g + 1) + 'rd number?'))
                    else:
                        user_input = float(input('what is the ' + str(g + 1) + 'rd number?'))
                else:
                    user_input = float(input('what is the ' + str(g + 1) + 'th number?'))
            # noinspection PyUnboundLocalVariable
            if user_input.is_integer:
                if user_input < 1:
                    print('Please input a positive integer!')
                    print('')
                    break
                else:
                    user_input = int(user_input)
                    all_input.append(user_input)
            else:
                print("That's not an integer!")
                print('')
                break
    except NameError:
        print("That's not a number!")
        print('')
    except ValueError:
        print("That's not a number!")
        print('')
    except TypeError:
        print("Please input a positive integer!")
        print('')

    for m in range(len(all_input)):
        number = all_input[m]
        try:
            number = float(number)
            if number.is_integer():
                number = int(number)
                if number > 0:
                    for i in range(1, number + 1):
                        quotient = number / i
                        if quotient.is_integer():
                            answers_semi.append(i)
                    given_groups[m] = answers_semi
                    answers_semi = []
                else:
                    print('Please input a positive integer!')
                    print('')
            else:
                print("That's not an integer!")
                print('')
        except ValueError:
            print("That's not a number!")
            print('')

    try:
        for s in range(0, given):
            for f in range(len(given_groups[s])):
                for r in range(0, given):
                    if given_groups[s][f] in given_groups[r]:
                        final_checker.append(r)
                        ans_dict[(given_groups[s][f])] = final_checker
                        if len(ans_dict[(given_groups[s][f])]) == given:
                            if given_groups[s][f] not in final_answers:
                                final_answers.append(given_groups[s][f])
                final_checker = []
        print('')
        print('The common factors are:')
        print(final_answers)
        print('')
    except NameError:
        print('Something in your input is wrong!')
        print('')
    except KeyError:
        print('Something in your input is wrong!')
        print('')
    except TypeError:
        print('Something in your input is wrong!')
        print('')
