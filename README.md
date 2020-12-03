<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/github-ssh.svg?maxAge=3600)](https://pypi.org/project/github-ssh/)
[![](https://img.shields.io/npm/v/github-ssh.svg?maxAge=3600)](https://www.npmjs.com/package/github-ssh)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/github-ssh/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/github-ssh/actions)

### Installation
```bash
$ [sudo] pip install github-ssh
```

```bash
$ [sudo] npm i -g github-ssh
```

#### How it works
+   creates ssh key files, ssh config file, copies public key to clipboard and opens [github settings -> SSH keys](https://github.com/settings/keys)
+   skip if ssh key exists and works

#### Features
**github multiple ssh keys**

#### Config
#### `~/.ssh/config`

```
Host *
    Include config.d/*
    Include config.d/*/*
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
    <a href="https://readme42.com/">readme42.com</a>
</p>
