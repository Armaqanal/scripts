import argparse
class TaskManager:
    task_list=[]
    def __init__(self):
        task_done=False
    def add_task(self,add):
        self.task_list.append(add) #should be self or class name
    def done_task(self,done_task): #this work in my list has done
        self.done_task=[]
        for i in self.task_list:
            if i:
                self.task_done=True
                self.done_task.append(i)
        return None

    def remove_task(self,remove):
        self.remove_task=remove
        for index,name in enumerate(1,self.task_list):
            if 0 < index +1 <= len(self.task_list):
                del index

    def display_list():
        pass

        
parser=argparse.ArgumentParser()
parser.add_argument("chose",choices=["add" , "done" , "remove","list"],help="tasks")
args=parser.parse_args()
if args.choices == "add" :
    
elif args.choices == "done":
    pass    
elif args.choices == "remove":   
    pass 



#parser.add_argument("action" , entekhab = ["add" , "done" , "remove"]


# if args.action == "add" :
#     pass
# elif args.action == "done":
#     pass    
# elif args.action == "remove":   
#     pass 