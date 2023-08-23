from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'The DjangoOptimus ToolKit for Django is an all-in-one utility designed to simplify and enhance the deployment process of Django projects, particularly tailored for seamless integration with the Vercel hosting platform. This toolkit empowers developers with a range of powerful features, streamlining essential tasks and boosting productivity.'

# Setting up
setup(
    name="DjangoOptimus",
    version='0.0.1',
    author="NagiPragalathan N",
    author_email="nagipragalathan@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['Django>=2.0','TerminalDesigner'],  # Replace with actual dependencies
   KEYWORDS = [
    'DjangoOptimus', 'Django', 'Toolkit', 'deployment', 'Django projects',
    'Vercel hosting', 'HTML to Django Conversion', 'custom template tags',
    'Base Model Templates', 'Vercel Hosting Support', 'Modules and Functions',
    'Base.py', 'Host.py', 'Template.py', 'Designer', 'vercelkit.py',
    'Streamlined Deployment', 'Vercel platform', 'deployment files',
    'base settings', 'configurations', 'existing HTML content',
    'foreground colors', 'background colors', 'console output',
    'coding experience', 'deployment process', 'configuration overhead'
],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)