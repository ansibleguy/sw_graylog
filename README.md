<a href="https://graylog.org/products/source-available/">
<img src="https://graylog.org/wp-content/uploads/2022/07/GrayLog_Logo_color.png" alt="Graylog Server Logo" width="500"/>
</a>

# Ansible Role - Graylog-Server dockerized

Role to deploy dockerized Graylog-Server on a linux server

<a href='https://ko-fi.com/ansible0guy' target='_blank'><img height='35' style='border:0px;height:46px;' src='https://az743702.vo.msecnd.net/cdn/kofi3.png?v=0' border='0' alt='Buy me a coffee' />

[![Molecule Test Status](https://badges.ansibleguy.net/sw_graylog.molecule.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/molecule.sh.j2)
[![YamlLint Test Status](https://badges.ansibleguy.net/sw_graylog.yamllint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/yamllint.sh.j2)
[![PyLint Test Status](https://badges.ansibleguy.net/sw_graylog.pylint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/pylint.sh.j2)
[![Ansible-Lint Test Status](https://badges.ansibleguy.net/sw_graylog.ansiblelint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/ansiblelint.sh.j2)
[![Ansible Galaxy](https://badges.ansibleguy.net/galaxy.badge.svg)](https://galaxy.ansible.com/ui/standalone/roles/ansibleguy/sw_graylog)

Molecule Logs: [Short](https://badges.ansibleguy.net/log/molecule_sw_graylog_test_short.log), [Full](https://badges.ansibleguy.net/log/molecule_sw_graylog_test.log)

**Tested:**
* Debian 12

## Install

```bash
# latest
ansible-galaxy role install git+https://github.com/ansibleguy/sw_graylog

# from galaxy
ansible-galaxy install ansibleguy.sw_graylog

# or to custom role-path
ansible-galaxy install ansibleguy.sw_graylog --roles-path ./roles

# install dependencies
ansible-galaxy install -r requirements.yml
```

## Functionality

* **Package installation**
  * Ansible dependencies (_minimal_)


* **Configuration**
  * 


  * **Default config**:
    * Syslog Listeners on 5140 (TCP/UDP)
    * GELF Listeners on 12201 (TCP/UDP)
 

  * **Default opt-ins**:
    * Auto-Update Job


  * **Default opt-outs**:
    * Backup Job (*high storage usage*)

## Info

* **Note:** this role currently only supports debian-based systems


* **Note:** Most of the role's functionality can be opted in or out.

  For all available options - see the default-config located in [the main defaults-file](https://github.com/ansibleguy/sw_graylog/blob/latest/defaults/main/1_main.yml)!


* **Warning:** Not every setting/variable you provide will be checked for validity. Bad config might break the role!


## Usage

### Config

Define the config as needed:

```yaml
app:

```

You might want to use 'ansible-vault' to encrypt your passwords:
```bash
ansible-vault encrypt_string
```

### Execution

Run the playbook:
```bash
ansible-playbook -K -D -i inventory/hosts.yml playbook.yml
```

There are also some useful **tags** available:
* 
*

To debug errors - you can set the 'debug' variable at runtime:
```bash
ansible-playbook -K -D -i inventory/hosts.yml playbook.yml -e debug=yes
```
