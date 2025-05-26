# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20517405
# Date: 10/12/2023

def validation():
    """validating the input recieved"""
    while True:
        try:
            pass_1 = int(input('Please enter your credits at pass: '))
            defer = int(input('Please enter credits at defer: '))
            fail = int(input('Please enter your credits at fail: '))

            # to check the input integer is within range
            if 0 <= pass_1 <= 120 and 0 <= defer <= 120 and 0 <= fail <= 120 and pass_1 % 20 == 0 and defer % 20 == 0 and fail % 20 == 0:

                # to check whether sum of pass_1,defer and fail equal to 120
                total_credits = pass_1 + defer + fail
                if total_credits != 120:
                    print('Total incorrect')
                else:
                    return pass_1, defer, fail
                    break
            else:
                print("out of range")


        except ValueError:             # this will prevent the program from crashing if non integer inputs are entered.
            print('Integer Requied')


def outcomes():
    '''this function is designed to  students to predict their progression outcome at the end of each academic year. '''

    pass_1, defer, fail = validation()
    if pass_1 == 120:
        print('progress')
    elif pass_1 == 100:
        print('progess(module trailer)')
    elif fail >= 80:
        print('Exclude')
    else:
        print('Do not progress - module retriver')


outcomes()

outcomes.getMouse()
outcomes.close()













