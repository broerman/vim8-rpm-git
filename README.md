vim82 on Redhat/Centos 7
=======================

Compile vim in a vagrant enviroment

The SPEC file for building vim package is kept simple.
It loads vim source from githup and compiles in one rpm package

vagrant exports the rpmbuild directories of the builing host.

####

    vagrant up


    


#### cleanup

    sudo rm -rf rpmbuild/*