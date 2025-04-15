## content

personal tutorial project following roughly https://realpython.com/docker-continuous-integration/


# steps before committing changes

1. lint your code with pylint

        C:\prog\doro> poetry run pylint src/doro/

2. test your code with pytest

        C:\prog\doro> poetry run pytest

3. check your changes 

        C:\prog\doro> git diff

if everything is fine, commit the change.

# creating a docker image (localy)

1. build the image (localy)

        C:\prog\doro> docker build -t doro .

2. run the container from the image

        C:\prog\doro> docker run -p 5000:5000 --name sdoro doro

this binds the internal port 5000 from the container to the host machines port 5000, also names the image 'sdoro' to have an easy acces into the container if needed

3. get into the bash console inside the container

        docker exec -ti sdoro bash

here you can try `wget http://localhost:5000` to fiddle with the server internally


# starting dev mode

        C:\prog\doro> poetry run flask --app src/doro/app run
        