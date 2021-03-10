# This app solves the following problem

Authenticating and signing up users: This involves building an API to sign up the
users and store the user details in an
appropriate database. The database will have to be designed by the applicant.
Registration endpoint

    1. Sign up API

    This should accept all kinds of parameters. Bio fields like - Name, Email, Phone.

    - Identification fields like - Username, Userld.

    - Authentication fields like a password. Care must be taken that passwords
    should not be stored in plain text.

    - The fields must be checked for validity (passwords must be 8 characters long, usernames should be unique, the name should not have letters, etc)
    and the API must return a valid error in case something is invalid. Should return a successful message, if everything is valid. Login endpoint

    2. Login API
       1. Should accept username and password.
       2. Returns a failed message if authentication fails Should return all the Biodata fields of the user in case the username and password match.

## Installation

Make sure the that the ptython version is >=3.8.

### Environment Setup

The following demonstrates setting up and working with a development environment:

    ```
    $ make virtualenv
    $ source env/bin/activate
    ```

### Intall dependencies

To install the dependencies, run the following:

    ```
    $ pip install -r requirements.txt
    ```

## Run

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

Go to the project root directory and execute the command:

    ```
    $ make run
    ```

Alternatively, you can try

    ```
    $ docker-compose up
    ```

Alternatively, you can try

    ```
    $ python intellify_backend/manage.py runserver 9000
    ```

## Examples

To get the examples, you can try the following commands

    ```
    $ make show_examples
    ```

## Testcases

The command to test it as follows:

    ```
    $ make test
    ```

## Docker

Included is a basic `Dockerfile` for building and running the application, and can be built with the included `make` helper:

    ```
    $ make docker
    ```