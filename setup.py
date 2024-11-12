import setuptools

#with open("README.md","r",encoding="utf.8") as f:
with open("README.md", "r", encoding="utf-8") as f: 
    long_description = f.read()


    __version__ = "0.0.0"

    REPO_NAME = "chicken-fecal-classification_project"
    AUTHOR_USER_NAME ="itisha249"
    SRC_REPO = "cnn-classifier"
    AUTHOR_EMAIL = "itishahmt@gmail.com"


    setuptools.setup(
        name=SRC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        author_email=AUTHOR_EMAIL,
        description="a small python package for cnn app",
        long_description= long_description,
        long_description_content = "text/markdown",
        url=f"https://github.com/(AUTHOR_USER_NAME)/(REPO_NAME)/issues"
    )
    package_dir = {"": "src"},
    packages=setuptools.find_packages(where="src")