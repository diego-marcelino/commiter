from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_1, custom_style_2, custom_style_3

options_type = (
    'feat: A new feature',
    'build: build system or external dependencies',
    'fix: A bug fix',
    'docs: Documentation only changes',
    'refactor: A code change that neither fixes a bug nor adds a feature',
    'style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)',
    'test: Adding missing tests or correcting existing tests',
    'ci: CI configuration files and scripts',
    'perf: A code change that improves performance',
)

def get_type_from_selected(selected):
    selected = selected.split(':')[0]
    return selected

choice_commit_type = {
    'type': 'list',
    'name': 'commit_type',
    'message': 'Commit type',
    'choices': options_type,
    'filter': get_type_from_selected
}

def filter_commit_title(title):
    return title

input_title = {
    'type': 'input',
    'name': 'title',
    'message': f'Commit title {50} chars left',
    'filter': filter_commit_title
}

commit_body = {
    'type': 'editor',
    'name': 'bio',
    'message': 'Please write a short bio of at least 3 lines.\n',
    'default': 'Hello World',
}

questions = [
    choice_commit_type,
    input_title,
    commit_body
]

if __name__ == '__main__':
    answers = prompt(questions, style=custom_style_3)
    commit_type = answers['commit_type']
    title = answers['title']
    commit_body = answers['bio']

    commit_message = '{}: {}\n\n{}'.format(
            commit_type, title, commit_body.strip()
        )

    commit_command = f'git commit -m "{commit_message}"'

    print(commit_command)

