import predict
# MAIN PROGRAMME
# making a new instent
pr = predict.Predict()
print('-' * 100)
print('Staff Version With Historgram\n')

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
