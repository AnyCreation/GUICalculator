import dearpygui.dearpygui as dpg

dpg.create_context()
W, H = 400, 800

Number_One, Number_Two = 0, 0


last_item = dpg.last_item()


new_text = []
new_func = ""

def StrOrInt(Num, M): # Namber --> int \ Rules --> str
    try:
        Num.append(int(M))
    except ValueError:
        Num.append(str(M))

    return Num

def Func_Push(Num, Func): # Func-Rules
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
func = { # Rules
    "[+]": lambda Num : Func_Push(Num, "+"),
    "[-]": lambda Num : Func_Push(Num, "-"),
    "[x]": lambda Num : Func_Push(Num, "x"),
    "[/]": lambda Num : Func_Push(Num, "/"),
    "[^]": lambda Num : Func_Push(Num, "^")
}

def After_The_Decimal_Point(K1, K2):
    return str(K1) + str(K2)

def Set_Rules(sender): # Replace Append "Rules" (Number (int) Or Function (str)) And "[...]" /// Rule For Func Read In "F_count[rus/eng].txt"
    global new_text
    if new_text == "[...]":
        new_text = []
        new_text = StrOrInt(new_text, sender)
    else:
        new_text = StrOrInt(new_text, sender)

    for Check in range(0, len(new_text) - 1): # Checks The Rules According To The "F_count[rus/eng].txt"
        if type(new_text[Check]) in [int, float] and type(new_text[Check + 1]) in [int, float]: #Check Numbers Using Rules 1, 2, 3
            K1, K2 = new_text[Check], new_text[Check + 1]
            if K1 >= 1:
                COS = K1 * 10 + K2
                new_text.append(COS)
            elif K1 > 0:
                COS = float(After_The_Decimal_Point(K1, K2))
                new_text.append(COS)   
            else:
                COS = K2 / 10
                new_text.append(COS)
                
            if COS in new_text:
                new_text.remove(K1)
                new_text.remove(K2)

        if type(new_text[Check]) == str and type(new_text[Check + 1]) == str: #Check Str Using Rules 5
            K1 = new_text[Check]
            new_text.remove(K1)
            
    dpg.set_value(Use_Num, new_text)

def Delete_Number(sender): # For Button. Delete "Rules" And Set "[...]"
    global new_text, Use_Num
    new_text = "[...]"
    dpg.set_value(Use_Num, new_text)

def Get_Result(sender): # Need To Checking The "Rules" (new_text) And Give Result
    global new_text, new_func, Result
    pass
        


""" (| ------ ↓↓ Button Func (+, -, *, /, ^, DELETE and RESULT) And Number (1 - 9) ↓↓ --------------------------|) |X| """
def Num_Buttons(Start, End, W, H): # Button (1 - 9 and 0)
    button_width = W / 3 - 40
    button_height = H / 4 - 20

    with dpg.group(horizontal=True, horizontal_spacing=5): # Button 1 - 9
        S1 = dpg.add_button(label=f"{Start}", tag=f"{Start}", callback=Set_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(S1, 4)
        S2 = dpg.add_button(label=f"{Start + 1}", tag=f"{Start + 1}", callback=Set_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(S2, 4)
        S3 = dpg.add_button(label=f"{End}", tag=f"{End}", callback=Set_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(S3, 4)

        if End == 9:
            ZERO = dpg.add_button(label="0", tag=f"0", callback=Set_Rules, width=button_width, height=button_height)
            dpg.bind_item_theme(ZERO, 4)

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
        dpg.bind_item_theme(DEL, 4)

        dpg.add_text("|Choose |Actions", wrap=0, color=(81, 204, 242))

    RES = dpg.add_button(label="RESULT", tag="RESULT", callback=Get_Result, width=button_width * 2 - 10, height=button_height)
    dpg.bind_item_theme(RES, 4)
""" (| ------ ↑↑ Button Func (+, -, *, /, ^, DELETE and RESULT) And Number (1 - 9) ↑↑ --------------------------|) |X|"""



def Result_Text(): # Text: {"Rules"} = {Result}
    global Use_Num, Info, Result
    with dpg.group(horizontal=True, horizontal_spacing=5):
        Use_Num = dpg.add_text("[...]")
        dpg.add_text("=")
        Result = dpg.add_text("Result")

with dpg.window(label="Calculator", tag="Win"): # Window
     with dpg.theme(tag=4): # Costum For Button
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)
    
     Result_Text()
     
     """T = "-" * (W // 5)
     dpg.add_text(T)"""

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