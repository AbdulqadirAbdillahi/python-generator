from InquirerPy import prompt

# list of prompts for the user

quiz_questions = [
    {
        "type": "input", 
        "name": "project_title", 
        "message": "Enter the project title:"
    },

    {
        "type": "input", 
        "name": "project_desc", 
        "message": "Brief description of the project:"
    },

    {
        "type": "input",
        "name": "install_steps", 
        "message": "Installation steps:"
    },

    {
        "type": "input", 
        "name": "usage_info", 
        "message": "How to use this project:"
    },

    {
        "type": "list",
        "name": "project_license",
        "message": "Select a license for your project:",
        "choices": [
            "MIT", "Apache 2.0", "GPLv3", "Unlicense"
        ],
    },
    {
        "type": "input", 
        "name": "author_name", 
        "message": "Your name:"
    },
    {
        "type": "input", 
        "name": "contact_info", 
        "message": "Contact Info (email, Github, LinkedIn, etc):"
     },


]
