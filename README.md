# Assignment 1

##Part 1: Docker file Creation, GitHub and Docker Hub Integration

●	Step 1 (5 marks): Identify a Sample Application

I have choosen a simple fast-api counter application for this assigment.
File: fastapi-app.py

●	Step 2 (5 marks): Identify the Dependencies
Dependencies required for this application includes 
- python to be installed
- pip should be working fine (python package manager)
- FastAPI
- uvicorn
First two covered through DockerFile, last two are mentioned in the file requirements.txt.

●	Step 3 (15 marks): Create a Docker file

Created docker file with python base image and rest of the format as per file: Dockerfile.
- Python from Docker Hub with the tag of latest.
- Dependencies intallation covered through RUN command
- Code file copied to that image
- Necessary files covered from requirements that will be installed by above mentioned RUN command
- Along with entrypoint configuration

●	Step 4 (25 marks): Build the Docker Image

In verifying the image, encountered issues in code. Resolved them by running code in python.

The following is the output and running status along with evidences:

G:\Git\Project01>docker build -t fastapi-app .
[+] Building 45.8s (10/10) FINISHED                                                                      docker:default
 => [internal] load .dockerignore                                                                                  1.9s
 => => transferring context: 2B                                                                                    0.1s
 => [internal] load build definition from Dockerfile                                                               0.8s
 => => transferring dockerfile: 200B                                                                               0.1s
 => [internal] load metadata for docker.io/library/python:latest                                                   4.6s
 => [auth] library/python:pull token for registry-1.docker.io                                                      0.0s
 => CACHED [1/4] FROM docker.io/library/python:latest@sha256:7b8d65a924f596eb65306214f559253c468336bcae09fd575429  0.0s
 => [internal] load build context                                                                                  0.2s
 => => transferring context: 733B                                                                                  0.0s
 => [2/4] COPY main.py main.py                                                                                     0.6s
 => [3/4] COPY requirements.txt requirements.txt                                                                   1.1s
 => [4/4] RUN pip install -r requirements.txt                                                                     34.3s
 => exporting to image                                                                                             2.1s
 => => exporting layers                                                                                            2.0s
 => => writing image sha256:bd596fbc18ff4564da0c2ca35343b3730bcc2d433915fc0fba3ade715fdc0b3c                       0.0s
 => => naming to docker.io/library/fastapi-app                                                                     0.1s

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview

G:\Git\Project01>docker images -a
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
fastapi-app   latest    bd596fbc18ff   25 seconds ago   1.05GB

G:\Git\Project01>docker run -d -p 2020:2020 --fastapi-container bd596fbc18ff4564da0c2ca35343b3730bcc2d433915fc0fba3ade715fdc0b3c
unknown flag: --fastapi-container
See 'docker run --help'.

G:\Git\Project01>docker run -d -p 2020:2020 --name fastapi-container bd596fbc18ff4564da0c2ca35343b3730bcc2d433915fc0fba3ade715fdc0b3c
094bea001ce1f40b29ced28edbf5b9007d280d36236a28e57ccdc818527822c8

![image](https://github.com/Smurfie07/myDevOps/assets/42376819/64e09cd5-b1a1-4fd0-ba66-75bbf2e61b57)
![image](https://github.com/Smurfie07/myDevOps/assets/42376819/4ab046ed-9818-490a-82ff-0d081ccc4c0a)
![image](https://github.com/Smurfie07/myDevOps/assets/42376819/7190a8ed-b4d9-41be-9608-360d9c559bbf)

●	Step 5 (25 marks): Push the Docker Image to Docker Hub
FIrst updated the tag of the image then pushed the same with that tag.

 G:\Git\Project01>docker tag bd596fbc18ff msurj/fastapi-app:041123

 G:\Git\Project01>docker images
 REPOSITORY          TAG       IMAGE ID       CREATED       SIZE
 msurj/fastapi-app   041123    bd596fbc18ff   2 hours ago   1.05GB
 fastapi-app         latest    bd596fbc18ff   2 hours ago   1.05GB

 G:\Git\Project01>docker push msurj/fastapi-app:041123
The push refers to repository [docker.io/msurj/fastapi-app]
72a315f07f81: Layer already exists
dc9df3c08322: Layer already exists
a3d8a0ba8c4c: Layer already exists
701d0b971f5f: Layer already exists
619584b251c8: Layer already exists
ac630c4fd960: Layer already exists
86e50e0709ee: Layer already exists
12b956927ba2: Layer already exists
266def75d28e: Layer already exists
29e49b59edda: Layer already exists
1777ac7d307b: Layer already exists
041123: digest: sha256:8d4680ac09d93d9f097e2ae12766d87e9e09f3fe46140f4c35e0aff3d1d5ba1c size: 2633

![image](https://github.com/Smurfie07/myDevOps/assets/42376819/ae1a5c3f-334a-407d-9ad9-f339ca47ad36)

 ●	Step 6 (10 marks): Create a GitHub Repository

This is the repo on GitHub created for Assigment 1
PATH: https://github.com/Smurfie07/myDevOps/

●	Step 7 (15 marks): Include a README.md file

This is the subjected file for the Assigment 1
PATH: https://github.com/Smurfie07/myDevOps/main/README.md

●	Step 8 (5 marks): Push the Codebase to GitHub
Commands used: Git init / add / status / commit / push [origin/branch] / pull [origin] [branch]
- First connecting local folder to this myDevOps repo.
- Configuring git congif to global for future authentication.
- And rest of the processes is init -> add -> push -> commit
![image](https://github.com/Smurfie07/myDevOps/assets/42376819/49566f8b-fa4c-4ee9-9fb5-6e03b7dcf754)



##Part 2: Docker Containers with Commands

●	Step 1 (5 marks): Using the docker image from Part 1

Using the same image from previous part i.e. fastapi-app

●	Step 2 (20 marks): Run the Docker Container

Command: G:\Git\Project01>docker run -d -p 2020:2020 --name fastapi-app-container bd596fbc18ff4564da0c2ca35343b3730bcc2d433915fc0fba3ade715fdc0b3c

-> 96e8b4f4534ce3b4f1c4ba9615a3f0b8b86d54cf0189299935c5858334bf8908

![image](https://github.com/Smurfie07/myDevOps/assets/42376819/be0d2b63-a951-4a89-bf9b-4925567687bf)

●	Step 3 (20 marks): Use Different Docker Container Commands
  //Use the following commands and copy paste their output in readme.md file.
  
■	'docker ps' command to list all running containers
G:\Git\Project01>docker ps
CONTAINER ID   IMAGE          COMMAND            CREATED         STATUS         PORTS                    NAMES
96e8b4f4534c   bd596fbc18ff   "python main.py"   3 minutes ago   Up 3 minutes   0.0.0.0:2020->2020/tcp   fastapi-app-container

■	'docker stop' command to stop a running container
G:\Git\Project01>docker stop
"docker stop" requires at least 1 argument.
See 'docker stop --help'.

Usage:  docker stop [OPTIONS] CONTAINER [CONTAINER...]

Stop one or more running containers

G:\Git\Project01>docker stop 96e8b4f4534c
96e8b4f4534c

■	'docker rm' command to remove a stopped container
G:\Git\Project01>docker ps -a
CONTAINER ID   IMAGE          COMMAND            CREATED         STATUS                     PORTS     NAMES
96e8b4f4534c   bd596fbc18ff   "python main.py"   6 minutes ago   Exited (0) 2 minutes ago             fastapi-app-container

G:\Git\Project01>docker rm 96e8b4f4534c
96e8b4f4534c

■	'docker logs' command to view the logs of a container
G:\Git\Project01>docker logs 9642b2755401fafe761cf0cbe15b6f953db735787548274e6cf396527f2b2689
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:2020 (Press CTRL+C to quit)
INFO:     172.17.0.1:59932 - "GET /docs HTTP/1.1" 200 OK
INFO:     172.17.0.1:59932 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     172.17.0.1:59932 - "GET /count HTTP/1.1" 200 OK
INFO:     172.17.0.1:59932 - "GET /count HTTP/1.1" 200 OK
INFO:     172.17.0.1:59932 - "GET /count HTTP/1.1" 200 OK
INFO:     172.17.0.1:59932 - "GET /count HTTP/1.1" 200 OK

■	'docker inspect' command to view the details of a container
G:\Git\Project01>docker inspect 9642b2755401fafe761cf0cbe15b6f953db735787548274e6cf396527f2b2689
[
    {
        "Id": "9642b2755401fafe761cf0cbe15b6f953db735787548274e6cf396527f2b2689",
        "Created": "2023-11-04T23:04:53.5233134Z",
        "Path": "python",
        "Args": [
            "main.py"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 1114,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-11-04T23:04:54.9108603Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:bd596fbc18ff4564da0c2ca35343b3730bcc2d433915fc0fba3ade715fdc0b3c",
        "ResolvConfPath": "/var/lib/docker/containers/9642b2755401fafe761cf0cbe15b6f953db735787548274e6cf396527f2b2689/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/9642b2755401fafe761cf0cbe15b6f953db735787548274e6cf396527f2b2689/hostname",
        "HostsPath": "/var/lib/docker/containers/9642b2755401fafe761cf0cbe15b6f953db735787548274e6cf396527f2b2689/hosts",
        "LogPath": "/var/lib/docker/containers/9642b2755401fafe761cf0cbe15b6f953db735787548274e6cf396527f2b2689/9642b2755401fafe761cf0cbe15b6f953db735787548274e6cf396527f2b2689-json.log",
        "Name": "/fastapi-app-container",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "2020/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "2020"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                29,
                120
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/476ea4c095890924b069a3557cfcf7d142175f5bdfdbdabb9b2cd7145db08ac1-init/diff:/var/lib/docker/overlay2/k9jvhbt0tq6a0l9oa1jbj68o3/diff:/var/lib/docker/overlay2/pjcxce3ty1kb9gqtsvwhbojtc/diff:/var/lib/docker/overlay2/q8i8h9zvg52rt6gxfi06zckti/diff:/var/lib/docker/overlay2/471de51bfb5da5036a5629a1db755978a28753a366790d2a7eecffafe2c09090/diff:/var/lib/docker/overlay2/5d5ef10797fbc53f96225c9cafe92ff6c1a8ae3e231e4222a32405f357a5e758/diff:/var/lib/docker/overlay2/6a1b90d9f7a8618368c3cc6064055a6d616a68c9a0af4fdafb8cfab07a097847/diff:/var/lib/docker/overlay2/5b633c9686462ac849d876fb388981dd15df3107235e09ea474f096c808955dc/diff:/var/lib/docker/overlay2/66a7c2e8aedf03613147c59adfb7c7a6ecb57dfa8b4fc317b7092aacdd1e2305/diff:/var/lib/docker/overlay2/d3b7278296381112934648054d4f6374cb35892cbaaf1fd8e73d2bcaf50fad49/diff:/var/lib/docker/overlay2/bece230eff18aef0db9eb719e9ac2156044e11241d5c652905757514aef9751c/diff:/var/lib/docker/overlay2/72294cf208cdbc38045422cf92f9cd251ba6e05778119eabcdf0828597582f57/diff",
                "MergedDir": "/var/lib/docker/overlay2/476ea4c095890924b069a3557cfcf7d142175f5bdfdbdabb9b2cd7145db08ac1/merged",
                "UpperDir": "/var/lib/docker/overlay2/476ea4c095890924b069a3557cfcf7d142175f5bdfdbdabb9b2cd7145db08ac1/diff",
                "WorkDir": "/var/lib/docker/overlay2/476ea4c095890924b069a3557cfcf7d142175f5bdfdbdabb9b2cd7145db08ac1/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "9642b2755401",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "2020/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305",
                "PYTHON_VERSION=3.12.0",
                "PYTHON_PIP_VERSION=23.2.1",
                "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/c6add47b0abf67511cdfb4734771cbab403af062/public/get-pip.py",
                "PYTHON_GET_PIP_SHA256=22b849a10f86f5ddf7ce148ca2a31214504ee6c83ef626840fde6e5dcd809d11"
            ],
            "Cmd": null,
            "Image": "bd596fbc18ff4564da0c2ca35343b3730bcc2d433915fc0fba3ade715fdc0b3c",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "python",
                "main.py"
            ],
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "b05e39ed4c563cf403dae2fd058788c2048024309010e188e8e683a44f0fdbaa",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "2020/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "2020"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/b05e39ed4c56",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "528cbd58cfc87082f2346318da3e1b8b89bdc44c08b6ba2b5502e67a43e26f66",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "cc156e33375333b3a56f6b84090bd02b92002e06d703a66e4e1bc38bc399996e",
                    "EndpointID": "528cbd58cfc87082f2346318da3e1b8b89bdc44c08b6ba2b5502e67a43e26f66",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]

■	'docker exec' command to execute a command inside a running container
G:\Git\Project01>docker exec 9642b2755401 python -V
Python 3.12.0

■	'docker attach' command to attach to a running container

■	'docker commit' command to create a new image from a container
■	'docker cp' command to copy files/folders between the container and the host
■	'docker stats' command to view the resource usage of containers
■	'docker top' command to view the running processes inside a container
■	'docker start' command to start a stopped container
■	'docker pause' command to pause a running container
■	'docker unpause' command to unpause a paused container
■	'docker rename' command to rename a container
■	'docker wait' command to wait for a container to exit and then display its exit code
■	'docker attach' command to attach local standard input, output, and error streams to a running container
■	'docker port' command to display the public-facing port that a container is listening on
G:\Git\Project01>docker port 9642b2755401
2020/tcp -> 0.0.0.0:2020

■	'docker update' command to update a container's resource limits
G:\Git\Project01>docker update -m "0.5" 9642b2755401
9642b2755401

■	'docker restart' command to restart a running container
G:\Git\Project01>docker restart 9642b2755401
9642b2755401

●	Step 4 (25 marks): Document Your Results in README.md

> Documented above in this README file

●	Step 5: Push the codebase for the sample application to your GitHub repository (create a new one for this part)



##Part 3: Docker Volumes

●	Create a new Docker volume named "my_volume". (2 marks)
●	Create a new Docker container using the "nginx" image and mount the "my_volume" volume to the container's "/usr/share/nginx/html" directory. (4 marks)
●	Verify that the "nginx" default page is accessible on your host machine at http://localhost:8080. (2 marks)
●	Create a new file named "index.html" on your host machine and add some text to it. (2 marks)
●	Copy the "index.html" file from your host machine to the "my_volume" volume using the "docker cp" command. (4 marks)
●	Verify that the "index.html" file is accessible on your host machine at http://localhost:8080. (2 marks)
●	Stop and remove the container. (2 marks)
●	Create a new Docker container using the "httpd" image and mount the "my_volume" volume to the container's "/usr/local/apache2/htdocs" directory. (4 marks)
●	Verify that the "httpd" default page is accessible on your host machine at http://localhost:8081. (2 marks)
●	Create a new file named "about.html" on your host machine and add some text to it. (2 marks)
●	Copy the "about.html" file from your host machine to the "my_volume" volume using the "docker cp" command. (4 marks)
●	Verify that the "about.html" file is accessible on your host machine at http://localhost:8081/about.html. (2 marks)
●	Stop and remove the container. (2 marks)
●	Verify that the "index.html" and "about.html" files are still available in the "my_volume" volume. (4 marks)
●	Cleanup: Remove the "my_volume" volume. (2 marks)
●	Create a README.md file and document your findings for each command. For each command, provide a brief description of what it does, followed by the output and logs generated by the command. Ensure that the README.md file is well-organized, easy to read, and contains all necessary information. (14 marks)
●	Push the codebase for the sample application to your GitHub repository (create a new one for this part)
