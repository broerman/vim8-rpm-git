
Vagrant.configure(2) do |config|
  config.vm.box = "generic/centos7"
  config.vm.synced_folder ".", "/vagrant" ,
    type: "nfs" ,
    linux__nfs_options: ['rw','no_subtree_check','no_root_squash','async']
  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yml"
  end
end

