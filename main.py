import dearpygui.dearpygui as dpg
import time

dpg.create_context()
W, H = 600, 800

Number_One, Number_Two = 0, 0


last_item = dpg.last_item()

new_text = []
new_func = ""

S = ""

dpg.set_global_font_scale(1)

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ | |

""" (| ------ ↓↓ Sets Body Text: [Enter The Equation] = Result ↓↓ --------------------------|) |X| """
def Sets_Result_Text(): # Text: {"Rules"} = {Result}
    global Use_Num, Result

    with dpg.font_registry():
        default_font = dpg.add_font("C:/Windows/Fonts/Arial.ttf", (W * 0.03))  # Обычный размер шрифта

    with dpg.group(horizontal=True, horizontal_spacing=5):
        Use_Num = dpg.add_text("[Enter The Equation]")
        Qua = dpg.add_text("=")
        Result = dpg.add_text("Result")

    dpg.bind_item_font(Use_Num, default_font)
    dpg.bind_item_font(Qua, default_font)
    dpg.bind_item_font(Result, default_font)
""" (| ------ ↑↑ Sets Body Text: [Enter The Equation] = Result ↑↑ --------------------------|) |X| """

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ | |

""" (| ------ ↓↓ mathematical symbols - Fucn ↓↓ --------------------------|) |X| """
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
func = { # Rules-Lambda
    "[+]": lambda Num : Func_Push(Num, "+"),
    "[-]": lambda Num : Func_Push(Num, "-"),
    "[x]": lambda Num : Func_Push(Num, "x"),
    "[/]": lambda Num : Func_Push(Num, "/"),
    "[^]": lambda Num : Func_Push(Num, "^")
}
""" (| ------ ↑↑ mathematical symbols - Fucn ↑↑ --------------------------|) |X| """

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ | |

""" (| ------ ↓↓ Sets Up The User's Qquation And Processes It To Combine And Produce A Result ↓↓ --------------------------|) |X| """
def After_The_Decimal_Point(K1, K2): # To Avoid Errors When Dividing
    return str(K1) + str(K2)
def DivisionZero(): # If The User Tries To Divide By Zero
    global ZERO

    ByZero = dpg.add_text("Division by zero is prohibited! May Ee[enter The Equation]", parent="Win", 
                 pos=[dpg.get_item_pos(ZERO)[0] + dpg.get_item_width(ZERO) + 10, 
                      dpg.get_item_pos(ZERO)[1] + (dpg.get_item_height(ZERO) / 2) - 10],
                      color=[200, 0, 0])
    time.sleep(0.85)
    dpg.delete_item(ByZero)
    Delete_Rules()
def StrOrInt(Num, M): # Namber -{become}-> int (Example: '9' --> 9) | Rules -{Stays}-> str (Example: '/' --> '/')
    try:
        Num.append(int(M))
    except ValueError:
        Num.append(str(M))

    return Num

def BecomeListToStr(Num):
    S = ""
    for Ch in Num:
        S += str(Ch) + " "

    return S

def Sets_Rules(sender): # Replace "[Enter The Equation]" and [Number (int) Or Function (str)] /// Rule For Func Read In "F_count[rus/eng].txt"
    global new_text

    if new_text == "[Enter The Equation]":
        new_text = []
        new_text = StrOrInt(new_text, sender)
    else:
        new_text = StrOrInt(new_text, sender)

    for Check in range(0, len(new_text) - 1): # Checks The Rules According To The "F_count[rus/eng].txt"
        if type(new_text[Check]) in [int, float] and type(new_text[Check + 1]) in [int, float]: #Check Numbers Using Rules 1, 2, 3
            K1, K2 = new_text[Check], new_text[Check + 1]
            if K1 >= 1: # K = 1 <---> Infinity 
                COS = K1 * 10 + K2
                new_text.append(COS)
            elif K1 > 0: # K =  0 <---> 0.5 <---> 1
                COS = float(After_The_Decimal_Point(K1, K2))
                new_text.append(COS)   
            else: # K = 0 
                COS = K2 / 10
                new_text.append(COS)
                
            if COS in new_text:
                new_text.remove(K1)
                new_text.remove(K2)

        if type(new_text[Check]) == str and type(new_text[Check + 1]) == str: #Check Str Using Rules 5
            K1 = new_text[Check]
            new_text.remove(K1)

        try: 
            if new_text[Check] == "/" and new_text[Check + 1] == 0: #Check If user writing "/" and 0 Using Rules 6
                K1 = new_text[Check + 1]
                new_text.pop()
                DivisionZero()
        except IndexError:
            continue

    S = BecomeListToStr(new_text)
    dpg.set_value(Use_Num, S)
""" (| ------ ↑↑ Sets Up The User's Qquation And Processes It To Combine And Produce A Result ↑↑ --------------------------|) |X| """

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ | |

""" (| ------ ↓↓ Func For DELETE ↓↓ --------------------------|) |X| """
def Delete_Rules(): # For Button. Delete All "Rules" And Sets "[Enter The Equation]"
    global new_text, Use_Num
    new_text = "[Enter The Equation]"
    dpg.set_value(Use_Num, new_text)
def Delete_Last_El_Rules(): # For Button. Delete Last Elemant In "Rules"
    global new_text, Use_Num, S
    S = ""
    if (len(new_text) -1 == 0) or (len(new_text) == 0) or (new_text == "[Enter The Equation]"): # if "Rules" Not Have Elemants
        Delete_Rules()
    else:
        new_text.pop()

    S = BecomeListToStr(new_text)
    dpg.set_value(Use_Num, S)
""" (| ------ ↑↑ Func For DELETE ↑↑ --------------------------|) |X| """

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ | | 

""" (| ------ ↓↓ Func - Give The Result ↓↓ --------------------------|) |X| """
def Get_Result(): # Checking The "Rules" (new_text) And Give Result
    global new_text, new_func, Result, S1, S2

    for R in range(0, len(new_text) - 2):
        if (type(new_text[R]) in [int, float]) and (type(new_text[R + 1]) == str) and (type(new_text[R + 2]) in [int, float]): 
            S1, S2 = new_text[R], new_text[R + 2]
            F = new_text[R + 1]
        
            dpg.set_value(Result, Func_Push([S1, S2], F))
""" (| ------ ↑↑ Give The Result ↑↑ --------------------------|) |X| """


""" (| ------ ↓↓ Button Func (+, -, *, /, ^, DELETE and RESULT) And Number (1 - 9) ↓↓ --------------------------|) |X| """
def Num_Buttons(Start, End, W, H): # Button (1 - 9 and 0)
    global ZERO
    button_width = W / 5 - 40
    button_height = H / 8 - 20

    with dpg.group(horizontal=True, horizontal_spacing=5): # Button 1 - 9
        S1 = dpg.add_button(label=f"{Start}", tag=f"{Start}", callback=Sets_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(S1, 4)
        S2 = dpg.add_button(label=f"{Start + 1}", tag=f"{Start + 1}", callback=Sets_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(S2, 4)
        S3 = dpg.add_button(label=f"{End}", tag=f"{End}", callback=Sets_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(S3, 4)

    if End == 9:
        ZERO = dpg.add_button(label="0", tag=f"0", callback=Sets_Rules, width=button_width, height=button_width)
        dpg.bind_item_theme(ZERO, 4)
def Func_Buttons(): # Function Button (+, -, *, /, ^, DELETE and RESULT)
    button_width = W / 7 - 40
    button_height = H / 8 - 20

    dpg.add_text("|---------------- Choose Actions ----------------------------|", wrap=0, color=(81, 204, 242))
    with dpg.group(horizontal=True, horizontal_spacing=5): # Button: +, -, *, /, ^ and Delete

        with dpg.group(horizontal=False, horizontal_spacing=10):
            dpg.add_text("|", wrap=0, color=(81, 204, 242))
            dpg.add_text("|", wrap=0, color=(81, 204, 242))
            
        F1 = dpg.add_button(label="+", tag="+", callback=Sets_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(F1, 4)
        F2 = dpg.add_button(label="-", tag="-", callback=Sets_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(F2, 4)
        F3 = dpg.add_button(label="x", tag="x", callback=Sets_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(F3, 4)
        F4 = dpg.add_button(label="/", tag="/", callback=Sets_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(F4, 4)
        F5 = dpg.add_button(label="^", tag="^", callback=Sets_Rules, width=button_width, height=button_height)
        dpg.bind_item_theme(F5, 4)

        DEL = dpg.add_button(label="DELETE", tag="DELETE", callback=Delete_Rules, width=button_width * 2 - 10, height=button_height)
        dpg.bind_item_theme(DEL, 4)
        ERA = dpg.add_button(label="ERASE", tag="ERASE", callback=Delete_Last_El_Rules, width=button_width * 2 - 10, height=button_height)
        dpg.bind_item_theme(ERA, 4)       
    dpg.add_text("|----------------|------|-------|----------------------------|", wrap=0, color=(81, 204, 242))

    RES = dpg.add_button(label="RESULT", tag="RESULT", callback=Get_Result, width=button_width * 2 - 10, height=button_height)
    dpg.bind_item_theme(RES, 4)
""" (| ------ ↑↑ Button Func (+, -, *, /, ^, DELETE and RESULT) And Number (1 - 9) ↑↑ --------------------------|) |X| """

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ | |


with dpg.window(label="Calculator", tag="Win"): # Window
     with dpg.theme(tag=4): # Costum For Button
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)
    
     Sets_Result_Text() # Sets And Changes Qquation And Result
     
     T = "-" * (W // 5)
     dpg.add_text(T) # Sets "---" between Text And Button

     Num_Buttons(1, 3, W, H) # Sets Num Button 1 - 3
     Num_Buttons(4, 6, W, H) # Sets Num Button 4 - 6
     Num_Buttons(7, 9, W, H) # Sets Num Button 7 - 9
     
     Func_Buttons() # Sets Func Button - (+, -, /, *, ^)


dpg.create_viewport(title='Calculator', width=W, height=H)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Win", True)
dpg.start_dearpygui()
dpg.destroy_context()