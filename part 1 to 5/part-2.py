#Part - 2
# function for check range


def checkRange(num):
    if num % 20 == 0 and 0 <= num <= 120:
        return True
    else:
        return False

# function for check total


def checkTotal(pass_, defer, fail):
    if(pass_ + defer + fail == 120):
        return True
    else:
        return False

# function for predict


def predict(pass_=0, defer=0, fail=0):
    if(checkTotal(pass_, defer, fail)):
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
    else:
        print('Total incorrect')

# getting information from user and check data type


def getInput():
    while True:
        pass_ = input('Please enter your credits at Pass : ')
        try:
            pass_ = int(pass_)
            if not checkRange(pass_):
                print('Out of range')
                continue
            else:
                while True:
                    defer = input('Please enter your credits at defer : ')
                    try:
                        defer = int(defer)
                        if not checkRange(defer):
                            print('Out in range')
                            continue
                        else:
                            while True:
                                fail = input(
                                    'Please enter your credits at fail : ')
                                try:
                                    fail = int(fail)
                                    if not checkRange(fail):
                                        print('Out of range')
                                        continue
                                    else:
                                        break
                                except:
                                    print('Integer Required')
                                    continue
                                break
                    except:
                        print('Integer Required')
                        continue
                    break
        except:
            print('Integer Required')
            continue
        break
    return pass_, defer, fail


# function call
pass_, defer, fail = getInput()
predict(pass_, defer, fail)
