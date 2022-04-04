from os import walk

def walk_folder(path):
  folder_list = []

  for _,_,files in walk(path):
    for file in files:
      folder_list.append(file)
  return folder_list

my_list = walk_folder('./folder')

print(my_list)