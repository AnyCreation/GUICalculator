import dearpygui.dearpygui as dpg

dpg.create_context()
W, H = 400, 800

<<<<<<< HEAD
Number_One, Number_Two = 0, 0
=======
with dpg.window(label="Windows", width=800, height=800):
    dpg.add_text("HELLO") 
    dpg.add_button(label="button")
    dpg.add_input_text(label="TEXT! HERE!")
    dpg.add_button(label="button")
>>>>>>> 6c427d05eb5f3a10cdef4dee1a9a0fea83e30deb

new_text = 0

def Set_Back(sender):
    global new_text
    new_text += int(sender)
    dpg.set_value(Res, new_text)

last_item = dpg.last_item()

def Num_Buttons(Start, End, W, H):
    button_width = W / 3 - 40
    button_height = H / 4 - 20

    with dpg.theme(tag=4):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)


    with dpg.group(horizontal=True, horizontal_spacing=5):
        S1 = dpg.add_button(label=f"{Start}", tag=f"{Start}", callback=Set_Back, width=button_width, height=button_height)
        dpg.bind_item_theme(S1, 4)
        S2 = dpg.add_button(label=f"{Start + 1}", tag=f"{Start + 1}", callback=Set_Back, width=button_width, height=button_height)
        dpg.bind_item_theme(S2, 4)
        S3 = dpg.add_button(label=f"{End}", tag=f"{End}", callback=Set_Back, width=button_width, height=button_height)
        dpg.bind_item_theme(S3, 4)

def Set_button(Start, End, W, H):
    button_width = W / 3 - 40
    button_height = H / 4 - 20

    with dpg.theme(tag=4):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)


    with dpg.group(horizontal=True, horizontal_spacing=5):
        S1 = dpg.add_button(label=f"{Start}", tag=f"{Start}", callback=Set_Back, width=button_width, height=button_height)
        dpg.bind_item_theme(S1, 4)
        S2 = dpg.add_button(label=f"{Start + 1}", tag=f"{Start + 1}", callback=Set_Back, width=button_width, height=button_height)
        dpg.bind_item_theme(S2, 4)
        S3 = dpg.add_button(label=f"{End}", tag=f"{End}", callback=Set_Back, width=button_width, height=button_height)
        dpg.bind_item_theme(S3, 4)

with dpg.window(label="Calculator", tag="Win"):
     Res = dpg.add_text("[...]")
     Set_button(1, 3, W, H)
     Set_button(4, 6, W, H)
     Set_button(7, 9, W, H)

dpg.create_viewport(title='Calculator', width=W + 20, height=H)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Win", True)
dpg.start_dearpygui()
dpg.destroy_context()