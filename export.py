import os


for directory in next(os.walk("."))[1]:
    os.chdir(directory)
    file_names = []
    for path, subdirs, files in os.walk("."):
        for name in files:
            if ".org" in name:
                file_names.append(os.path.join(path, name))
    file_names = "\"" +  "\" \"".join(file_names) + "\""
    os.system(f"""pandoc -s {file_names} -o README.docx""")
    os.chdir("..")

print("Единые конспекты/отчёты созданы")
