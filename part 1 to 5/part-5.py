#Part - 5

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


def horizontalHistrogram():
    print('Horizotal Histrogram\n')
    print(f'Prograss {ProgressCount} : ', '*' * ProgressCount)
    print(f'Trailer {trailerCount} : ', '*' * trailerCount)
    print(f'Retriever {reretrieverCount} : ', '*' * reretrieverCount)
    print(f'Excluded {excludeCount} : ', '*' * excludeCount, '\n')


# data set
data = [[120, 0, 0], [100, 20, 0], [100, 0, 20], [80, 20, 20], [60, 40, 20], [
    40, 40, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100], [0, 0, 120]]

for row in data:
    predict(row[0], row[1], row[2])

horizontalHistrogram()
print(str(reretrieverCount + excludeCount +
          trailerCount + ProgressCount), 'outcomes in total')
