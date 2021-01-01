vim82 on Redhat/Centos 7
=======================

Compile vim in a vagrant enviroment

The SPEC file for building vim package is kept simple.
It loads vim source from githup and compiles in one rpm package

vagrant exports the rpmbuild directories of the builing host.

#### run vagrant to build the vim package.

    vagrant up

#### cleanup before another build 

    sudo rm -rf rpmbuild/*
    
#### install  vim build for centos7

    rpm -Uvh https://github.com/broerman/vim8-rpm-git/blob/master/rpmbuild/RPMS/x86_64/vim-8.2-2230.el7.x86_64.rpm
