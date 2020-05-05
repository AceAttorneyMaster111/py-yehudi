import setuptools
with open("README.md", "r") as f:
	long_description = f.read();
setuptools.setup(
	name="py-yehudi",
	version="0.0.1a1.dev1",
	author="Noah Simon",
	author_email="NoahS2003@gmail.com",
	description="A Python wrapper for the Sefaria API",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/AceAttorneyMaster111/py-yehudi",
	packages=setuptools.find_packages(),
	classifiers=[
		"Development Status :: 1 - Planning",
		"Intended Audience :: Developers",
		"Intended Audience :: Religion",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Programming Language :: Python :: 3.8",
		"Topic :: Religion"
	],
	python_requires="~=3.8",
	license="MIT",
)