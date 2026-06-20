import tkinter as tk

window = tk.Tk()

window.title("โปรแกรมบันทึกผลการเรียน")
window.geometry("800x600")

title_label = tk.Label(
    window,
    text="โปรแกรมบันทึกผลการเรียน",
    font=("Kanit", 20)
)

title_label.pack(pady=20)

window.mainloop()