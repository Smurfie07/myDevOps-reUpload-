# Assignment 1

Part 1: Docker file Creation, GitHub and Docker Hub Integration

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

- First connecting local folder to this myDevOps repo.
- 
