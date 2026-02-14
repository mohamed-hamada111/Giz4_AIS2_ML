import tkinter as tk

class SalaryPrediction:
    def __init__(self, root):
        self.root = root
        self.root.title("Depi Diploma for AI")
        self.root.geometry('500x400')
        self.create_widgets()

    def create_widgets(self):
        header = tk.Label(
            self.root,
            text='Depi - Machine Learning Diploma',
            bg='blue',
            fg='white',
            font=('Arial', 20, "bold")
        )
        header.pack(fill=tk.X)


if __name__ == '__main__':
    root = tk.Tk()
    app = SalaryPrediction(root)
    root.mainloop()
