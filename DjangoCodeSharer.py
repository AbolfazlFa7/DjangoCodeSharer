from pathlib import Path
import colorama
import sys

colorama.init(autoreset=True)

if '-f' in sys.argv:
    Format = True
    if len(sys.argv) == 2:
        sys.argv.insert(1, '.')
else:
    Format = False

python = False
html = False
text = False
css = False
js = False
if Format:
    print(f'\n{colorama.Back.BLACK+colorama.Fore.YELLOW}Select number code : {
          colorama.Fore.GREEN}Example{colorama.Fore.LIGHTBLUE_EX} "123" = python , html , text :')
    print()
    print(colorama.Fore.CYAN+'1' + colorama.Fore.WHITE +
          '.' + colorama.Fore.LIGHTGREEN_EX + ' Python')
    print(colorama.Fore.CYAN+'2' + colorama.Fore.WHITE +
          '.' + colorama.Fore.LIGHTRED_EX + ' Html')
    print(colorama.Fore.CYAN+'3' + colorama.Fore.WHITE +
          '.' + colorama.Fore.RESET + ' Text')
    print(colorama.Fore.CYAN+'4' + colorama.Fore.WHITE +
          '.' + colorama.Fore.RED + ' Css')
    print(colorama.Fore.CYAN+'5' + colorama.Fore.WHITE +
          '.' + colorama.Fore.LIGHTYELLOW_EX + ' Javascript')
    print(colorama.Fore.CYAN+'6' + colorama.Fore.WHITE + '. ' +
          colorama.Fore.BLACK+colorama.Back.WHITE + 'All')
    print()
    choice = input(colorama.Fore.LIGHTYELLOW_EX +
                   f'Enter your choice :{colorama.Fore.LIGHTCYAN_EX} ')

    python_format = False
    html_format = False
    text_format = False
    css_format = False
    js_format = False

    for x in choice.strip():
        if x == '1':
            python_format = True

        elif x == '2':
            html_format = True

        elif x == '3':
            text_format = True

        elif x == '4':
            css_format = True

        elif x == '5':
            js_format = True

        elif x == '6':
            python_format = True
            html_format = True
            text_format = True
            css_format = True
            js_format = True

        else:
            print(colorama.Fore.LIGHTRED_EX+'invalid choice')
            exit()


x = sys.argv[1] if len(sys.argv) > 1 else '.'
x = Path(r'{}'.format(x))
print(colorama.Fore.CYAN+'\nPath : '+colorama.Fore.GREEN+str(x.absolute()))

file = f"{Path(__file__).with_name('DjangoCodeSharer.txt').as_posix()}"
with open(file, 'a') as y:
    f = Path(file)

    if not f.exists():
        f.touch()
    else:
        f.write_text('')

    y.write("This is my django project , with all of its file and their location:\n\n")
    for a in x.rglob('*.*'):
        if Format:
            if python_format:
                python = a.suffix == '.py'
            if html_format:
                html = a.suffix == '.html' or a.suffix == '.htm'
            if text_format:
                text = a.suffix == '.txt'
            if css_format:
                css = a.suffix == '.css'
            if js_format:
                js = a.suffix == '.js'
        else:
            python = a.suffix == '.py'
            html = a.suffix == '.html' or a.suffix == '.htm'

        suffix = any([python, html, text, css, js])

        if suffix:

            try:
                y.write(f'content of this File : ({
                        a}) -->\n{a.read_text()}\n\n')
                print(f'{a}  {colorama.Fore.LIGHTGREEN_EX+'Writed' +
                      colorama.Fore.WHITE+' '+str('{:.2f}'.format(a.stat().st_size / 1024))+' Kb'}')
            except Exception as e:
                print(e)
                print(f'{a}  {colorama.Fore.LIGHTRED_EX+'Error'}')

        else:
            print(f'{a}  {colorama.Fore.GREEN+'Not Writed'}')


print(colorama.Fore.CYAN+'\nDone !')
print('\n'+colorama.Fore.BLUE+'File Size : ' + colorama.Fore.LIGHTYELLOW_EX +
      str('{:.1f}'.format(Path(file).stat().st_size / 1024))+' Kb')
