reretrieverCount = 0
excludeCount = 0
trailerCount = 0
ProgressCount = 0


def predict(pass_=0, defer=0, fail=0):
    global reretrieverCount
    global excludeCount
    global trailerCount
    global ProgressCount

    if(pass_ + defer + fail == 120):
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


def checkRange(num):
    if num % 20 == 0 and 0 <= num <= 120:
        return True
    else:
        return False


def gettingInput():
    while True:
        pass_ = input('Please enter your credits at Pass : ')
        try:
            pass_ = int(pass_)
            if not checkRange(pass_):
                print('out of range')
                continue
            else:
                while True:
                    defer = input('Please enter your credits at Pass : ')
                    try:
                        defer = int(defer)
                        if not checkRange(defer):
                            print('out of range')
                            continue
                        else:
                            while True:
                                fail = input(
                                    'Please enter your credits at Pass : ')
                                try:
                                    fail = int(fail)
                                    if not checkRange(fail):
                                        print('out of range')
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


def horizontalHistrogram(reretrieverCount, excludeCount, trailerCount, ProgressCount):
    print('-' * 100)
    print('Horizotal Histrogram\n')
    print(f'Prograss {ProgressCount} : ', '*' * ProgressCount)
    print(f'Trailer {trailerCount} : ', '*' * trailerCount)
    print(f'Retriever {reretrieverCount} : ', '*' * reretrieverCount)
    print(f'Excluded {excludeCount} : ', '*' * excludeCount)


def verticalHistrogarm(reretrieverCount, excludeCount, trailerCount, ProgressCount):
    print('-' * 100)
    print('Vertical Histrogram\n')
    header = ['Prograss', 'Trailer', 'Retriever', 'Excluded']
    print(' '.join(header))
    for x in range(max(ProgressCount, trailerCount, reretrieverCount, excludeCount)):
        print(" {0}     {1}     {2}     {3}".format(
            '*    ' if x < ProgressCount else '     ',
            '*    ' if x < trailerCount else '     ',
            '*    ' if x < reretrieverCount else '     ',
            '*    ' if x < excludeCount else '     '
        ))


print('-' * 100)
print('Staff Version With Historgram\n')
pass_, defer, fail = gettingInput()
predict(pass_, defer, fail)
while True:
    cmd = input(
        f"\nWould you like to enter another set of data? \nEnter 'y' for Yes or 'q' to Quit and view result : ")
    print('\n')
    if cmd == 'y':
        pass_, defer, fail = gettingInput()
        predict(pass_, defer, fail)
    elif cmd == 'q':
        horizontalHistrogram(reretrieverCount, excludeCount,
                             trailerCount, ProgressCount)
        verticalHistrogarm(reretrieverCount, excludeCount,
                           trailerCount, ProgressCount)
        exit()
    else:
        print('[x] Error : Invalied input')
        continue
