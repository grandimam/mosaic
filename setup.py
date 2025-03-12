from setuptools import setup, find_packages

setup(
    name="mosaic",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',
    ],
    author="Your Name",
    author_email="your-email@example.com",
    description="A Django library for using React-style components in templates.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
    ],
)
