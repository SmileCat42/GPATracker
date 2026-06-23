import tkinter as tk
from tkinter import ttk
import json


current_table = None

def update_grade():

    global current_table
    if current_table is None:
        return
    
    selected_item = current_table.selection()

    if not selected_item:
        return

    current_table.set(
        selected_item[0],
        "grade",
        grade_var.get()
    )

    values = current_table.item(selected_item[0], "values")
    selected_code = values[0]

    print(selected_code)

    for subject in subjects:
        if subject["code"] == selected_code:
            subject["grade"] = grade_var.get()
            break
    
    print("กำลังบันทึกเกรด")

    with open("course2.json", "w", encoding="utf-8") as file:
        json.dump(
            subjects,
            file,
            ensure_ascii=False,
            indent=4
    )
    
    if current_table == table_wait:
        values = current_table.item(
        selected_item[0],
        "values"
    )

    new_values = (
        values[0],          # code
        values[1],          # name
        values[2],          # credit
        grade_var.get()     # grade ใหม่
    )

    table_wait.delete(
        selected_item[0]
    )

    table_passed.insert(
        "",
        tk.END,
        values=new_values
    )

def on_select(event):
    

    global current_table
    current_table = event.widget
    selected_item = current_table.selection()

    if not selected_item:
        return

    values = current_table.item(selected_item[0], "values")

    code = values[0]
    name = values[1]
    if values[3]:
        grade_combo.set(values[3])
    else:
        grade_combo.set("กรุณาเลือกเกรด")

    selected_subject_label.config(
        text=f"วิชาที่เลือก: {code} {name}"
    )

    grade_combo.config(state="readonly")


window = tk.Tk()

style = ttk.Style()
print(style.theme_names())
style.theme_use("clam")

style.configure(
    "Passed.Treeview",
    background="#E8F5E9",
    fieldbackground="#E8F5E9"
)

style.configure(
    "Wait.Treeview",
    background="#FFF8E1",
    fieldbackground="#FFF8E1"
)
style.configure(
    "Treeview",
    rowheight=30
)

passed_frame = ttk.LabelFrame(
    window,
    text="วิชาที่ผ่านแล้ว"
)

waiting_frame = ttk.LabelFrame(
    window,
    text="วิชาที่ยังไม่ผ่าน"
)
center_frame = ttk.Frame(window)

window.title("โปรแกรมบันทึกผลการเรียน")
window.geometry("800x800")

title_label = tk.Label(
    window,
    text="โปรแกรมบันทึกผลการเรียน",
    font=("Kanit", 20)
)

title_label.pack(pady=20)

table_passed = ttk.Treeview(
    passed_frame,
    columns=("code", "name", "credit", "grade"),
    show="headings",
    style="Passed.Treeview",
)
table_wait = ttk.Treeview(
    waiting_frame,
    columns=("code", "name", "credit", "grade"),
    show="headings",
    style="Wait.Treeview",
)

table_passed.heading("code", text="รหัสวิชา")
table_passed.heading("name", text="ชื่อวิชา")
table_passed.heading("credit", text="หน่วยกิต")
table_passed.heading("grade", text="เกรด")

table_passed.column("code", width=180, anchor="center")
table_passed.column("name", width=350)
table_passed.column("credit", width=100, anchor="center")
table_passed.column("grade", width=100, anchor="center")

table_wait.heading("code", text="รหัสวิชา")
table_wait.heading("name", text="ชื่อวิชา")
table_wait.heading("credit", text="หน่วยกิต")
table_wait.heading("grade", text="เกรด")

table_wait.column("code", width=180, anchor="center")
table_wait.column("name", width=350)
table_wait.column("credit", width=100, anchor="center")
table_wait.column("grade", width=100, anchor="center")

with open("course2.json", "r", encoding="utf-8") as file:
    subjects = json.load(file)

passed_count = 0
wait_count = 0

for subject in subjects:
    values = (
        subject["code"],
        subject["name"],
        subject["credit"],
        subject["grade"]
    )
    if subject["grade"]:
        table_passed.insert(
            "",
            tk.END,
            values=values
        )
        passed_count+=1

    else:
        table_wait.insert(
            "",
            tk.END,
            values=values
        )
        wait_count+=1

grade_var = tk.StringVar()

grade_combo = ttk.Combobox(
    center_frame,
    textvariable=grade_var,
    values=["", "A", "B+", "B", "C+", "C", "D+", "D", "F"],
    state="readonly"
)

grade_combo.set("กรุณาคลิกเลือกวิชา")

update_button = tk.Button(
    center_frame,
    text="💾 บันทึกเกรด",
    font=("Kanit", 11),
    width=15,
    background="#fad96e",
    command=update_grade
)

selected_subject_label = tk.Label(
    center_frame,
    text="ยังไม่ได้เลือกวิชา",
    font=("Kanit", 11)
)

passed_height = min(5, max(3, passed_count))
wait_height = min(7, max(3, wait_count))

table_passed.config(height=passed_height)
table_wait.config(height=wait_height)

passed_scroll = ttk.Scrollbar(
    passed_frame,
    orient="vertical",
    command=table_passed.yview
)

table_passed.configure(
    yscrollcommand=passed_scroll.set,
)

wait_scroll = ttk.Scrollbar(
    waiting_frame,
    orient="vertical",
    command=table_wait.yview
)

table_wait.configure(
    yscrollcommand=wait_scroll.set
)

table_passed.tag_configure(
    "odd",
    background="#6eec94"
)

table_wait.tag_configure(
    "even",
    background="#fa2376"
)

table_passed.bind("<<TreeviewSelect>>", on_select)
table_wait.bind("<<TreeviewSelect>>", on_select)

grade_combo.pack(pady=(20,5))
grade_combo.config(state="disabled") 

passes_label=tk.Label(passed_frame, text="วิชาที่ผ่านแล้ว")
passed_frame.pack(fill="both", expand=True,  padx=20, pady=20)
passed_scroll.pack(
    side="right",
    fill="y"
)
table_passed.pack(
    side="left",
    fill="both",
    expand=True
)

center_frame.pack(fill="x")
waiting_frame.pack(fill="both", expand=True, padx=20, pady=20)
wait_scroll.pack(
    side="right",
    fill="y"
)
table_wait.pack(
    side="left",
    fill="both",
    expand=True
)

selected_subject_label.pack(pady=5)

update_button.pack(pady=20)


window.mainloop()