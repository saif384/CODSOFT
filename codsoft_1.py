from tkinter import *
class ToDo:
    def __init__(self, root):
        self.root = root
        self.root.title('TO-DO-LIST')
        self.root.geometry('650x410+300+150')
        self.label=Label(self.root,text='To-Do-List App',font='ariel, 25 bold',width=8,bd=4,bg='blue',fg='white')
        self.label.pack(side='top',fill=X)
        self.label=Label(self.root,text='Add Task',font='ariel, 22 bold',width=8,bd=5,bg='blue',fg='white')
        self.label.place(x=40, y=50)
        self.label = Label(self.root, text='Tasks', font='ariel, 22 bold', width=8, bd=4, bg='blue', fg='white')
        self.label.place(x=350, y=50)
        self.main_text=Listbox(self.root,height=9,bd=4,width=20,font='ariel, 20 italic bold')
        self.main_text.place(x=330,y=100)
        self.text=Text(self.root,bd=5,height=2,width=30,font='ariel, 10 bold')
        self.text.place(x=20,y=120)
        def add():
            content=self.text.get(1.0,END)
            self.main_text.insert(END,content)
            with open('data.txt','a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)
        def delete():
            delete_=self.main_text.curselection()
            look=self.main_text.get(delete_)
            with open('data.txt','r+') as f:
                new_f=f.readline()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)
        with open('data.txt','r') as f:
            read=f.readlines()
            for i in read:
                ready=i.split()
                self.main_text.insert(END,ready)
            f.close()
        self.button=Button(self.root,text='Add',font='Times, 20 bold',width=10,bd=4,bg='blue',fg='white',command=add)
        self.button.place(x=30,y=190)
        self.button2 = Button(self.root, text='Delete', font='Times, 20 bold', width=10, bd=4, bg='blue', fg='white',command=delete)
        self.button2.place(x=30, y=250)

def main():
    root=Tk()
    vi=ToDo(root)
    root.mainloop()

if __name__ == '__main__':
    main()