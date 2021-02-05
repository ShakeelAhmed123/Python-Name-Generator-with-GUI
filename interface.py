from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Spinbox
import random
import time as t


def f3(f_name):
    f_3 = f_name[0], f_name[1], f_name[2]
    return f_3


def l3(l_name):
    l_3 = l_name[-3], l_name[-2], l_name[-1]
    return l_3


def f4(f_name):
    f_4 = f_name[0], f_name[1], f_name[2], f_name[3]
    return f_4


def l4(l_name):
    l_4 = l_name[-4], l_name[-3], l_name[-2], l_name[-1]
    return l_4


def on_click():
    file = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    f = open(file)
    names = f.read()
    names = names.splitlines()
    f.close()
    my_text.config(state='normal')
    my_text.delete(1.0, END)
    my_text.config(state='disabled')

    for name in names:
        my_text.config(state='normal')
        my_text.insert(END, name)
        my_text.insert(END, '\n')
    my_text.config(state='disabled')

    def on_gen():
        space3 = Label(window, height=1, bg='coral')
        space3.grid(column=1, row=11)

        window.geometry('480x750')
        window.minsize(480, 750)
        window.maxsize(480, 750)

        show_output = scrolledtext.ScrolledText(window, width=55, height=10, font=('Arial Bold', 11), state='disabled')
        show_output.grid(column=1, row=12)

        show_output.config(state='normal')
        show_output.delete(1.0, END)
        show_output.config(state='disabled')

        show_output.config(state='normal')

        delay = time.get()
        t_end = t.time() + int(delay)

        while t.time() <= t_end:

            f_name = random.choice(names)
            l_name = random.choice(names)

            f_len = len(f_name)
            l_len = len(l_name)

            if f_len == 3 and l_len == 3:
                f_3 = f3(f_name)
                l_3 = l3(l_name)

                bro = f_3 + l_3
                br = ''.join(bro)
                show_output.insert(END, br)
                show_output.insert(END, '\n')

            elif f_len == 3 and l_len > 3:
                f_3 = f3(f_name)
                l_4 = l4(l_name)

                bro = f_3 + l_4
                br = ''.join(bro)
                show_output.insert(END, br)
                show_output.insert(END, '\n')

            elif f_len > 3 and l_len == 3:
                f_4 = f4(f_name)
                l_3 = l3(l_name)

                bro = f_4 + l_3
                br = ''.join(bro)
                show_output.insert(END, br)
                show_output.insert(END, '\n')

            elif f_len > 3 and l_len > 3:
                f_4 = f4(f_name)
                l_4 = l4(l_name)

                bro = f_4 + l_4
                br = ''.join(bro)
                show_output.insert(END, br)
                show_output.insert(END, '\n')

            else:
                pass

        if t.time() > t_end:

            def exp_logic():
                exp_file = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
                exp = open(exp_file, 'w')
                ow = 'Overwrite File?'
                ye = "Exporting names to this file will overwrite all of it's previous content. Do you wish to proceed?"
                res = messagebox.askyesno(ow, ye)

                if res is True:
                    temp = show_output.get(1.0, END)
                    exp.write(temp)
                    exp.close()
                else:
                    exp.close()

            def dupes():
                show_output.config(state='normal')

                string = ""
                temp_str = show_output.get(1.0, END)
                string += temp_str
                string = string.splitlines()

                my_list = list(dict.fromkeys(string))
                show_output.delete(1.0, END)
                for name_ in my_list:
                    show_output.insert(END, name_)
                    show_output.insert(END, '\n')
                show_output.config(state='disabled')

            dp_space = Label(window, height=1, bg='coral')
            dp_space.grid(column=1, row=13)

            dp = Button(window, text='Remove Duplicates', bg='coral', fg='Black', font=('Arial Bold', 11))
            dp.config(command=dupes)
            dp.grid(column=1, row=14)

            txt_t = 'Export names as Text file'
            export = Button(window, text=txt_t, bg='coral', fg='Black', font=('Arial Bold', 11), command=exp_logic)
            export.grid(column=1, row=16)

            messagebox.showinfo('Operation Ended!', 'Names have been generated!')

            # space6 = Label(window, height=1, bg='coral')
            # space6.grid(column=1, row=17)

        show_output.config(state='disabled')

    gen_button.config(state='normal', command=on_gen)

    var = IntVar()
    var.set(5)

    space4 = Label(window, height=1, bg='coral')
    space4.grid(column=1, row=9)

    time = Spinbox(window, from_=1, to=100, width=10, textvariable=var)
    time.grid(column=1, row=10)

    space5 = Label(window, height=1, bg='coral')
    space5.grid(column=1, row=15)


window = Tk()
window.configure(bg='coral')
window.geometry('480x480')
window.minsize(480, 480)
window.maxsize(480, 480)
window.title("Name Generator")

hello = Label(window, text="Hello, Welcome to Names Generator", bg='coral', font=('Arial Bold', 20))
hello.grid(column=1, row=1)

p = 'Please select the text file with the names, separated by lines'
ins = Label(window, height=1, text=p, bg='coral', font=('Arial Bold', 11))
ins.grid(column=1, row=2)

p2 = 'And make sure there are no spaces'
txt = Label(window, height=1, text=p2, bg='coral', font=('Arial Bold', 11))
txt.grid(column=1, row=3)

opn_button = Button(window, text="File", bg='coral', fg='Black', font=('Arial Bold', 11), command=on_click)
opn_button.grid(column=1, row=4)
opn_button.config(height=1, width=15)

space = Label(window, height=1, bg='coral')
space.grid(column=1, row=5)

my_text = scrolledtext.ScrolledText(window, width=55, height=10, font=('Arial Bold', 11), state='disabled')
my_text.grid(column=1, row=6)

space2 = Label(window, height=1, bg='coral')
space2.grid(column=1, row=7)

gen_button = Button(window, text='Generate Names', bg='coral', fg='Black', font=('Arial Bold', 11), state='disabled')
gen_button.grid(column=1, row=8)

copy = Label(window, text='Made by Shakeel Ahmed Khan', bg='coral')
copy.grid(column=1, row=17)

window.mainloop()
