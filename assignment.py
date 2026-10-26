# You can remove 'pass' if you written code in the function
# Exercise 1
def save_scores(names, scores, filename):
    file=open(filename, "w")
    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
    file.close()
    
# Exercise 2
def average_score(filename):
    file=open(filename, "r")
    lines=file.readlines()
    file.close()
    total=0
    count=0
    for line in lines:
        cleaned_line=line.strip()
        if cleaned_line:
            parts=cleaned_line.split(",")
            total+=int(parts[1])
            count+=1
    if count==0:
        return 0
    return round(total / count, 1)

# Exercise 3
def filter_passed(source, destination, pass_mark):
    file_in=open(source, "r")
    lines=file_in.readlines()
    file_in.close()
    passed_count=0
    file_out=open(destination, "w")
    for line in lines:
        cleaned_line=line.strip()
        if cleaned_line:
            parts=cleaned_line.split(",")
            if int(parts[1])>=pass_mark:
                file_out.write(cleaned_line + "\n")
                passed_count+=1
    file_out.close()
    return passed_count

# Exercise 4
def replace_word(filename, old_word, new_word):
    file=open(filename, "r")
    content=file.read()
    file.close()
    count=content.count(old_word)
    new_content=content.replace(old_word, new_word)
    file=open(filename, "w")
    file.write(new_content)
    file.close()
    return count

# Exercise 5
def remove_line(filename, line_number):
    file=open(filename, "r")
        lines=file.readlines()
        file.close()
    
        if line_number<1 or line_number>len(lines):
            return False
    
        del lines[line_number - 1]
    
        file=open(filename, "w")
        for line in lines:
            file.write(line)
        file.close()
    
        return True
