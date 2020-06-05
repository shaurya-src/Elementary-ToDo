def show_menu():
    print('MENU:')
    print('1. Add a task')
    print('2. Show To-Do list')
    print('3. Mark as done')
    print('4. Exit')


def add_tasks(task):
    with open('data.txt', 'a+') as f:
        f.write(task)
        f.write('\n')


def show_todo():
    with open('data.txt', 'r+') as f:
        tasks = f.readlines()
        for i in range(len(tasks)):
            print('{}. {}'.format(i + 1, tasks[i].strip()))
        print('(Total {} tasks).'.format(len(tasks)))


def mark_as_done(index):
    with open('data.txt', 'r') as f1:
        tasks = f1.readlines()
    item = tasks[index - 1].strip('\n')
    with open('data.txt', 'w') as f2:
        for task in tasks:
            if task.strip('\n') != item:
                f2.write(task)
    print('"{}" is marked as done.'.format(item))


choice = 0
show_menu()

while choice != '4':
    choice = input('Enter your choice: \t')

    if choice == '1':
        t = input('Enter the task: ')
        add_tasks(t)
        print('Item added: {}'.format(t))
    elif choice == '2':
        print('To-do List:')
        show_todo()
    elif choice == '3':
        show_todo()
        while True:
            x = input('Select the task to be marked as done: ')
            try:
                mark_as_done(int(x))
                break
            except Exception:
                print('Select a valid task.')

    elif choice == '4':
        print('See ya!')
    else:
        print('Try again by entering a valid choice.')
