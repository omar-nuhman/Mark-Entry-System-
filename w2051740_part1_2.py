# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20517405
# Date: 10/12/2023

def validation():

        """validating the input recieved"""
        while True:
            try:
                pass_1 = int(input('Please enter your credits at pass: '))
                defer = int(input('Please enter your credits at defer: '))
                fail = int(input('Please enter your credits at fail: '))

                # to check the input integer is within range

                if 0 <= pass_1 <= 120 and 0 <= defer <= 120 and 0 <= fail <= 120 and pass_1 % 20 == 0 and defer % 20 == 0 and fail % 20 == 0:

                    # to check whetner sum of pass_1,defer and fail equal to 120

                    total_credits = pass_1 + defer + fail
                    if total_credits != 120:
                        print('Total incorrect')
                    else:
                        return pass_1, defer, fail
                        break
                else:
                    print("out of range")

            # this will prevent the program from crashing if non integer inputs are entered.
            except ValueError:
                print('Integer Requied')




def outcomes():
    '''this function is designed to  students to predict their progression outcome at the end of each academic year. '''

    pass_1, defer, fail = validation()
    if pass_1 == 120:
        return ('progress')
    elif pass_1 == 100:
        return ('progress(module trailer)')
    elif fail >= 80:
        return ('Exclude')
    else:
        return ('Do not progress - module retriver')


#creating a loop in order for staffs to enter multiple output.
#intializing variable
count = 0
progress = 0
progress_module_trailer = 0
exclude = 0
do_not_progress = 0


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


    decision = input('in order to quit the loop enter "q" else enter any charecter: ')
    if decision.lower() == "q":
        break
    else:
        continue

from graphics import *


#These variables are used in the creation of a histogram. Furthermore, the previously collected variables are divided to prevent the histogram bars from exceeding the window

height = 360  #using line as a base
progress_graph = height - progress*4
progress_module_trailer_graph = height - progress_module_trailer*4
exclude_graph = height - exclude*4
do_not_progress_graph = height - do_not_progress*4

#create a window
window = GraphWin("Histogram",600,400)
window.setBackground("Mint Cream")# Set the background colour of the window

#headinng
heading = Text(Point(100, 20),'Histogram Result')
heading.draw(window)
heading.setTextColor("grey")
heading.setSize(15)
heading.setStyle("bold")

line = Line(Point(50,360),Point(560,360))
line.draw(window)


#progress
bar = Rectangle(Point(30,360),Point(130, progress_graph))
bar.setFill('green')
bar.draw(window)

#labelling progress
label = Text(Point(80, 370), 'progress')
label.draw(window)
#printing number of students progressed
no_of_students = Text(Point(80,(progress_graph-10)), progress)
no_of_students.draw(window)


#progress (module trailer)
bar = Rectangle(Point(150,360), Point(250, progress_module_trailer_graph))
bar.setFill('light green')
bar.draw(window)

#labelling
label = Text(Point(200, 370), 'module trailer')
label.draw(window)
#printing number of students progressed(module trailer)
no_of_students = Text(Point(200,(progress_module_trailer_graph-10)), progress_module_trailer)
no_of_students.draw(window)


#did't progress
bar = Rectangle(Point(270,360),Point(370, do_not_progress_graph))
bar.setFill('pink')
bar.draw(window)

#labelling
label = Text(Point(320, 370), 'do not progress')
label.draw(window)
#printing number of students didn't progress
no_of_students = Text(Point(320,(do_not_progress_graph-10)), do_not_progress)
no_of_students.draw(window)


#exclude
bar = Rectangle(Point(400,360),Point(500, exclude_graph))
bar.setFill('red')
bar.draw(window)

#labelling
label = Text(Point(450, 370), 'exclude')
label.draw(window)
#printing number of students excluded
no_of_students = Text(Point(450,(exclude_graph-10)), exclude)
no_of_students.draw(window)





window.getMouse()
window.close()

