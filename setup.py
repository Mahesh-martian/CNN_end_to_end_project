import setuptools

__version__ = '0.0.1'

with open('README.md', 'r',encoding='utf-8') as f:
    log_desc = f.read()

REPO_NAME = 'cnnClassifier'
AUTHOR_NAME = 'Mahesh Kumar'
SRC_REPO = 'CNNclassifier'
AUTHOR_EMAIL = 'maheshkumar2010@gmail.com'

setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author = AUTHOR_NAME,
    author_email = AUTHOR_EMAIL,
    
    description= 'this is my classifier project',
    long_description= log_desc,
    
    long_description_content = "text/markdown",
    url = f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}',
    
    project_url = {
    "Bug Tracker" : f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues',
    },
    
    package_dir={'':"src"},
    packages=setuptools.find_packages(where='src')
)