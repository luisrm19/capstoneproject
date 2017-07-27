import tkinter as tk



class Data:
    ''' The model. '''
    def __init__(self):
        self.bins = ['','','']

class Greeting (tk.Frame):

    def __init__(self,root):
        tk.Frame.__init__(self, root)
        self.vals = ['',0,0,1]
        
        self.name = tk.Entry(root)
        tk.Label(root, text="Database Name").grid(row=0, sticky = 'e')

        self.row = tk.Entry(root)
        tk.Label(root, text="Number of Rows").grid(row=1, sticky = 'e')


        self.col = tk.Entry(root)
        tk.Label(root, text="Number of Cols").grid(row=2, sticky = 'e')

        
                
        self.name.grid(row=0,column=1)
        self.row.grid(row=1, column=1)
        self.col.grid(row=2, column=1)


        self.button = tk.Button(root, text="Get", command=self.on_button)
        self.button.grid(row=4)

    def on_button(self):
        self.vals = [self.name.get(),self.row.get(),self.col.get(),0]
        


class Mainwin(tk.Frame):
    def __init__(self,root):
        tk.Frame.__init__(self, root)
        tk.Label(root, text="new main window").grid(row=0, sticky = 'e')


class Controller:
    def __init__(self, root):
        self.data = Data() # the model
        self.greeting = Greeting(root) # the view
        if(self.greeting.vals[3]==0):
            print(self.greeting.vals[3])
            self.data.bins[0] = self.greeting.vals[0]
            self.data.bins[1] = self.greeting.vals[1]
            self.data.bins[2] = self.greeting.vals[2]
            print(self.data.bins)
        #if(self.greeting.vals[3]==0):
        #   self.mainwin = Mainwin(root)


if __name__ == '__main__':
    root = tk.Tk()
    Controller(root)
    root.mainloop()
