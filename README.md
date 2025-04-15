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

# starting dev mode

        C:\prog\doro> poetry run flask --app src/doro/app run
        