from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8', errors='ignore') as f:
    readme = f.read()

setup(
    name='human_genome_projects',
    version='0.1.0',
    description='Manipulating txt, csv files with human genome information.',
    long_description=readme,
    author='Maurizio Lopez',
    author_email='maurizio.school@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={'console_scripts': ['human_genome_projects=human_genome_projects.main',]}
)
