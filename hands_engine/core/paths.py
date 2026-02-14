# Path Management Utilities

# Function to ensure a directory exists

def ensure_dir(directory):
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to get the data directory

def get_data_dir():
    import os
    return os.path.join(os.path.dirname(__file__), 'data')

# Function to get the skills directory

def get_skills_dir():
    return os.path.join(get_data_dir(), 'skills')

# Function to get the logs directory

def get_logs_dir():
    return os.path.join(get_data_dir(), 'logs')

# Function to get the fixtures directory

def get_fixtures_dir():
    return os.path.join(get_data_dir(), 'fixtures')

# Function to get a specific skill directory

def get_skill_dir(skill_name):
    return os.path.join(get_skills_dir(), skill_name)

# Function to get a skill file

def get_skill_file(skill_name, file_name):
    return os.path.join(get_skill_dir(skill_name), file_name)

# Function to get the skill anchors directory

def get_skill_anchors_dir(skill_name):
    return os.path.join(get_skill_dir(skill_name), 'anchors')

# Function to get a skill anchor file

def get_skill_anchor_file(skill_name, anchor_file_name):
    return os.path.join(get_skill_anchors_dir(skill_name), anchor_file_name)
