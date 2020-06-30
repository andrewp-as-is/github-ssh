import setuptools

setuptools.setup(
    name='github-ssh',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/github-ssh']
)
