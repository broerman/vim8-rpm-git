vim82 on Redhat/Centos 7
=======================

Compile vim in a vagrant environment.

The SPEC file for building vim package is kept simple.
It loads vim source from github and compiles in one rpm package.
Some files like man pages are removed to avoid dependency errors, when installing beside distropackage.
The binary is located in /usr/local/bin.

#### vim.spec 

The vim.spec also includes vim-plugins.  

- lightline
- editorconfig
- ale

#### run vagrant to build the vim package.

    vagrant up

#### cleanup before another build 

    sudo rm -rf rpmbuild/*
    
#### install  vim build for centos7

    rpm -Uvh https://github.com/broerman/vim8-rpm-git/blob/master/rpmbuild/RPMS/x86_64/vim-8.2-2230.el7.x86_64.rpm
