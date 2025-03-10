type Commands = Tuple[str, ...]
type Shell_Builder = Tuple[str, Commands]

# IMPORTANT: the Callable couldnt be typed with the Tuple[str, ...] within it's body.
## It needed a redirection of type Commands to perform this
def shell_extract(commands: Callable[[Shell_Builder], str|bool], **kwargs) -> Tuple[str | bool]:
    results = []

    template = commands[0]

    for command in commands[1]: 
        results.append(shell(template % command))

    return results

def shell(shell_order: str, _return: bool) -> str | bool:
    try:
        result = subprocess.run(shell_order, capture_output=True, shell=True)
    except:
        return False
    
    if _return:
        return result.stdout.decode().strip()
    
    return True

def test() -> NoReturn:
    base_command = 'ls -l /etc/shadow | cut -d " " -f %s'
    user = '1 | cut -c5-6'
    group = '4'
    other = '8-9'

    results = shell_extract((base_command, (user, group, other)))

    if isinstance(results, list):
        for idx, option in enumerate(['user', 'group', 'other']):
            if idx < 2:
                if 'r' in (tmp := results[idx]) and 'w' in tmp:
                    print(f'The {option} has writeable and readable access to the shadow file!')
                elif 'r' in results[idx]:
                    print(f'The {option} has readable access to the shadow file!')
                elif 'w' in results[idx]:
                    print(f'The {option} has writeable access to the shadow file!')
            else:
                print(f'All others has the following access: {results[idx]}')
