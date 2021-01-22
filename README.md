# FOSDEM21-Demo

Demo for my talk at FOSDEM 2021 — https://bit.ly/3oO3Lsw

<br>

## Requirements

* Docker
* Watchman
* Ansible toolset
* Useful linux packages


## Ansible overview

Create a container using thhe ansible toolset docker image, andd open enter into the container

```bash
$ docker run -it --rm  quay.io/ansible/toolset bash
# root@93891a6d52ce:/#
```

Create a new role 

```bash 
root@93891a6d52ce:$ ansible-galaxy role init fosdem21
# - Role fosdem21 was created successfully
```

Let's look at the role folder structure
```bash
root@93891a6d52ce:$ apt intall tree # Install 'tree' package
root@93891a6d52ce:$ tree -L 2  fosdem21
# fosdem21
# ├── README.md
# ├── defaults
# │   └── main.yml
# ├── files
# ├── handlers
# │   └── main.yml
# ├── meta
# │   └── main.yml
# ├── tasks
# │   └── main.yml
# ├── templates
# ├── tests
# │   ├── inventory
# │   └── test.yml
# └── vars
#     └── main.yml
```