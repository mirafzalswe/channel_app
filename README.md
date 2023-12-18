# Channel_App

## Enjoy Reading

> This project is for creating posts. It is designed so that only admins can publish posts, and other users can only read those posts.

![image](https://github.com/mirafzal114/channel_app/assets/136591233/a53cfcf5-9c87-4411-9037-128848a264cf)

![image](https://github.com/mirafzal114/channel_app/assets/136591233/4786a466-073e-4b01-9c5a-441391bc14cb)

![image](https://github.com/mirafzal114/channel_app/assets/136591233/a305d071-315f-47f8-be84-dfe54265c466)


**A sample program works like this.


## Installation and Usage
## Project using pipenv
### The first step you must take is to work with pipenv

This project uses the pipenv tool to manage dependencies and the Python virtual environment.

### Install pipenv

1. Make sure Python is installed on your computer.
2. Install pipenv using the command:

   ```
    $ pip install pipenv
    ```
3. Install dependencies by running `pip install -r requirements.txt`

### Cloning the project and installing dependencies

1. Clone the repository:
    ```
    $ git clone https://github.com/mirafzal114/channel_app.git
    ```
2. Access the repository:
    ```
    $ git clone https://github.com/mirafzal114/channel_app.git
    ```

3. Run the `pipenv install` command to create a virtual environment and install all dependencies from the `Pipfile.lock` file.

### Working with the project

- To activate the virtual environment, run:
    ```
    pipenv shell
    ```
- To install new dependencies run:
    ```
    pipenv install <package_name>
    ```
- To run scripts or an application from your project, use ``pipenv run``.


**After you have logged into the `(channel_app) channel_app` environment, you will have `(channel_app) channel_app` in this form.

```bash
$ python manage.py makemigrations
```

**This will create all the migration files (database migrations) needed to run this application.

**To apply this migration, run the following command**
```bash
$ python manage.py migrate
```
**One final step, and then our application will be running. We need to create an admin user to run this application. Type the following command in the terminal and provide a username, password, and email address for the admin user.**
```bash
$ python manage.py createsuperuser
```
 ** Run the program with
 **Start the program with the command:**
```bash
$ python manage.py runserver
```

4. Exit the environment:
    ````bash
    $ exit
    ````

## Project using Docker
### Now if you have Docker, see the project to use it with.

This project uses Docker to manage its environment. To run it locally, follow these steps:

### Steps to start the project

### Install Docker

1. Make sure you have Docker installed on your computer.
2. If Docker is not installed, you can download it [from here](https://docs.docker.com/get-docker/) and install it according to the instructions for your operating system.

### Start the project
### We have already entered the repositories with `pipenv` before, now we will continue with the next one, but you first enter your `Docker Desktop` application if you do not have `Linux` of course:
1. Create a Docker image by running the command: 
    ```
    $ docker build -t my_channel .
    ```
2. Once the image has been successfully created, start the container: 
    ```
    $ docker run -p 1212:8000 my_channel
    ```
3. Check ``Dockerfile`` if you do not have an image download from ``Docker Hub``:
    ````bash
    $ docker pull python:3.11-alpine
    ````

Your project should now be available in your browser at `https://localhost:1212/posts`. - Here `posts/` means this from application Django.

5. Home Page:
    ```
    https://localhost:1212/posts
    ```
## Project home page. ##

## Project without Docker
###

1. Going into the environment:
    ```bash
    $ pipenv shell
    ```
2. Enter the command:
    ````bash
    $ python manage.py runserver
    ````

### Create a post
1. **Go to `admin` Page:**
    ```
    https://localhost/admin
    ```
2. **After entering the page, you can create your posts."
3. **Fill in the required fields:**
    - Image: Select an image(you can uploast post without image) file on your computer.
    - Title: Enter the title of your post.
    - Text: Write the content of your post.
4. Click the `Save` button to create your post.
5. Your post will be displayed on the page:
    ```
    https://localhost/posts/channel
    ```
**You can see them through this path.

## Contribute ##
**If you would like to contribute to the app please follow these steps:**

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make changes and commit with descriptive messages.
5. Submit your changes to your repository fork.
6. Create a pull request to the main repository.

## Contacts
**If you have any questions or suggestions regarding the application, please contact us at mirafzaaal2609@gmail.com We value your opinion!
