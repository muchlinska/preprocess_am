import setuptools

with open('READ ME.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_am',
	version = '0.0.9',
	author = 'Anna M',
	author_email = 'anna.muchlinska@gmail.com',
	description = 'This is preprocessing package',
	long_description = 'long_description',
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Progmramming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	'Operating System :: OS Independent'],
	python_requires = '>=3.9.13'
	)