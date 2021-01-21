from setuptools import setup
gh_repo = 'https://github.com/weaming/git-refs'

setup(
    name='git-refs',  # Required
    version='0.1',  # Required
    description='list git references(branches, tags) on local and remote repositories',  # Required
    url=gh_repo,  # Optional
    author='weaming',  # Optional
    author_email='garden.yuen@gmail.com',  # Optional
    py_modules=['git_refs'],
    keywords='git,cli,develop',  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'git-refs=git_refs:main',
        ],
    },

    project_urls={  # Optional
        'Bug Reports': gh_repo,
        'Source': gh_repo,
    },
)
