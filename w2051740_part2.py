# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20517405
# Date: 10/12/2023

def validation():
    """validating the input recieved"""
    while True:
        marks=[]
        try:
            pass_1 = int(input('Please enter your credits at pass: '))
            defer = int(input('Please enter your credits at defer: '))
            fail = int(input('Please enter your credits at fail: '))

            # to check the input integer is within range

            if (0 <= pass_1 <= 120 and 0 <= defer <= 120 and 0 <= fail <= 120) and (pass_1 % 20 == 0 and defer % 20 == 0 and fail % 20 == 0):

                # to check whetner sum of pass_1,defer and fail equal to 120

                total_credits = pass_1 + defer + fail
                if total_credits != 120:
                    print('Total incorrect')
                else:
                    marks.append(pass_1)
                    marks.append(defer)
                    marks.append(fail)
                    return marks

            else:
                print("out of range")


        except ValueError:  # this will prevent the program from crashing if non integer inputs are entered.
            print('Integer Requied')


# returning the values after the validation to variable response



def outcomes():
    '''this function is designed to  students to predict their progression outcome at the end of each academic year. '''

    response = validation()


    if response[0] == 120:
        response.append("progress")
        data.append(response)

        return ('progress')


    elif response[0] == 100:
        response.append("progress(module trailer")
        data.append(response)
        return ('progress(module trailer)')
    elif response[2] >= 80:
        response.append("Exclude")
        data.append(response)
        return ('Exclude')

    else:
        response.append("Do not progress - module retriver")
        data.append(response)
        return ('Do not progress - module retriver')



# creating a loop in order for staffs to enter multiple output.
# intializing variable
count = 0
progress = 0
progress_module_trailer = 0
exclude = 0
do_not_progress = 0
data = []



while True:
    output = outcomes()
    print(output)
    count += 1

    if output == 'progress':
        progress += 1
    elif output == 'progress(module trailer)':
        progress_module_trailer += 1
    elif output == 'Exclude':
        exclude += 1
    else:
        do_not_progress += 1

    decision = input('in order to quit the loop enter "q" else enter any character: ')
    if decision.lower() == "q":
        print("\nPart 2:")

        for item in data:

            print(f"{item[3]} - {item[0]},{item[1]},{item[2]}")
        break
    else:
        continue


