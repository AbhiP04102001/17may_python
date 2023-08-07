def read_text_file(task):
    try:
        with open(task, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An error occurred while reading the file.")


file_path ='task.py'  
read_text_file(file_path)
