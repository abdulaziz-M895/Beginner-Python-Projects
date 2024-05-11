# With Some ChatGPT help :)

todo_list = {}

def add_task():
  """
  Function to add a task to the to-do list.
  """
  item = input('Todo: ')
  if item in todo_list:
      print('Todo already exists.')
  else:
      todo_list[item] = False  # Set task as not done initially
      print('Task added successfully.')

def remove_task():
    """
    Function to remove a task from the to-do list.
    """
    if len(todo_list.keys()) == 0:
        print('No Tasks to Remove.')
        return
    
    item = input('Todo to remove: ')
    if item in todo_list:
        del todo_list[item]
        print('Task removed successfully.')
    else:
        print('There is no such item.')


def mark_task_done():
  """
  Function to mark a task as done in the to-do list.
  """
  item = input('Todo to mark as done: ')
  if item in todo_list:
      todo_list[item] = True
      print('Task marked as done.')
  else:
      print('There is no such item.')

def view_tasks():
  """
  Function to view the entire to-do list along with task statuses.
  """
  print("To-Do List:")
  for task, done in todo_list.items():
      status = "Done" if done else "Not Done"
      print(f"{task}: {status}")

# Main program loop
while True:
  command = input('Add, Remove, Mark Done, View or Exit: ').lower()
  if command == 'add':
      add_task()
  elif command == 'remove':
      remove_task()
  elif command == 'mark done':
      mark_task_done()
  elif command == 'view':
      view_tasks()
  elif command == 'exit':
      break
  else:
      print('Invalid Option')