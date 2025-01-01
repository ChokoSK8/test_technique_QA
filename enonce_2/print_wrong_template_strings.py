import sys
import os
import re

PATTERN = r"`(.*?)`"

def get_template_strings(file):
    template_strings_of_file = []
    file_content = file.read()
    matches = re.finditer(PATTERN, file_content, re.DOTALL)
    for match in matches:
        template_strings_of_file.append(match.group(1))
    return template_strings_of_file

def get_wrong_template_strings(template_strings):
    wrong_template_strings = {}
    for file in template_strings.keys():
        wrong_template_strings_of_file = []
        for template_string in template_strings[file]:
            if re.search(r'\n', template_string) is None and re.search(r'\$\{(\w+)\}', template_string) is None:
               wrong_template_strings_of_file.append(template_string) 
        if len(wrong_template_strings_of_file):
            wrong_template_strings[file] = wrong_template_strings_of_file
    return wrong_template_strings

def get_number_of_newline(string):
    matches = re.findall(r'\n', string)
    return len(matches)

def print_wrong_template_strings(wrong_template_strings):
    for js_file in wrong_template_strings.keys():
        number_of_wrong_template_strings = len(wrong_template_strings[js_file])
        print(f"\n\33[34mYou have {number_of_wrong_template_strings} wrong template strings in {js_file}")
        with open(js_file, 'r') as file:
            file_content = file.read()
            for wrong_template_string in wrong_template_strings[js_file]:
                match = re.search(wrong_template_string, file_content)
                match_indexes = match.span()
                line_number = get_number_of_newline(file_content[:match_indexes[0]])
                print(f"\033[92mline {line_number} \33[37m: \033[91m{wrong_template_string}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("How to use : python3 print_wrong_template_strings <directory>")
        sys.exit(2)
    JS_FILES_DIR = sys.argv[1]
    js_files = [f"{JS_FILES_DIR}/{filename}" for filename in os.listdir(JS_FILES_DIR)]
    template_strings = {}
    for js_file in js_files:
        with open(js_file, 'r') as file:
            template_strings_of_file = get_template_strings(file)
            if len(template_strings_of_file):
                template_strings[js_file] = template_strings_of_file
    wrong_template_strings = get_wrong_template_strings(template_strings)
    if len(wrong_template_strings):
        print_wrong_template_strings(wrong_template_strings)
        sys.exit(1)
    else:
        print(f"\033[92mYou haven't any wrong template strings in {JS_FILES_DIR}")
