from tkinter import Tk, BOTH, Canvas

class Window:
    
    def __init__(self,width,height):
        self.__root = Tk()
        self.__root.titile("Maze Solver")
        self.__canvas = Canvas(self.__root,height=height,width=width)
        self.__canvas.pack(fill=BOTH,expand=1)
        self.__running=False
        self.__root.protocol("WM_DELETE_WINDOW",self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running= True
        while(self.__unning):
            self.redraw()
        print("Window closed ...")
    
    def close(self):
        self.__running= False
    
    
    def draw_line(self,Line,fill_color="black"):
        Line.draw(self.__canvas,fill_color)
class Point:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Line:

    def __init__(self,p1,p2):
        self.__p1 = p1
        self.__p2 = p2

    def draw(self,canvas,fill_color):
        x1,y1 = self.__p1.x,self.__p1.y
        x2,y2 = self.__p2.x,self.__p2.y
        canvas.create_line(x1,y1,x2,y2,fill = fill_color,width=2)
        canvas.pack(fill=BOTH,expand=1)