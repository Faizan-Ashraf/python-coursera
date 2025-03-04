with open("python-coursera/abc.txt","r") as file:
    # print(file.read()) # return all data of file
    # print(file.readline()) # prints only first line
    f_content = file.read()
    f_content_list = f_content.split('\n') # stores in a list
    print(f_content_list[0])