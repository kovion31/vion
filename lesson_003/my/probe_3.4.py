x = 42
print('дратути!')
if x < 0:
    print('Меньше нуля')
    result = -1
elif x == 0:
    print('Равно нулю')
    result = 0
elif x == 1:
    print('Равно единице')
    result = 1
else:
    print('Больше нуля, но не равно единице')
    if x == 42:
        print('Вау!')
    result = 42
print('дотвидания!')