def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "Empty Input"
    return f"Redult {f_name.title()} {l_name.title()}"

print(format_name(input("Enter the first Name:-"),input("Enter the Last name")))