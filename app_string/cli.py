import argparse
from app_string.generate import generate
from app_string.FileListConfig import FileListConfig

def main():
    parser = argparse.ArgumentParser(description="Create a long string with all file paths and contents from an application")
    
    # Add arguments
    parser.add_argument("path", nargs="?", help="Path to fetch all contents (optional, will prompt if not provided)")
    parser.add_argument("--no-ignore-git", action="store_true", help="Don't ignore .git directories")
    parser.add_argument("--no-ignore-node-modules", action="store_true", help="Don't ignore node_modules directories")
    parser.add_argument("--no-ignore-vendor", action="store_true", help="Don't ignore vendor directories")
    parser.add_argument("--no-ignore-var-cache", action="store_true", help="Don't ignore var/cache directories")
    parser.add_argument("--no-ignore-file", action="store_true", help="Don't use .app-string-ignore file")
    parser.add_argument("--only-path", action="store_true", help="Only show file paths, not contents")
    parser.add_argument("--full-path", action="store_true", help="Show full paths instead of relative paths")
    parser.add_argument("--regex-ignore", help="Regex pattern to ignore files/directories")
    
    args = parser.parse_args()
    
    # Create config object
    file_list_config = FileListConfig()
    
    # Apply command line arguments
    if args.no_ignore_git:
        file_list_config.ignore_git = False
    if args.no_ignore_node_modules:
        file_list_config.ignore_node_modules = False
    if args.no_ignore_vendor:
        file_list_config.ignore_vendor = False
    if args.no_ignore_var_cache:
        file_list_config.ignore_var_cache = False
    if args.no_ignore_file:
        file_list_config.ignore_file = False
    if args.only_path:
        file_list_config.only_path = True
    if args.full_path:
        file_list_config.full_path = True
    if args.regex_ignore:
        file_list_config.regex_ignore = args.regex_ignore
    
    # Pass path to generate function
    generate(file_list_config, args.path)

if __name__ == "__main__":
    main()