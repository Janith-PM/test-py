#Part - 3

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
reretrieverCount = 0
excludeCount = 0
trailerCount = 0
ProgressCount = 0


def predict(pass_=0, defer=0, fail=0):
    global reretrieverCount
    global excludeCount
    global trailerCount
    global ProgressCount
    if(checkTotal(pass_, defer, fail)):
        if (pass_ == 120 and defer == 0 and fail == 0):
            print('Progress')
            ProgressCount += 1
        elif(pass_ == 100 and 0 <= defer <= 20 and 0 <= fail <= 20):
            print('Progress (module trailer)')
            trailerCount += 1
        elif(0 <= pass_ <= 40 and 0 <= defer <= 40 and 80 <= fail <= 120):
            print('Exclude')
            excludeCount += 1
        elif(0 <= pass_ <= 80 and 0 <= defer <= 120 and 0 <= fail <= 60):
            print('Do not progress - module retriever')
            reretrieverCount += 1
        else:
            print('error : invalied Entry')
    else:
        print('Total incorrect')

# getting information from user and check data type


def getInput():
    while True:
        pass_ = input('\nPlease enter your credits at Pass : ')
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


# Horizontal HIstrogram
def horizontalHistrogram():
    print('-' * 100)
    print('Horizotal Histrogram\n')
    print(f'Prograss {ProgressCount} : ', '*' * ProgressCount)
    print(f'Trailer {trailerCount} : ', '*' * trailerCount)
    print(f'Retriever {reretrieverCount} : ', '*' * reretrieverCount)
    print(f'Excluded {excludeCount} : ', '*' * excludeCount)


# function call
# main loop
print('-' * 100)
print('Staff Version With Historgram')

while True:
    pass_, defer, fail = getInput()
    predict(pass_, defer, fail)
    while True:
        cmd = input(
            "\nWould you like to enter another set of data? \nEnter 'y' for Yes or 'q' to Quit and view result : ")
        if cmd.lower() == 'q':
            horizontalHistrogram()
            exit()
        elif cmd.lower() == 'y':
            break
        else:
            print('[x] Error : Invalied input')
            continue
