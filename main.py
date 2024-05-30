import PySimpleGUI as sg

classification_require_credit_dict = {
    "all-subject": 124,
    "base-subject": 24,
    "base": 10,
    "career": 4,
    "foreign-language": 8,
    "wellness": 2,
    "specialized-subject": 84,
    "specialized-fundamental": 6,
    "specialized-education": 48,
    "teacher-training-subject": 0,
    "teacher-training": 0
}

classification_credit_dict = {
    "all-subject": 0,
    "base-subject": 0,
    "base": 0,
    "career": 0,
    "foreign-language": 0,
    "wellness": 0,
    "specialized-subject": 0,
    "specialized-fundamental": 0,
    "specialized-education": 0,
    "teacher-training-subject": 0,
    "teacher-training": 0,
}

classification_grouping_dict = {
    "base-subject": "all-subject",
    "specialized-subject": "all-subject",
    "base": "base-subject",
    "career": "base-subject",
    "foreign-language": "base-subject",
    "wellness": "base-subject",
    "specialized-fundamental": "specialized-subject",
    "specialized-education": "specialized-subject",
    "teacher-training": "teacher-training-subject",
}

ignore_classification = ["teacher-training", "teacher-training-subject"]


class show_display:
    def create_layout(self):
        layout = [
            [sg.Text("履修科目", size=(7, 1)), sg.Text("合計: 0科目", size=(10, 1), key="all-subject_credit_count"),
             sg.Text("", key="all-subject_info")],
            [sg.Text("専門科目", size=(7, 1)), sg.Text("合計: 0科目", size=(10, 1), key="base-subject_credit_count"),
             sg.Text("", key="base-subject_info")],
            [sg.Text("", size=(2, 1)), sg.Text("基礎", size=(9, 1)),
             sg.InputText(key="base", default_text="0", size=(5, 1)),
             sg.Text("入力してください", key="base_info")],
            [sg.Text("", size=(2, 1)), sg.Text("キャリア", size=(9, 1)),
             sg.InputText(key="career", default_text="0", size=(5, 1)),
             sg.Text("入力してください", key="career_info")],
            [sg.Text("", size=(2, 1)), sg.Text("外語", size=(9, 1)),
             sg.InputText(key="foreign-language", default_text="0", size=(5, 1)),
             sg.Text("入力してください", key="foreign-language_info")],
            [sg.Text("", size=(2, 1)), sg.Text("ウェルネス", size=(9, 1)),
             sg.InputText(key="wellness", default_text="0", size=(5, 1)),
             sg.Text("入力してください", key="wellness_info")],
            [sg.Text("専門科目", size=(7, 1)),
             sg.Text("合計: 0科目", size=(10, 1), key="specialized-subject_credit_count"),
             sg.Text("", key="specialized-subject_info")],
            [sg.Text("", size=(2, 1)), sg.Text("専門基礎", size=(9, 1)),
             sg.InputText(key="specialized-fundamental", default_text="0", size=(5, 1)),
             sg.Text("入力してください", key="specialized-fundamental_info")],
            [sg.Text("", size=(2, 1)), sg.Text("専門教育", size=(9, 1)),
             sg.InputText(key="specialized-education", default_text="0", size=(5, 1)),
             sg.Text("入力してください", key="specialized-education_info")],
            [sg.Text("教職科目", size=(7, 1)),
             sg.Text("合計: 0科目", size=(10, 1), key="teacher-training-subject_credit_count"),
             sg.Text("", key="teacher-training-subject_info")],
            [sg.Text("", size=(2, 1)), sg.Text("教職関係", size=(9, 1)),
             sg.InputText(key="teacher-training", default_text="0", size=(5, 1)),
             sg.Text("判定対象外", key="teacher-training_info")],
            [sg.Button("OK")]
        ]
        return layout

    def show(self):
        layout = self.create_layout()
        window = sg.Window("取得単位確認", layout)

        while True:
            event, values = window.read()

            if event == "OK":
                list = classification_credit_dict.keys()
                for key in list:
                    classification_credit_dict[key] = 0

                excepting_flag = False
                for key in list:
                    try:
                        if key.find('subject') > -1:
                            continue
                        classification_credit_dict[key] = int(values[key])
                        classification_credit_dict[classification_grouping_dict.get(key, key)] += int(values[key])
                    except ValueError:
                        window[key + "_info"].update("整数以外で入力しないでください。", text_color="#ff0000")
                        excepting_flag = True

                if excepting_flag:
                    continue

                for key in list:
                    if key.find('subject') > -1 and classification_grouping_dict.keys().__contains__(key):
                        classification_credit_dict[classification_grouping_dict.get(key, key)] += classification_credit_dict[key]

                for key in list:
                    window[key + "_info"].update("")
                    if ignore_classification.__contains__(key):
                        window[key + "_info"].update("判定対象外", text_color="#ffffff")
                    elif classification_credit_dict[key] >= classification_require_credit_dict[key]:
                        window[key + "_info"].update("必要単位数超過",
                                                     text_color="#33cc33")
                    else:
                        window[key + "_info"].update("必要単位数未超過",
                                                     text_color="#ff0000")

                    if key.find("subject") > -1:
                        window[key + "_credit_count"].update("合計: " + str(classification_credit_dict[key]) + "科目")

            if event == sg.WIN_CLOSED:
                break


display = show_display()
display.show()
