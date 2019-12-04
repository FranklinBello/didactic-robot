# Cygnus

## Installation

1. Clone the project from the *development* branch into your file system.
    a.
    ```
    git clone URL/of/the/repository.git
    ```
    b. 
    ```
    cd didactic-robot
    ```
    c. 
    ```
    git remote -v
    ```
    d.
    ```
    git checkout -b develop
    ```
    e.
    ```
    git branch
    ```
    e.
    ```
    git pull origin develop
    ```
2. In the folder containing the project, create an environment called ```env```. 
    For macOs and Linux use the commnand:
    ```
    $ python -m venv env
    ```
    For Windows:
    ```
    python -m venv env
    ```
3. Activate the environment by running:
    For macOs and Linux:
    ```
    $ source env/bin/activate
    ```
    For Windows:
    ```
    env\Scripts\activate
    ```
    The environment is active when ```(env)``` appears above or to the left of the command line.
4. Install the required packages by running:
    ```
    $ pip install -r requirements.txt
    ``` 
5. Set up the environment variables
    ```
    export FLASK_APP=run.py
    export FLASK_ENV=development
    ```
6. To run the ap
    ```
    flask run
    ```

## Resources

##### Webpages
- Flask Official Documentation: [Link](http://flask.palletsprojects.com/en/1.1.x/tutorial/)
- Flask Mega Tutorial: [Link](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- Explore Flask: [Link](https://exploreflask.com/en/latest/preface.html)

##### Videos
Corey Schaffer: [Link](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
Julian Nash: [Link](https://www.youtube.com/watch?v=BUmUV8YOzgM&list=PLF2JzgCW6-YY_TZCmBrbOpgx5pSNBD0_L)