import os


class Task:
    def __init__(self, name, status = "processing"):
        self.id = None
        self.name = name
        self.status = status


class TaskManager:
    file_path = "tasks.txt"

    @staticmethod
    def add_task(new_task: Task):
        with open(TaskManager.file_path, 'a') as f:
            content = f"{new_task.name},{new_task.status}\n"
            f.write(content)

    @staticmethod
    def done_task(task_no):  # this work in my list has done
        with open(TaskManager.file_path, 'r') as f:
            index = task_no - 1
            lines = f.read().splitlines()
            if 0 <= index < len(lines):
                line = lines[index]
                current_status = line.split(',')[1]
                lines[index] = line.replace(current_status, "done")
            else:
                print("Task does not exist")
        with open(TaskManager.file_path, 'w') as f:
            f.write('\n'.join(lines))

    @staticmethod
    def remove_task(task_no):
        with open(TaskManager.file_path, 'r') as f:
            index = task_no - 1
            lines = f.read().splitlines()
            if 0 <= index < len(lines):
                lines.pop(index)
            else:
                print("Task does not exist")
        with open(TaskManager.file_path, 'w') as f:
            f.write('\n'.join(lines))

    @staticmethod
    def display_list():
        with open(TaskManager.file_path, 'r') as f:
            lines = f.read().splitlines()
            for line_no, line in enumerate(lines, 1):
                print(line_no, line.split(","))


if __name__ == '__main__':
    tm = TaskManager()
    tm.add_task(new_task=Task(name="Task 1", status="processing"))
    tm.add_task(new_task=Task(name="Task 2", status="done"))
    tm.display_list()
    print("----------------------------")
    tm.done_task(1)
    tm.display_list()
    print("--------------------------")
    tm.remove_task(1)
    tm.display_list()
