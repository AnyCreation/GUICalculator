import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Windows", width=800, height=800):
    dpg.add_text("HELLO")
    dpg.add_button(label="button")
    dpg.add_input_text(label="TEXT! HERE!")
    dpg.add_button(label="button")

dpg.create_viewport(title='Zagalovor okna', width=800, height=800)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()