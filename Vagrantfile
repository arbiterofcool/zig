# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
echo I am provisioning
sudo apt-get update
yes | sudo apt-get install -y docker.io python-pip npm
git clone https://github.com/arbiterofcool/zig.git
sudo ln -sf /usr/bin/docker /usr/local/bin/docker

SCRIPT

=begin

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
sudo sh -c "echo deb https://get.docker.io/ubuntu docker main \
> /etc/apt/sources.list.d/docker.list"
sudo passwd -a vagrant docker
echo \"127.0.0.1      internal_registry\" >> /etc/hosts; \n"

=end

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "phusion/ubuntu-14.04-amd64"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.

  # Shipyard
  config.vm.network :forwarded_port, :host => 8000, :guest => 8000
  config.vm.network :forwarded_port, :host => 8005, :guest => 8005

  # Ruby
  config.vm.network :forwarded_port, :host => 3000, :guest => 3000

  # Postgres
  config.vm.network :forwarded_port, :host => 5432, :guest => 5432

  # Redis
  config.vm.network :forwarded_port, :host => 6379, :guest => 6379

  # Set up a bunch of forwarded ports to expose docker containers through the host OS without hassle...
  (49000..49900).each do |port|
    config.vm.network :forwarded_port, :host => port, :guest => port
  end

  # https://docs.vagrantup.com/v2/provisioning/docker.html
  config.vm.provision "docker" do |d|
    d.pull_images "postgres:9.4"
    d.pull_images "phusion/passenger-full:0.9.11"

    # For full shipyard
    d.pull_images "shipyard/shipyard"
    d.pull_images "shipyard/agent"
    d.pull_images "shipyard/deploy"
    d.pull_images "shipyard/redis"
    d.pull_images "shipyard/router"
    d.pull_images "shipyard/lb"
    d.pull_images "shipyard/db"
  end

  # config.vm.provision "shell"
  config.vm.provision "shell", inline: $script

  # sudo apt-get update
  # yes | sudo apt-get install lxc-docker
end
