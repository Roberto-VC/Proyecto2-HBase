from src import *

if __name__ == '__main__':
    print('---- Welcome to HDFS simulation ----')
    print('Type a command to manipulate data or type "exit" to quit')

    command = ''
    while command != 'exit':
        command = input('\nHDFS> ')
        output = process_input(command)
        print(output)

    print('Exiting HDFS\n')
