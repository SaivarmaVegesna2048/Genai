from setuptools import find_packages,setup
setup(
    name='Mcq_generator',
    version='0.0.1',
    author='krishna varma',
    author_email='saivarma1003@gmail.com',
    install_requires=['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
    
)