import tkinter as tk
from tkinter import ttk
import json

#++++++++++++++++++++++++++++++++++++++++++++++ splash +++++++++++++++++++++++++++++++++++++++++++++

splash = tk.Tk()

splash.overrideredirect(True)      # ไม่มีขอบหน้าต่าง
splash.geometry("450x250")

label1 = tk.Label(
    splash,
    text="GPA TRACKER",
    bg="#FFF8F0",
    fg="#435570",
    font=("Kanit",26,"bold")
)
label2 = tk.Label(
    splash,
    text=" Student Grade Manager\nVersion1.0",
    bg="#FFF8F0",
    fg="#435570",
    font=("Kanit",14)
)
label3 = tk.Label(
    splash,
    text="Developer\nกฤตยา ตันติชัยยกุล",
    bg="#FFF8F0",
    fg="#435570",
    font=("Kanit",14)
)
label4 = tk.Label(
    splash,
    text="Ramkamhaeng University\n\nLoading...",
    bg="#FFF8F0",
    fg="#435570",
    font=("Kanit",14)
)
progress = ttk.Progressbar(
    splash,
    mode="indeterminate",
    length=350
)

progress.start(10)
splash.configure(bg="#FFF8F0")
width = 600
height = 400

x = (splash.winfo_screenwidth() // 2) - (width // 2)
y = (splash.winfo_screenheight() // 2) - (height // 2)

splash.geometry(f"{width}x{height}+{x}+{y}")

label1.pack(expand=True)
label2.pack(expand=True)
label3.pack(expand=True)
label4.pack(expand=True)
progress.pack(pady=(5,10))

#+++++++++++++++++++++++++++++++++++++++++++ Function ++++++++++++++++++++++++++++++++++++++++++++++

def show_guide():

    guide = tk.Toplevel(window)
    guide.title("คู่มือการใช้งาน")
    guide.geometry("700x550")

    # ---------- Canvas ----------
    canvas = tk.Canvas(guide, highlightthickness=0)

    scrollbar = ttk.Scrollbar(
        guide,
        orient="vertical",
        command=canvas.yview
    )

    scroll_frame = tk.Frame(canvas)

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window(
        (0, 0),
        window=scroll_frame,
        anchor="nw"
    )

    canvas.configure(
        yscrollcommand=scrollbar.set
    )

    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    # ---------- หัวข้อ ----------
    tk.Label(
        scroll_frame,
        text=" คู่มือการใช้งาน\n",
        font=("Kanit",18,"bold"),
        fg="#435570"
    ).pack(
        anchor="w",
        padx=20,
        pady=(20,10)
    )

    # ---------- วิธีใช้งาน ----------
    tk.Label(
        scroll_frame,
        text=" วิธีใช้งาน",
        font=("Kanit",14,"bold")
    ).pack(anchor="w", padx=20)

    tk.Label(
        scroll_frame,
        justify="left",
        anchor="w",
        font=("Kanit",11),
        text=
"""1. เลือกวิชาจากตาราง 'วิชาที่ยังไม่ผ่าน'
2. เลือกเกรดจากรายการ
3. กดปุ่ม 💾 บันทึกเกรด
4. โปรแกรมจะ
• คำนวณ GPA ใหม่
• อัปเดตจำนวนหน่วยกิต
• ย้ายวิชาไปยังตารางที่ผ่านแล้ว
"""
    ).pack(
        anchor="w",
        padx=35,
        pady=(5,20)
    )

    ttk.Separator(scroll_frame).pack(fill="x", padx=20)

    # ---------- ความหมายของสี ----------
    tk.Label(
        scroll_frame,
        text=" ความหมายของสี",
        font=("Kanit",14,"bold")
    ).pack(anchor="w", padx=20, pady=(15,0))

    tk.Label(
        scroll_frame,
        justify="left",
        anchor="w",
        font=("Kanit",11),
        text=
""" สีทอง      GPA ≥ 3.50 (เกียตินิยมอันดับ 1)
 สีฟ้า        GPA ≥ 3.25 (เกียตินิยมอันดับ 2)
 สีเทา       GPA ปกติ
 สีแดง      GPA ≤ 2.00 (ควรปรับปรุงผลการเรียน)
 สีเขียว    ยังไม่มีการบันทึกเกรด
"""
    ).pack(anchor="w", padx=35, pady=(5,20))

    ttk.Separator(scroll_frame).pack(fill="x", padx=20)

    # ---------- หมายเหตุ ----------
    tk.Label(
        scroll_frame,
        text=" หมายเหตุ",
        font=("Kanit",14,"bold")
    ).pack(anchor="w", padx=20, pady=(15,0))

    tk.Label(
        scroll_frame,
        justify="left",
        anchor="w",
        font=("Kanit",11),
        text=
"""
• ฟีเจอร์เกียตินิยมจะคำนวณจากเกรดเบื้องต้นเท่านั้น อย่างไรแล้วท่านอาจต้อง
  ศึกษาเงื่อนไขกับทางมหาวิทยาลัยเพิ่มเติม เช่น การรีเกรด การเทียบโอน เป็นต้น
• เวอร์ชั่นนี้ยังไม่ได้รอบรับการคำนวณเกรดของกลุ่มที่เทียบโอน หากท่านตรวจสอบแล้ว
  ถ้ามีการคำนวณเกรดของกลุ่มวิชาทั่วไปด้วย ท่านสามารถใส่เกรด C+ ในกลุ่มวิชาเสรีและ
  RAM ได้เลย แต่ถ้าไม่มีการคำนวณ ท่านก็เว้นไว้ ปล่อยให้อยู่ตารางข้างล่างได้เลย
"""
    ).pack(anchor="w", padx=35, pady=(5,20))

def show_about():

    about = tk.Toplevel(window)
    about.title("About")
    about.geometry("500x430")
    about.resizable(False, False)

    frame = tk.Frame(
        about,
        padx=25,
        pady=20
    )
    frame.pack(fill="both", expand=True)

    # ===== Title =====
    tk.Label(
        frame,
        text="🎓 GPA Tracker",
        font=("Kanit", 20, "bold"),
        fg="#435570"
    ).pack()

    tk.Label(
        frame,
        text="Student Grade Management System",
        font=("Kanit", 11),
        fg="gray"
    ).pack(pady=(0, 15))

    ttk.Separator(frame).pack(fill="x", pady=10)

    # ===== Developer =====
    tk.Label(
        frame,
        text="Developer",
        font=("Kanit", 13, "bold"),
        anchor="w"
    ).pack(fill="x")

    tk.Label(
        frame,
        text="กฤตยา ตันติชัยยกุล",
        font=("Kanit", 11),
        anchor="w",
        justify="left"
    ).pack(fill="x")

    tk.Label(
        frame,
        text="Bachelor of Science (Computer Science)\nRamkhamhaeng University",
        font=("Kanit", 11),
        fg="gray",
        justify="left",
        anchor="w"
    ).pack(fill="x", pady=(0, 10))

    ttk.Separator(frame).pack(fill="x", pady=10)

    # ===== Contact =====
    tk.Label(
        frame,
        text="Contact",
        font=("Kanit", 13, "bold"),
        anchor="w"
    ).pack(fill="x")

    tk.Label(
        frame,
        text="📧 Email\n   golfring.dove@gmail.com",
        font=("Kanit", 11),
        justify="left",
        anchor="w"
    ).pack(fill="x", pady=(5, 5))

    tk.Label(
        frame,
        text="💬 LINE\n   golfalohaha",
        font=("Kanit", 11),
        justify="left",
        anchor="w"
    ).pack(fill="x")

    ttk.Separator(frame).pack(fill="x", pady=15)

    # ===== Footer =====
    tk.Label(
        frame,
        text="Version 1.0",
        font=("Kanit", 10),
        fg="gray"
    ).pack()

    tk.Label(
        frame,
        text="© 2026 GPA Tracker\nAll Rights Reserved.",
        font=("Kanit", 10),
        fg="gray"
    ).pack(pady=(5, 0))

def start():
    progress.stop()
    splash.destroy()

splash.after(3000, start)

splash.mainloop()
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
    selected_name = values[1]
    
    print(selected_code)

    for subject in subjects:
        if (
        subject["code"] == selected_code
        and
        subject["name"] == selected_name
        ):
            subject["grade"] = grade_var.get()
            break
    else:
        print("ไม่เจอวิชา", selected_code)
    
    print("กำลังบันทึกเกรด")

    with open("data/course.json", "w", encoding="utf-8") as file:
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

    if total_credits == 0:
        gpa = 0
        gpa_label.config(
            bg="#dbf5e2"
        )
        info_frame.config(bg="#dbf5e2")
        credit_label.config(bg="#dbf5e2")
        remain_label.config(bg="#dbf5e2")
        honor_label.config(
            text=" เริ่มอัพเดทเกรดจากตารางด้านล่างได้เลย",
            fg="#2e3030",
            bg="#dbf5e2"
        )
        return
    else:
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
            text=" ขอจบไม่ได้ ขยันเพิ่มอีกกก!",
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

#+++++++++++++++++++++++++++++++++++++++++++ id +++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++ Style ++++++++++++++++++++++++++++++++++++++++++++

window = tk.Tk()

style = ttk.Style()
print(style.theme_names())
style.theme_use("clam")

style.configure(
    "Passed.Treeview",
    background="#E3FAE5",
    relief="flat",
    foreground="#0D0E0D"
)

style.configure(
    "Wait.Treeview",
    background="#FDEEEE",
    foreground="#0E0B0B"
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
    foreground="#494545",
    font=("Kanit", 11, "bold")
)

#++++++++++++++++++++++++++++++++++++++++++++++++ Frame ++++++++++++++++++++++++++++++++++++++++++

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
    bg="#EFEFEF",
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

#+++++++++++++++++++++++++++++++++++++++++++++++++ Table +++++++++++++++++++++++++++++++++++

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

with open("data/course.json", "r", encoding="utf-8") as file:
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
    background="#E9A825",
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
    font=("Kanit", 20, "bold"),
    fg="#435570"
)
title_label.pack(pady=(20,0))
title2_label = tk.Label(
    window,
    text="Comsci Ramkhamhaeng GPA Tracker",
    font=("Kanit", 14),
    fg="#919191"
)
title2_label.pack(pady=(0,5))

top_menu = tk.Frame(
    window,
    bg=window.cget("bg")     # ใช้สีพื้นเดียวกับโปรแกรม
)
top_menu.pack(pady=(0, 2))
#+++++++++++++++++++++++++++++++++++++++++++++ Menu bar ++++++++++++++++++++++++++++++++++++++++++

guide_btn = tk.Button(
    top_menu,
    text="🛈 คำแนะนำการใช้งาน",
    relief="flat",
    bg=window.cget("bg"),
    activebackground="#E8E8E8",
    cursor="hand2",
    command=show_guide
)

guide_btn.pack(side="left", padx=(15,5), pady=1)

about_btn = tk.Button(
    top_menu,
    text="ⓘ About",
    relief="flat",
    bg=window.cget("bg"),
    activebackground="#E8E8E8",
    cursor="hand2",
    command=show_about
)

about_btn.pack(side="left", padx=5, pady=1)

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