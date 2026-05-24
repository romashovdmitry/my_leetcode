from time import sleep


def print_and_sleep(value, line_break=True, sleepy=True):
    
    if line_break:
        print('\n')

    print(value)

    if sleepy:
        sleep(1)