import setuptools

setuptools.setup(
    name='github-ssh',
    version='2020.12.3',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/github-ssh']
)
