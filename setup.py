import setuptools

setuptools.setup(
    name="my_python_package_from_github",
    version="0.0.1",
    author="Kayode Adechinan",
    author_email="kayode.adechinan@gmail.com",
    description="simple python package hosted on Github",
    packages=setuptools.find_packages(),
    install_requires=[],
    license='MIT',
    zip_safe=False
)
