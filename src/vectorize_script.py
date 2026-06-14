from vectorize_book import vectorize_book_and_store_to_db, vectorize_chapters

subjects = [
    "class_12/biology",
    "class_12/chemistry",
    "class_12/physics"
]

for subject in subjects:
    vector_db_name = subject.replace("/", "_") + "_vector_db"
    vectorize_book_and_store_to_db(subject, vector_db_name)
    vectorize_chapters(subject)
