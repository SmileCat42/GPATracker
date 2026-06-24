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
    update_gpa()

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

def update_gpa():
    grade_points = {
        "A": 4.0,
        "B+": 3.5,
        "B": 3.0,
        "C+": 2.5,
        "C": 2.0,
        "D+": 1.5,
        "D": 1.0,
        "F": 0.0
    }
    total_points = 0
    total_credits = 0
    remain = 0 

    for subject in subjects:
        grade = subject["grade"]
        if grade:
            credit = subject["credit"]
            total_points += (
            grade_points[grade]
            * credit
            )
            total_credits += credit
        else:
            credit = subject["credit"]
            remain += credit

    credit_label.config(text=f" ผ่านแล้วทั้งหมด: {total_credits} / 127 หน่วยกิต")
    remain_label.config(text=f" คงเหลือ: {remain}  หน่วยกิต")
    gpa = total_points / total_credits
    if gpa >= 3.5:
        info_frame.config(bg="#f7edc4")
        credit_label.config(bg="#f7edc4")
        remain_label.config(bg="#f7edc4")
        gpa_label.config(
            text=f" GPA:  {gpa:.2f}",
            bg="#f7edc4"
        )
        honor_label.config(
            text="  ✮ เกียตินิยมอันดับ 1",
            fg="#f3a806",
            bg="#f7edc4"
        )

    elif gpa >= 3.25:
        info_frame.config(bg="#c8f2f5")
        credit_label.config(bg="#c8f2f5")
        remain_label.config(bg="#c8f2f5")
        gpa_label.config(
            text=f" GPA:  {gpa:.2f}",
            bg="#c8f2f5"
        )
        honor_label.config(
            text="  ✮ เกียตินิยมอันดับ 2",
            fg="#17bdd3",
            bg="#c8f2f5"
        )
    elif gpa <= 2.0:
        info_frame.config(bg="#f7c4c4")
        credit_label.config(bg="#f7c4c4")
        remain_label.config(bg="#f7c4c4")
        gpa_label.config(
            text=f" GPA:  {gpa:.2f}",
            bg="#f7c4c4"
        )
        honor_label.config(
            text="  ขอจบไม่ได้ ขยันเพิ่มอีกก",
            fg="#e73a3a",
            bg="#f7c4c4"
        )
    else:
        info_frame.config(bg="silver")
        credit_label.config(bg="silver")
        remain_label.config(bg="silver")
        gpa_label.config(
            text=f" GPA:  {gpa:.2f}",
            bg="silver"
        )
        honor_label.config(
            text=" ",
            fg="#cecfcf",
            bg="silver"
        )

window = tk.Tk()

style = ttk.Style()
print(style.theme_names())
style.theme_use("clam")

style.configure(
    "Passed.Treeview",
    background="#DFEBFA",
    fieldbackground="#E8F5E9"
)

style.configure(
    "Wait.Treeview",
    background="#FDEBE8",
    fieldbackground="#FFF8E1"
)
style.configure(
    "Treeview",
    rowheight=30
)
style.configure(
    "Passed.TLabelframe.Label",
    foreground="#435570",
    font=("Kanit", 11, "bold")
)
style.configure(
    "Waiting.TLabelframe.Label",
    foreground="#d4c9c96f",
    font=("Kanit", 11, "bold")
)

passed_frame = ttk.LabelFrame(
    window,
    text="      วิชาที่ผ่านแล้ว",
    style="Passed.TLabelframe"
)

waiting_frame = ttk.LabelFrame(
    window,
    text="      วิชาที่ยังไม่ผ่าน",
    style="Waiting.TLabelframe"
)
center_frame = tk.Frame(window,padx=20,pady=1)
info_frame = tk.Frame(
    center_frame,
    bg="white",
    bd=3,
    relief="ridge",
    padx=15,
    pady=15
)
control_frame = tk.Frame(
    center_frame,
    bg="#f5ecd0",
    bd=1,
    relief="groove")

info_frame.pack(
    side="left",
    fill="x",
    expand=True,
    padx=10,
    pady=10
)

control_frame.pack(
    side="right",
    expand=True,
    fill="x",
    padx=20
)

window.title("โปรแกรมบันทึกผลการเรียน")
window.geometry("800x800")



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
    control_frame,
    textvariable=grade_var,
    values=["", "A", "B+", "B", "C+", "C", "D+", "D", "F"],
    state="readonly"
)

grade_combo.set("กรุณาคลิกเลือกวิชา")

update_button = tk.Button(
    control_frame,
    text="💾 บันทึกเกรด",
    font=("Kanit", 11, "bold"),
    fg="white",
    width=15,
    background="#f59e1b",
    command=update_grade
)

selected_subject_label = tk.Label(
    control_frame,
    text="ยังไม่ได้เลือกวิชา",
    font=("Kanit", 11),
    bg=control_frame["bg"]
)

passed_height = min(4, max(3, passed_count))
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

#++++++++++++++++++++++++++++++++++++++++++++ Label ++++++++++++++++++++++++++++++++++++++

title_label = tk.Label(
    window,
    text="โปรแกรมบันทึกผลการเรียน",
    font=("Kanit", 20, "bold")
)
title_label.pack(pady=(20,0))
title2_label = tk.Label(
    window,
    text="Comsci Ramkamhaeng University\n" \
    "กฤตยา ตันติชัยยกุล",
    font=("Kanit", 11),
    fg="#6E6D6D"
)
title2_label.pack(pady=(2,2))

gpa_label = tk.Label(
        info_frame,
        text="  GPA: 0.00",
        font=("Kanit", 14),
        bg=info_frame["bg"]
    )
credit_label = tk.Label(
    info_frame,
    text="  หน่วยกิตที่ผ่าน: 0",
    font=("Kanit", 11),
    bg=info_frame["bg"]
)
remain_label = tk.Label(
    info_frame,
    text="  หน่วยกิตคงเหลือ: 127",
    font=("Kanit", 11),
    bg=info_frame["bg"]
)
honor_label = tk.Label(
    info_frame,
    font=("Kanit", 11),
    bg=info_frame["bg"]
)
control_label = tk.Label(
    control_frame,
    text="  จัดการผลการเรียน",
    font=("Kanit", 11, "bold"),
    fg="#473c16",
    bg=control_frame["bg"]
)

table_passed.bind("<<TreeviewSelect>>", on_select)
table_wait.bind("<<TreeviewSelect>>", on_select)

control_label.pack(pady=(10,2))
grade_combo.pack(pady=(10,2))
grade_combo.config(state="disabled") 

passes_label=tk.Label(passed_frame, text="วิชาที่ผ่านแล้ว")
passed_frame.pack(fill="both", expand=True,  padx=20, pady=10)
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
waiting_frame.pack(fill="both", expand=True, padx=20, pady=10)
wait_scroll.pack(
    side="right",
    fill="y"
)
table_wait.pack(
    side="left",
    fill="both",
    expand=True
)

selected_subject_label.pack(pady=2)

update_button.pack(pady=10)

gpa_label.pack(anchor="w")
credit_label.pack(anchor="w")
remain_label.pack(anchor="w")
honor_label.pack(anchor="w")
update_gpa()

window.mainloop()