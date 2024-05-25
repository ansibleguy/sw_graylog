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

----

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

----

## Roadmap

* GeoIP download and mapping for [easy integration](https://graylog.org/post/how-to-set-up-graylog-geoip-configuration/)

----

## Usage

### Config

Minimal example:

```yaml
graylog:
  domain: 'log.template.ansibleguy.net'
  secret: !vault |
    ...
  pwd:
    graylog: !vault |  # admin
      ...
    opensearch: !vault |  # admin
      ...
```

Update as needed:

```yaml
graylog:
  domain: 'log.template.ansibleguy.net'
  aliases: ['syslog.template.ansibleguy.net']
  secret: !vault |
    ...
  pwd:
    graylog: !vault |  # admin
      ...
    opensearch: !vault |  # admin
      ...  

  manage:
    webserver: true  # you could disable the role-managed nginx if you want to self-manage it

  docker_nftables: true  # self-manage firewall; clear docker auto-created rules
  
  settings:  # graylog config file settings; see: https://github.com/Graylog2/graylog2-server/blob/6.0.0/misc/graylog.conf
    inputbuffer_processors: 5
    processbuffer_processors: 5
    outputbuffer_processors: 3

  opensearch:
    ram: '10g'

  backup:  # WARNING: high disk usage
    enable: true
    retention_days: 14

  auto_update:  # auto update containers to latest minor release
    enable: true
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
* config
* install
* docker
* webserver
* backup

To debug errors - you can set the 'debug' variable at runtime:
```bash
ansible-playbook -K -D -i inventory/hosts.yml playbook.yml -e debug=yes
```

----

## Functionality

* **Package installation**
  * Ansible dependencies (_minimal_)
  * Docker server and client
  * Nginx if webserver is managed


* **Configuration**

  * **Default config**:
    * Syslog Listeners on 5140 (TCP/UDP)
    * GELF Listeners on 12201 (TCP/UDP)
    * 4GB of RAM for OpenSearch
    * [Disk watermark for OpenSearch](https://opensearch.org/docs/2.2/api-reference/cluster-api/cluster-settings/) set to 99%
 

  * **Default opt-ins**:
    * Auto-Update Job
    * Managing Webserver => see: [THIS Role](https://github.com/ansibleguy/infra_nginx)


  * **Default opt-outs**:
    * Backup Job (*high storage usage*)

## Info

* **Note:** this role currently only supports debian-based systems


* **Note:** Most of the role's functionality can be opted in or out.

  For all available options - see the default-config located in [the main defaults-file](https://github.com/ansibleguy/sw_graylog/blob/latest/defaults/main/1_main.yml)!


* **Warning:** Not every setting/variable you provide will be checked for validity. Bad config might break the role!


* **Note:** The Graylog `secret` has to be at least 16 characters long!


* **Note:** The OpenSearch admin password has to meet some complexity criteria:

  * minimum length of 8 characters
  * at least one lowercase character
  * at least one uppercase character
  * at least one digit
  * at least one special character
