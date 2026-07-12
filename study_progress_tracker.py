# Calculate study progress percentage
# Example:
# 8 completed out of 10 tasks.
# Output:
# 80% completed
# Mark a task as completed
# Concepts:
#Function
# Arithmetic
# Return values
def add_tasks():
 tasks =[]
 while True:
    task= input("Enter your task: ")
    subject =input ("Enter subject of your task:")
    status_of_task = False
    new_task = {
    "status_of_task" :status_of_task,
    "task": task ,
    "subject": subject,
    }
    tasks.append(new_task)
    
    ans = input("Do you want to add another task? (yes/no): ").lower()
    if ans =="yes":
        continue

    if ans =="no": 
        return tasks

def mark_completed(tasks):
 while True:
  task_no = input("Which task do you want to get completed?:")
  if task_no == ""  :
    print("no task completed")
    break
  # Handle non-numeric input without crashing the program.
  try:
    task_no = int(task_no)
  except ValueError:
     print("invalid")
     print("Enter valid value")   
     continue
  if task_no < 1 or task_no > len(tasks) :
    print("invalid")
    print("Enter valid value")
  else: 
    for index,task in enumerate(tasks,start =1):
           if (index == task_no):
              print(task_no, "completed")
              task["status_of_task"] = True
  
  choice=input("Do you want any other task to be completed?yes/no:").lower()
  if choice == "yes":
     continue
  elif choice == "no" :
    break
 return tasks

def display_tasks(tasks):     
    print("\nYour Tasks\n")
    for i, task in enumerate(tasks, start=1):
            print(f"Task {i}")
            print(f"Task Name : {task['task']}")
            print(f"Subject   : {task['subject']}")
            status = "Completed" if task["status_of_task"] else "Pending"
            print(f"Status     : {status}")
            print("-" * 25)

def count_completed(tasks):    
 count = 0       
 for task in tasks:  
     if task['status_of_task']==True :  
      count += 1
 return count
     

def calculate_percentage(completed_tasks,total_tasks):
  percentage =(completed_tasks/total_tasks)*100
  return percentage

def main():
    tasks = add_tasks()
    mark_completed(tasks)
    display_tasks(tasks)
    completed_tasks = count_completed(tasks)
    percentage = calculate_percentage(completed_tasks,len(tasks))
    print(f"{percentage}% completed")
    print(f"{completed_tasks } out of {len(tasks)} tasks completed")

main()
    

          

    