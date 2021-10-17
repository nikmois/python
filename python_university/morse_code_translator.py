import tkinter
from tkinter.font import Font
from tkinter import *
from tkinter import messagebox

top = tkinter.Tk()
top.title("Morse code translator")
top.geometry('350x320')
top.configure(bg="black")

font_1 = Font(family='fixedsys',
              size=14,
              weight='normal')

font_2 = Font(family='fixedsys',
              size=9,
              weight='normal')

text = StringVar()
code = StringVar()



l = Label(top, text="MORSE CODE TRANSLATOR", font = font_1, bg="black", fg = "chartreuse2")

l.grid(row = 1, columnspan = 2, padx = 50, pady = 15)



L1 = Label(top, text = "TEXT", padx = 5, font = font_2, bg="black", fg = "chartreuse2")
L1.grid(row = 2, column = 0, sticky = 'W', padx = 10, pady = (25,5))
E1 = Entry(top, textvariable = text, bd = 5, font = font_2, bg="black", fg = "chartreuse2")
E1.grid(row = 2, column = 1, sticky = 'W', padx = 50, pady = (25,5))

scrollbar1 = Scrollbar(top, orient = 'horizontal', command = E1.xview, width = 14)
scrollbar1.grid(row = 3, column = 1, sticky = 'we', padx = 50)
E1.configure(xscrollcommand=scrollbar1.set)

L2 = Label(top, text = "CODE", padx = 5, font = font_2, bg="black", fg = "chartreuse2")
L2.grid(row = 4, column = 0, sticky = 'W', padx = 10, pady = (25, 5))
E2 = Entry(top, bd = 5, textvariable = code, font = font_2, bg="black", fg = "chartreuse2")
E2.grid(row = 4, column = 1, sticky = 'W', padx = 50, pady = (25, 5))

scrollbar2 = Scrollbar(top, orient = 'horizontal', command = E2.xview, width = 14)
scrollbar2.grid(row = 5, column = 1, sticky = 'we', padx = 50)
E2.configure(xscrollcommand=scrollbar2.set)

var = IntVar()
def clearMorse():
    morse_code = code.get()
    code_length = len(morse_code)
    E2.delete(0, code_length)

def clearText():
    entered_text = text.get()
    text_length = len(entered_text)
    E1.delete(0, text_length)


L3 = Label(top, text = "TO MORSE", padx = 5, font = font_2, bg="black", fg = "chartreuse2")
L3.grid(row = 6, column = 0, sticky = 'W', padx = 10, pady = (5, 0))
R1 = Radiobutton(top, bg = 'black', variable = var, value = 1, cursor = 'hand2', command = clearMorse, activebackground = 'black', activeforeground = "chartreuse2")
R1.grid(row = 6, column = 1, sticky = 'W', pady = (5, 0))


L4 = Label(top, text = "TO TEXT", padx = 5, font = font_2, bg="black", fg = "chartreuse2")
L4.grid(row = 7, column = 0, sticky = 'W', padx = 10, pady = 1)
R2 = Radiobutton(top, bg = 'black', variable = var, value = 2, cursor = 'hand2', command = clearText, activebackground = 'black', activeforeground = "chartreuse2")
R2.grid(row = 7, column = 1, sticky = 'W')

def message1():
        messagebox.showinfo("Text or code is missing", "Please write text or code which you want to translate")


def message2():
    messagebox.showinfo("Choose morse or text", "Please choose in what you want to translate. Choose 'TO MORSE' or 'TO TEXT'")

def message3():
    messagebox.showinfo("Error", "You can only write letters, numbers or spaces into 'TEXT' field")

def message4():
    messagebox.showinfo("Error", "You can only write '-', '.', '|' or spaces into 'CODE' field. Please put space after every morse character. To put space between words use '|'. Put spaces before and after '|'")

def unknown():
    messagebox.showinfo("Error", "Unknown Error appeared. Please try again later.")

def translate():
    value = var.get()
    text1 = text.get()
    code1 = code.get()
    library = {' ': '|','0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
	'7': '--...', '8': '---..', '9': '----.','A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
	'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
	'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
    library1 = {' ': '', '|': ' ', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
	'--...': '7', '---..': '8', '----.': '9','.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
	'--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
	'--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}
    if text1 or code1:
        if value:
            if value == 1:
                try:
                    E2.delete(0, len(code1))
                    morseCode = ""
                    for x in text1:
                        morseCode += library[x.upper()] + " "
                    E2.insert(0, morseCode)
                    E2.delete(len(morseCode)-1, len(morseCode))
                except KeyError:
                    message3()
                except:
                    unknown()
            else:
                try:
                    E1.delete(0, len(text1))
                    textEntry = ""
                    code2 = code1.split(" ")
                    for x in code2:
                        textEntry += library1[x]
                    E1.insert(0, textEntry)
                except KeyError:
                    message4()
                except:
                    unknown()
        else:
            message2()
    else:
        message1()


but = Button(top, command = translate, text="TRANSLATE", font = font_1, bg = 'black', bd = 5, fg = "chartreuse2", activebackground = 'black', activeforeground = "chartreuse2")
but.grid(row = 6, column = 1, pady = (40, 0))


top.mainloop()
