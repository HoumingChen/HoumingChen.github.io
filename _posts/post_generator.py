import datetime
import sys
print(sys.argv)
if len(sys.argv) > 1:
  post_name = str(sys.argv[1])
else:
  post_name = "untitled"

cur_time = datetime.datetime.now() 
date = cur_time.date()
exact_time = str(cur_time.time())
exact_time = exact_time.replace(".", " +/-")[0:-2]
header = f"---\ntitle: post_name \ndate: {date} {exact_time}\ncategories: []\ntags: []\npin: false\ncomments: false\ntoc: false\nmermaid: false\n---"
print(header)
with open(f'{date}-{post_name}.md', 'w') as the_file:
    the_file.write(header)
