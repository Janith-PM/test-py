# class
class Predict(object):
    def __init__(self):
        self.reretrieverCount = 0
        self.excludeCount = 0
        self.trailerCount = 0
        self.ProgressCount = 0

    def checkRange(self, num):
        if num % 20 == 0 and 0 <= num <= 120:
            return True
        else:
            return False

    def checkTotal(self, pass_, defer, fail):
        if(pass_ + defer + fail == 120):
            return True
        else:
            return False

    def prediction(self, pass_, defer, fail):
        if self.checkTotal(pass_, defer, fail):
            if(pass_ == 120 and defer == 0 and fail == 0):
                print('Progress')
                self.ProgressCount += 1
            elif(pass_ == 100 and 0 <= defer <= 20 and 0 <= fail <= 20):
                print('Progress (module trailer)')
                self.trailerCount += 1
            elif(0 <= pass_ <= 40 and 0 <= defer <= 40 and 80 <= fail <= 120):
                print('Exclude')
                self.excludeCount += 1
            elif(0 <= pass_ <= 80 and 0 <= defer <= 120 and 0 <= fail <= 60):
                print('Do not progress - module retriever)')
                self.reretrieverCount += 1
            else:
                print('error : invalied Entry')
        else:
            print('Total Incorrect')

    def getInput(self):
        while True:
            pass_ = input('Please enter your credits at Pass : ')
            try:
                pass_ = int(pass_)
                if not self.checkRange(pass_):
                    print('Out of range')
                    continue
                else:
                    while True:
                        defer = input('Please enter your credits at defer : ')
                        try:
                            defer = int(defer)
                            if not self.checkRange(defer):
                                print('Out in range')
                                continue
                            else:
                                while True:
                                    fail = input(
                                        'Please enter your credits at fail : ')
                                    try:
                                        fail = int(fail)
                                        if not self.checkRange(fail):
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

    def horizontalHistrogram(self):
        print('-' * 100)
        print('Horizotal Histrogram\n')
        print(f'Prograss {self.ProgressCount} : ', '*' * self.ProgressCount)
        print(f'Trailer {self.trailerCount} : ', '*' * self.trailerCount)
        print(f'Retriever {self.reretrieverCount} : ',
              '*' * self.reretrieverCount)
        print(f'Excluded {self.excludeCount} : ', '*' * self.excludeCount)

    def verticalHistrogarm(self):
        print('-' * 100)
        print('Vertical Histrogram\n')
        print(' '.join(['Prograss', 'Trailer', 'Retriever', 'Excluded']))
        for x in range(max(self.ProgressCount, self.trailerCount, self.reretrieverCount, self.excludeCount)):
            print(" {0}     {1}     {2}     {3}".format(
                '*   ' if x < self.ProgressCount else '     ',
                '*   ' if x < self.trailerCount else '     ',
                '*   ' if x < self.reretrieverCount else '     ',
                '*   ' if x < self.excludeCount else '     '
            ))


# MAIN PROGRAMME
# making a new instent
pr = Predict()
print('-' * 100)
print('Staff Version With Historgram\n')

if __name__ == '__main__':
    while True:
        pass_, defer, fail = pr.getInput()
        pr.prediction(pass_, defer, fail)
        while True:
            cmd = input(
                "\nWould you like to enter another set of data? \nEnter 'y' for Yes or 'q' to Quit and view result : ")
            if cmd.lower() == 'q':
                pr.horizontalHistrogram()
                pr.verticalHistrogarm()
                exit()
            elif cmd.lower() == 'y':
                print('')
                break
            else:
                print('[x] Error : Invalied input')
                continue
