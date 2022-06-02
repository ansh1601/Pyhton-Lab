class TODOreminder:
    def __init__(self,TODOlist=[]):
        self.TODOlist = TODOlist
    def list_todo(self):
        for i in range(0,len(self.TODOlist)):
            print(str(i+1) + " : " + self.TODOlist[i])
    def new_todo(self):
        self.TODOlist.append('submit timesheet')
        print(self.TODOlist)
    def remove_todo(self):
        self.TODOlist.pop(1)
        print(self.TODOlist)
obj = TODOreminder(['gym','study','play football'])
obj.list_todo()
obj.new_todo()
obj.remove_todo()
        
