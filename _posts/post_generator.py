import datetime
import os

def get_file_paths(date, post_name):
    _post_dir = os.path.dirname(os.path.realpath(__file__))
    site_dir = os.path.dirname(_post_dir)
    post_files_dir = os.path.join(os.path.join(site_dir, "assets"), "post_files")
    post_path = os.path.join(_post_dir, f'{date}-{post_name}.md')
    post_files_path = os.path.join(post_files_dir, post_name)
    print(post_path)
    print(post_files_path)
    return post_path, post_files_path

def create_path(given_path):
    if not os.path.exists(given_path):
        os.makedirs(given_path)


def get_times():
    cur_time = datetime.datetime.now()
    date = cur_time.date()
    exact_time = str(cur_time.time())
    exact_time = exact_time.replace(".", " +/-")[0:-2]
    return date, exact_time

def process():
    post_name = input("Post name:")
    date, exact_time = get_times()
    post_path, post_files_path = get_file_paths(date, post_name)
    header = f"---\ntitle: {post_name.replace('_', ' ')} \ndate: {date} {exact_time}\ncategories: []\ntags: []\npin: false\ncomments: false\ntoc: false\nmermaid: false\nmath: false\n---"
    comment = f"<!-- \n    Post Name:{post_name}\n    Post File dir: {post_files_path}\n-->"
    markdown_content = header + '\n\n' + comment + '\n'
    return markdown_content, post_path, post_files_path


def generate(markdown_content, post_path, post_files_path):
    print(f"generating {post_files_path} ...")
    create_path(post_files_path)
    print(f"writing markdown...")
    with open(post_path, 'w') as the_file:
        the_file.write(markdown_content)
    print(f"Finished!")

if __name__ == "__main__":
    markdown_content, post_path, post_files_path = process()
    generate(markdown_content, post_path, post_files_path)


