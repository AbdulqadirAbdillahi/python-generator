# main file to run readme generator

from InquirerPy import prompt
from prompts import quiz_questions

def project_readme(answers):

    return f"""
# {answers['project-title']}

## Description
{answers['project_desc']}

## Installation
{answers['install_steps']}

## Usage
{answers['usage_info']}

## License
{answers['project_license']}

## Author
{answers['author_name']}

## Contact
{answers['contact_info']}

"""

def main():

    user_answers = prompt(quiz_questions)

    readme = project_readme(user_answers)

    with open("README.md", "w") as file:
      file.write(readme)
# saves the readme file

    print("README.md generated successfully!")

if __name__ == "__main__":
    main()