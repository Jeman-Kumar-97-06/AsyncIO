myvar = {"name":"Jane", "age":30}

txt = "Happy {age}th birthday {name}"

print(txt.format_map(myvar))