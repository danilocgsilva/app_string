from app_string.generate import generate
from app_string.FileListConfig import FileListConfig

def main():
    file_list_config = FileListConfig()
    # file_list_config.full_path = False
    # file_list_config.regex_ignore = "__pycache__|egg-info|^/build"
    generate(file_list_config)

if __name__ == "__main__":
    main()