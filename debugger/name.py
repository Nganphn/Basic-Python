def name_count():
    
    name_list = []

    while True:
        name = input("Enter student name: ").strip()
        if not name:
            break
        name_list.append(name)
    
    counts = len(name_list)
    print("Student count: ", counts)

    print(",  ".join(name_list))

name_count()