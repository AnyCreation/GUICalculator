import dearpygui.dearpygui as dpg

dpg.create_context()
W, H = 400, 800

Number_One, Number_Two = 0, 0

new_text = []
new_func = ""


func = {
    "+": lambda x, y : x + y,
    "-": lambda: (2),
    "x": lambda: (3),
    "/": lambda: (4),
    "^": lambda:  (5)
}

def Set_Number(sender):
    global new_text, func
    new_text.append(int(sender))
    dpg.set_value(Use_Num, new_text)

def Set_Func(sender): 
    global new_func, Info, new_text
    new_func = f"[{sender}]"
    dpg.set_value(Info, new_func)

    L = new_text
    print(func[sender](L[0], L[1]))
    print(L)

last_item = dpg.last_item()

def Num_Buttons(Start, End, W, H):
    button_width = W / 3 - 40
    button_height = H / 4 - 20

    with dpg.group(horizontal=True, horizontal_spacing=5):
        S1 = dpg.add_button(label=f"{Start}", tag=f"{Start}", callback=Set_Number, width=button_width, height=button_height)
        dpg.bind_item_theme(S1, 4)
        S2 = dpg.add_button(label=f"{Start + 1}", tag=f"{Start + 1}", callback=Set_Number, width=button_width, height=button_height)
        dpg.bind_item_theme(S2, 4)
        S3 = dpg.add_button(label=f"{End}", tag=f"{End}", callback=Set_Number, width=button_width, height=button_height)
        dpg.bind_item_theme(S3, 4)

def Func_Buttons():
    button_width = W / 5 - 40
    button_height = 50

    with dpg.group(horizontal=True, horizontal_spacing=5):
        F1 = dpg.add_button(label="+", tag="+", callback=Set_Func, width=button_width, height=button_height)
        dpg.bind_item_theme(F1, 4)
        F2 = dpg.add_button(label="-", tag="-", callback=Set_Func, width=button_width, height=button_height)
        dpg.bind_item_theme(F2, 4)
        F3 = dpg.add_button(label="x", tag="x", callback=Set_Func, width=button_width, height=button_height)
        dpg.bind_item_theme(F3, 4)
        F4 = dpg.add_button(label="/", tag="/", callback=Set_Func, width=button_width, height=button_height)
        dpg.bind_item_theme(F4, 4)
        F5 = dpg.add_button(label="^", tag="^", callback=Set_Func, width=button_width, height=button_height)
        dpg.bind_item_theme(F5, 4)

def Result_Text():
    global Use_Num, Info
    with dpg.group(horizontal=True, horizontal_spacing=5):
        Info = dpg.add_text("[?]")
        dpg.add_text("|")
        Use_Num = dpg.add_text("[...]")
        dpg.add_text(":")
        Result = dpg.add_text("Result")

with dpg.window(label="Calculator", tag="Win"):
     
     with dpg.theme(tag=4):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)

     Result_Text()
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