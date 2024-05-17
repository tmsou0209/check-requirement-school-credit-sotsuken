import PySimpleGUI as sg


class show_display:
    def create_layout(self):
        layout = [
            [sg.Text("基礎"), sg.InputText(key="base"), sg.Text("入力してください", key="base_info")],
            [sg.Text("キャリア"), sg.InputText(key="career"), sg.Text("入力してください", key="career_info")],
            [sg.Text("外語"), sg.InputText(key="foreign-language"), sg.Text("入力してください", key="foreign-language_info")],
            [sg.Text("ウェルネス"), sg.InputText(key="wellness"), sg.Text("入力してください", key="wellness_info")],
            [sg.Text("専門基礎"), sg.InputText(key="specialized-fundamental"), sg.Text("入力してください", key="specialized-fundamental_info")],
            [sg.Text("専門教育"), sg.InputText(key="specialized-education"), sg.Text("入力してください", key="specialized-education_info")],
            [sg.Text("教職"), sg.InputText(key="teacher-training"), sg.Text("入力してください", key="teacher-training_info")],
            [sg.Button("OK")]
        ]
        return layout

    def show(self):
        layout = self.create_layout()
        window = sg.Window("取得単位確認", layout)

        use_api = False
        while True:
            event, values = window.read()

            if event == "OK":
                base = int(values["base"])
                career = int(values["career"])
                foreign_language = int(values["foreign-language"])
                wellness = int(values["wellness"])
                specialized_fundamental = int(values["specialized-fundamental"])
                specialized_education = int(values["specialized-education"])
                teacher_training = int(values["teacher-training"])

                if base >= 10:
                    window["base_info"].update(text="必要単位数超過", text_color="#33cc33")
                else:
                    window["base_info"].update(text="必要単位数未超過", text_color="#ff0000")



            if event == sg.WIN_CLOSED:
                break



display = show_display()
display.show()