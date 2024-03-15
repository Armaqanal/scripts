import argparse

from task import Task, TaskManager

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["add", "done", "remove", "list"], help="tasks")
    parser.add_argument("task_name_or_id", nargs='?', help="task name or task id")
    args = parser.parse_args()

    task_manager = TaskManager()

    if args.mode == "add":
        if args.task_name_or_id is not None:
            task_manager.add_task(new_task=Task(args.task_name_or_id))
            print(args.task_name_or_id)
    elif args.mode == "list":
        task_manager.display_list()
    elif args.mode == "done":
        if args.task_name_or_id is not None:
            task_manager.done_task(int(args.task_name_or_id))
    elif args.mode == "remove":
        if args.task_name_or_id is not None:
            task_manager.remove_task(int(args.task_name_or_id))
