import os

working_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(working_dir)

def get_chapter_list(selected_subject):
    subject_name = selected_subject.lower()

    chapters_dir = f"{parent_dir}/data/class_12/{subject_name}"

    if not os.path.exists(chapters_dir):
        return []

    chapters_list = [
        x[:-4] for x in os.listdir(chapters_dir)
        if x.endswith(".pdf")
    ]

    chapters_list.sort(key=lambda x: int(x.split(".")[0]))
    return chapters_list
