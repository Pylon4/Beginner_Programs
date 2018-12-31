##################
# Family Program #
##################
# ask questions about
# your Family
#################


dad = input('What is your dad called? ') # ask what your dad is named, and store that in a variable: dad
mom = input('What is your mom called? ') # ask what your mom is named, and store that in a variable: mom
have_sis = input('Do you have a sister? ') # ask: do you have a sister
have_bro = input('Do you have a brother? ') # ask: do you have a brother

check_sis = None # a varible that is sat to none
check_bro = None # a varible that is sat to none

if have_sis.lower() == 'yes': # if the variable have_sis = 'yes' print('you have a sister')
    check_sis = True # if the condition is true, set check_sis to true
else:
    check_sis = False # is the condition is false, set check_sis to false

if have_bro.lower() == 'yes': # if the variable have_bro = 'yes' do this condtion
    check_bro = True # if the condtion is true, set check_bro to True
else: # else do this
    check_bro = False # else set check_bro to false

if check_sis == True: # if check_sis is true
    sis = input('What is your sister called? ') # asks what youre sister is called
    print(f'You\'re sister is called {sis}') # print youre sister is called 'something'
else: # else do nothing
    pass

if check_bro == True: # if check_bro is true
    bro = input('What is your brother called? ') #asks what youre brother is called
    print(f'You\'re brother is called {bro}') # print youre brother is called 'something'
else: # else do nothing
    pass

print(f'You\'re dad is called {dad}') # prints your dads name
print(f'You\'re mom is called {mom}') # prints your moms name
