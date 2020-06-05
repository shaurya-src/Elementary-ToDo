def show_menu():
    print('MENU:')
    print('1. Add a task')
    print('2. Show To-Do list')
    print('3. Mark as done')
    print('4. Exit')


def show_todo(task_list):
    for i, item in enumerate(task_list):
        print('{}. {}'.format(i + 1, item))


tasks, choice = [], 0
show_menu()

while choice != '4':
    choice = input('Enter your choice: \t')

    if choice == '1':
        t = input('Enter the task: ')
        tasks.append(t)
        print('Item added: {}'.format(t))
    elif choice == '2':
        print('To-do List:')
        show_todo(tasks)
        print('(Total {} tasks).'.format(len(tasks)))
    elif choice == '3':
        show_todo(tasks)
        while True:
            try:
                x = int(input('Select the task to be marked as done: '))
                print('"{}" is marked as done.'.format(tasks[x-1]))
                del tasks[x - 1]
                break
            except Exception:
                print('Select a valid task!')
    elif choice == '4':
        print('See ya!')
    else:
        print('Try again by entering a valid choice.')
