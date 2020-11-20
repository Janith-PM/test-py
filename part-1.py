# Part - 1 function for predict progression outcome
def predict(pass_=0, defer=0, fail=0):
    if (pass_ == 120 and defer == 0 and fail == 0):
        print('Progress')
    elif(pass_ == 100 and 0 <= defer <= 20 and 0 <= fail <= 20):
        print('Progress (module trailer)')
    elif(0 <= pass_ <= 40 and 0 <= defer <= 40 and 80 <= fail <= 120):
        print('Exclude')
    elif(0 <= pass_ <= 80 and 0 <= defer <= 120 and 0 <= fail <= 60):
        print('Do not progress - module retriever')
    else:
        print('error : invalied Entry')


# function calling
pass_ = int(input('Please enter your credits at Pass : '))
defer = int(input('Please enter your credits at defer : '))
fail = int(input('Please enter your credits at fail : '))

predict(pass_, defer, fail)
