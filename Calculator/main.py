from calculator import Calculator
import tkinter as tk

def main():
    screen = tk.Tk()
    calc = Calculator(screen)
    screen.mainloop()

if __name__ == "__main__":
    main()