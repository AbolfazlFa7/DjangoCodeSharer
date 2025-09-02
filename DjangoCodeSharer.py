import sys
from pathlib import Path
import colorama

colorama.init(autoreset=True)

FILE_TYPES = {
    '1': ('.py',),
    '2': ('.html', '.htm'),
    '3': ('.txt',),
    '4': ('.css',),
    '5': ('.js',),
    '6': ('.env',),
    '7': ('.py', '.html', '.htm', '.txt', '.css', '.js', '.env')
}


def get_user_choice():
    """Prompt user to select file types to process."""
    print(f'\n{colorama.Back.BLACK + colorama.Fore.YELLOW}Select file type (example: {colorama.Fore.GREEN}"123"{colorama.Fore.LIGHTBLUE_EX} for Python, HTML, and Text):')
    print(f"{colorama.Fore.CYAN}1{colorama.Fore.WHITE}. {colorama.Fore.LIGHTGREEN_EX}Python")
    print(f"{colorama.Fore.CYAN}2{colorama.Fore.WHITE}. {colorama.Fore.LIGHTRED_EX}HTML")
    print(f"{colorama.Fore.CYAN}3{colorama.Fore.WHITE}. {colorama.Fore.RESET}Text")
    print(f"{colorama.Fore.CYAN}4{colorama.Fore.WHITE}. {colorama.Fore.RED}CSS")
    print(f"{colorama.Fore.CYAN}5{colorama.Fore.WHITE}. {colorama.Fore.LIGHTYELLOW_EX}JavaScript")
    print(f"{colorama.Fore.CYAN}6{colorama.Fore.WHITE}. {colorama.Fore.LIGHTMAGENTA_EX}.env")
    print(f"{colorama.Fore.CYAN}7{colorama.Fore.WHITE}. {colorama.Fore.BLACK + colorama.Back.WHITE}All")
    choice = input(
        f"{colorama.Fore.LIGHTYELLOW_EX}Enter your choice: {colorama.Fore.LIGHTCYAN_EX}")

    selected_extensions = set()
    for char in choice.strip():
        if char not in FILE_TYPES:
            print(f"{colorama.Fore.LIGHTRED_EX}Invalid choice: {char}")
            sys.exit(1)
        selected_extensions.update(FILE_TYPES[char])
    return selected_extensions


def main():
    format_mode = '-f' in sys.argv
    target_path = Path(sys.argv[1] if len(
        sys.argv) > 1 and sys.argv[1] != '-f' else '.').absolute()
    print(f"{colorama.Fore.CYAN}Path: {colorama.Fore.GREEN}{target_path}")

    extensions = get_user_choice() if format_mode else {
        '.py', '.html', '.htm', '.env'}

    output_file = Path(__file__).with_name('file.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("My Django project, including all files and their locations:\n\n")

        for file_path in target_path.rglob('*.*'):
            if file_path.suffix.lower() in extensions:
                try:
                    content = file_path.read_text(encoding='utf-8')
                    f.write(f'File content: ({file_path}) -->\n{content}\n\n')
                    size_kb = file_path.stat().st_size / 1024
                    print(
                        f"{file_path}  {colorama.Fore.LIGHTGREEN_EX}Written {colorama.Fore.WHITE}{size_kb:.2f} KB")
                except Exception as e:
                    print(f"{file_path}  {colorama.Fore.LIGHTRED_EX}Error: {e}")
            else:
                print(f"{file_path}  {colorama.Fore.GREEN}Not written")

    size_kb = output_file.stat().st_size / 1024
    print(f"\n{colorama.Fore.CYAN}Done!")
    print(f"{colorama.Fore.BLUE}File size: {colorama.Fore.LIGHTYELLOW_EX}{size_kb:.1f} KB")


if __name__ == "__main__":
    main()
