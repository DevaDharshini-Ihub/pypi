from setuptools import setup, find_packages

setup(
    name='pypiexample',  # Replace with your package name
    version='0.1.0',   # Version of your package
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        # List your package dependencies here
    ],
    author="Deva Dharshini",
    author_email='xxx.com',  # Your email
    description=' a greeting message.',
    long_description=open('README.md').read(),  # Use README.md for long description
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your-repo-name',  # Your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change to your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
)
