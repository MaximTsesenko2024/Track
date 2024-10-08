""" Головной файл проекта по отображению графика полёта тела под углом к горизонту"""
import tkinter
import Calc_track as Clt


class Interfece:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry('400x200')
        self.window.title('Полёт тела под углом к горизонту')
        self.window.resizable(False, False)
        self.lbl_speed = tkinter.Label(self.window, text="Начальная скорость в м/с")
        self.lbl_speed.place(x=10, y=30)
        self.ent_speed = tkinter.Entry(self.window)
        self.ent_speed.place(x=170, y=30)
        self.lbl_angle = tkinter.Label(self.window, text="Начальный угол в градусах")
        self.lbl_angle.place(x=10, y=60)
        self.ent_angle = tkinter.Entry(self.window)
        self.ent_angle.place(x=170, y=60)
        self.btn = tkinter.Button(self.window, text='Построить график', command=self.create)
        self.btn.place(x=70, y=100)

    def create(self):
        def str_to_float(string):
            if len(string) == 0:
                return None
            try:
                rez = float(string)
            except Exception:
                return None
            else:
                return rez

        v = str_to_float(self.ent_speed.get())
        a = str_to_float(self.ent_angle.get())
        if v is None or a is None:
            return 1
        Clt.fly(v, a)


if __name__ == '__main__':
    graf = Interfece()
    graf.window.mainloop()
