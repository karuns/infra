Ref:https://www.youtube.com/watch?v=vmSMrQ8Ev9w&t=77s
Steps:
1) create folder and files
    Dockerfile
    app/
        index.js
2) Install npm module : for mac --> brew install npm
3) cd  to workdir i.e. /app folder
4) create npm project: npm init -y
5) write simple script inside index.js and test it
6) write Docker file
    1) Take base image for nodejs (i.e. node)
    2) set working directory
    2) copy /app code to working directory
    3) install npm
    4) run app
    5) expose port
7) build docker image
    1) docker build -t nodeapp .
8) run docker image
    1) docker run -d -p 9003:9999 --name nodeapp3 nodeapp

