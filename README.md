<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/github-ssh.svg?maxAge=3600)](https://pypi.org/project/github-ssh/)
[![](https://img.shields.io/npm/v/github-ssh.svg?maxAge=3600)](https://www.npmjs.com/package/github-ssh)
[![Travis](https://api.travis-ci.org/looking-for-a-job/github-ssh.svg?branch=master)](https://travis-ci.org/looking-for-a-job/github-ssh/)

#### Installation
```bash
$ [sudo] npm i -g github-ssh
```
```bash
$ [sudo] pip install github-ssh
```

#### Features
**github multiple ssh keys**

#### How it works
+   creates ssh key files, ssh config file, copies public key to clipboard and opens [github settings -> SSH keys](https://github.com/settings/keys)
+   skip if ssh key exists and works

#### `~/.ssh/config`

```
Host *
    Include config.d/*
    Include config.d/*/*
```

#### CLI
```bash
usage: github-ssh username
```

#### Examples
```bash
$ github-ssh username
```

created files:
```
~/.ssh/github/id_rsa_github_username
~/.ssh/github/id_rsa_github_username.pub     (add to github settings -> SSH keys)
~/.ssh/config.d/github/username.github.com
```

```bash
$ cd path/to/repo
$ git remote add github git@username.github.com:username/repo.git
```

#### Links
+   [github settings -> SSH keys](https://github.com/settings/keys)

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>