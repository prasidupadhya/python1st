def number_range(pass_credit, defer_credit, fail_credit):
    numbers = [0, 20, 40, 60, 80, 100, 120]
    if pass_credit in numbers and defer_credit in numbers and fail_credit in numbers:
        return True

def progession_outcome(pass_credit, defer_credit ,fail_credit):
    total_credit = pass_credit + defer_credit + fail_credit

    if total_credit != 120:
        print('Total incorrect, the total of the pass, defer and fail credits is not 120. Please try again!')
        
    else:        
        if pass_credits == 120:
            global progressed
            print('Progress')
            progressed +=1
            
        elif pass_credits > 80:
            global trailed
            print('Progress (module trailer)')
            trailed +=1
            
        elif fail_credits >= 80:
            global excluded
            print('Exclude')
            excluded +=1
            
        else:
            global retrieved
            print('Do not Progress - module retriever')
            retrieved +=1

def Histogram():
    #References:
    #[1] https://www.w3resource.com/python-exercises/python-basic-exercise-26.php
    #[2] https://stackoverflow.com/questions/63873750/function-that-gives-a-certain-star-histogram
    print('-'*60)
    print('Histogram')
    print('Progress', progressed ,':', '*'*progressed)
    print('Trailer', trailed ,':', '*'*trailed)
    print('Retriever', retrieved ,':', '*'*retrieved)
    print('Excluded', excluded ,':', '*'*excluded)
    print()
    print(progressed + trailed + retrieved + excluded, 'outcomes in total.')

progressed = 0
retrieved = 0
trailed = 0
excluded = 0

user_input = 'y'
#Reference: [3] https://www.w3schools.com/python/ref_func_input.asp
while True:
    if user_input == 'y':
        print("-" * 60)
        print()
        try:
            pass_credits = int(input('Enter your total PASS credits: '))
            defer_credits = int(input('Enter your total DEFER credits: '))
            fail_credits = int(input('Enter your total FAIL credits: '))
        except ValueError:
            print('Integer required; the credit input is the wrong data type. Please try again!')
            continue

        if number_range(pass_credits,defer_credits,fail_credits):
            progession_outcome(pass_credits,defer_credits,fail_credits)
        else:
            print('Out of range, credits entered are not in the range 0, 20, 40, 60, 80, 100 and 120. Please try again!')
        
        print()
        print("-" * 60)
        user_input = input('Would you like to enter another set of data?\n'
                           'Enter "y" for yes or "q" to quit and view results: ')

    elif user_input == 'q':
        print()
        Histogram()
        break
    
    else:
        print()
        print("-" * 60)
        print()
        print('Input invalid, type either y or q.\n')
        print("-" * 60)
        print()
        user_input = input('Would you like to enter another set of data?\nEnter "y" for yes or "q" to quit and view results: ')
        continue

#Prasid Upadhya
