from app_string.generate import generate
from app_string.FileListConfig import FileListConfig

def main():
    file_list_config = FileListConfig()
    file_list_config.ignore_content = True
    file_list_config.full_path = False
    generate(file_list_config)

if __name__ == "__main__":
    main()