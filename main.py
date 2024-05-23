import dearpygui.dearpygui as dpg

dpg.create_context()
W, H = 400, 800

Number_One, Number_Two = 0, 0


last_item = dpg.last_item()


new_text = []
new_func = ""

def StrOrInt(Num, M):
    try:
        Num.append(int(M))
    except ValueError:
        Num.append(str(M))

    return Num

def Func_Push(Num, Func):
    M = 0
    if Func == "+":
        for i in Num:
            M += i
    elif Func == "-":
        M = Num[0]
        for i in range(1, len(Num)):
            M -= Num[i]
    elif Func == "x":
        M = 1
        for i in Num:
            M *= i
    elif Func == "/":
        M = Num[0]
        for i in range(1, len(Num)):
            M /= Num[i]
    elif Func == "^":
        M = Num[0]
        for i in range(1, len(Num)):
            M = M ** Num[i]

    return M
func = {
    "[+]": lambda Num : Func_Push(Num, "+"),
    "[-]": lambda Num : Func_Push(Num, "-"),
    "[x]": lambda Num : Func_Push(Num, "x"),
    "[/]": lambda Num : Func_Push(Num, "/"),
    "[^]": lambda Num : Func_Push(Num, "^")
}

def Set_Rules(sender): # Replace Append Rules (Number (int) Or Function (str)) and "[...]"
    global new_text, Fezmat
    if new_text == "[...]":
        new_text = []
        Fezmat = StrOrInt(new_text, sender)
    else:
        Fezmat = StrOrInt(new_text, sender)
    dpg.set_value(Use_Num, Fezmat)

def Delete_Number(sender):
    global new_text, Use_Num
    new_text = "[...]"
    dpg.set_value(Use_Num, new_text)

def Get_Result(sender): # Need To Checking The Rules (new_text) And Give Result
    global Fezmat, new_func, Result
    for Check in Fezmat: print(Check)

def Num_Buttons(Start, End, W, H): # Number Button (1 - 9)
    button_width = W / 3 - 40
    button_height = H / 4 - 20

    with dpg.group(horizontal=True, horizontal_spacing=5):
        S1 = dpg.add_button(label=f"{Start}", tag=f"{Start}", callback=Set_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(S1, 4)
        S2 = dpg.add_button(label=f"{Start + 1}", tag=f"{Start + 1}", callback=Set_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(S2, 4)
        S3 = dpg.add_button(label=f"{End}", tag=f"{End}", callback=Set_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(S3, 4)

def Func_Buttons(): # Function Button (+, -, *, /, ^, DELETE and RESULT)
    button_width = W / 5 - 40
    button_height = 50

    with dpg.group(horizontal=True, horizontal_spacing=5): # Button: +, -, *, /, ^ and Delete
        F1 = dpg.add_button(label="+", tag="+", callback=Set_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(F1, 4)
        F2 = dpg.add_button(label="-", tag="-", callback=Set_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(F2, 4)
        F3 = dpg.add_button(label="x", tag="x", callback=Set_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(F3, 4)
        F4 = dpg.add_button(label="/", tag="/", callback=Set_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(F4, 4)
        F5 = dpg.add_button(label="^", tag="^", callback=Set_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(F5, 4)

        DEL = dpg.add_button(label="DELETE", tag="DELETE", callback=Delete_Number, width=button_width * 2 - 10, height=button_height)

        dpg.add_text("Choose Actions")
        dpg.bind_item_theme(DEL, 4)

    RES = dpg.add_button(label="RESULT", tag="RESULT", callback=Get_Result, width=button_width * 2 - 10, height=button_height)
    dpg.bind_item_theme(DEL, 4)

def Result_Text(): # Text: {Rules} = {Result}
    global Use_Num, Info, Result
    with dpg.group(horizontal=True, horizontal_spacing=5):
        Use_Num = dpg.add_text("[...]")
        dpg.add_text("=")
        Result = dpg.add_text("Result")

with dpg.window(label="Calculator", tag="Win"):
     
     with dpg.theme(tag=4):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)

     Result_Text()
     T = "-" * (W // 5)
     dpg.add_text(T)
     Num_Buttons(1, 3, W, H)
     Num_Buttons(4, 6, W, H)
     Num_Buttons(7, 9, W, H)

     Func_Buttons()

dpg.create_viewport(title='Calculator', width=W + 20, height=H)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Win", True)
dpg.start_dearpygui()
dpg.destroy_context()