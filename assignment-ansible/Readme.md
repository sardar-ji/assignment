RBCAPP1 Ansible Playbook
------------------------
This evolving set of Ansible playbook creates an Ansible inventory file for 3 servers hosting httpd, rabbitmq and PostgresSQL services. It will  action based on a provided variable named "action":
    "action=verify_install": verifies the services are installed on their allocated hosts and if not, the playbook should install it.
    "action=check-disk" : with this action it should check the disk space on all servers and report any disk usage >  80%. Send an alert email to a selected email address.
    "action=check-status": with this action it should return the status of the application “rbcapp1” and a list of services that are down. (Used the REST endpoints created in TEST1).

Pre-requisites:
-------------

Controller Setup
--------------------
The controller is the computer the playbooks are run from (eg. your computer or Jenkins slave). This should be every step necessary to set up a clean macOS system to run the playbooks. This should only need to be done once.

1) Install Command Line Tools for Xcode by running xcode-select --install in Terminal
2) Install Homebrew, then install Ansible and ssh-copy-id
3) brew install ssh-copy-id ansible
4) Clone this repository:
    git clone https://github.com/sardar-ji/assignment/assignment-ansible.git
5) cd assignment-ansible

Running the playbook
----------------------
These first steps make sure the controller can talk to the target and execute commands.

First run
----------
1) Rename the hosts.ini to hosts and enter the addresses of your target machines and the name of the admin user.
2) Copy your SSH public key to the target or pass the key in the inventory file:
       ssh-copy-id -i ~/.ssh/mykey user@target_host
3) Update the nexus URL from where the rpms should be installed and add corporate proxy as needed in "assignment-ansible/inventories/assignment/group_vars/all.yml"

Playbook:
---------
assignment.yml: 
1) Inspect the installed services
2) Set up the yum.repos abd corporate proxy (optional)
3) Verfy the disk consumption and send an email if the disk utilization is greater than 80% to selected email reciepient.
4) Verify that the applications are installed, if not install them.
5) Retrieve the application status using rest api endpoints created in Test1


Command to run the playbook
----------------------------
ansible-playbook playbooks/assignment.yml -i inventories/assignment/hosts -e 'action=verify_install'

