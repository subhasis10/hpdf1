# hpdf1
Task 1 for HPDF

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Install Python 3

```
$ sudo apt-get install python3.6
```
2. Create a virtual environment and activate it.

```
$ virtualenv venv
$ source venv/bin/activate
```
3. Install flask in the virtual environment using pip.

```
(venv) $ pip install flask
```
4. To deactivate the virtual environment.

```
(venv) $ deactivate
```

### Installing

Clone the repository using the command

```
$ git clone https://github.com/subhasis10/hpdf1.git
```

Now go to the project directory and run the __init__.py file

```
(venv) $ python __init__.py 
```
Go to the browser and the type ```http://http://127.0.0.1:5000/``` to see the homepage and then go to subsequent endpoints as given in the tasks.


## Tasks
1. A simple hello-world at http://localhost:5000/ that displays a string "Hello World - Subhasis".

2. Displays the list of authors and the count of their posts by fetching data from [https://jsonplaceholder.typicode.com/users](https://jsonplaceholder.typicode.com/users) and [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts) in the address http://localhost:5000/authors.

3. Sets a simple cookie (if it has not already been set) at http://localhost:5000/setcookie with the values: username=Subhasis Martha and age=19.

4. Fetches the set cookie with http://localhost:5000/getcookies and displays the stored key-values in it.

5. Denies requests to http://localhost:5000/robots.txt page with an error message.

6. Render a HTML page at http://localhost:5000/html.

7. Accepts a string as input at http://localhost:5000/input which sends the data as POST to the same endpoint and prints the submitted string in stdout and the page.


## Built With

* [Flask](https://github.com/pallets/flask) - micro web framework written in Python
* [HTML5](https://github.com/h5bp/html5-boilerplate) -  markup language used for structuring and presenting content on the World Wide Web

## Contributing

Please read [CONTRIBUTING.md](https://github.com/subhasis10/hpdf1/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Subhasis Martha** - *Initial work* - [subhasis10](https://github.com/subhasis10)

List of [contributors](https://github.com/subhasis10/hpdf1/contributors) who participated in this project.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details
