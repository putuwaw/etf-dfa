# ETF-DFA

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![Forks](https://img.shields.io/github/forks/putuwaw/etf-dfa?style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/putuwaw/etf-dfa?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/putuwaw/etf-dfa?style=for-the-badge)

ETF-DFA is a website based string checker using Extended Transition Function for Deterministic Finite Automata.

## Features💡
By using ETF-DFA you can:
- [x] Checks whether a string is accepted by the language or not.
- [x] Get details of the ETF process for DFA.
- [x] Get transition diagram images of each language.

## Technology 👨‍💻
ETF-DFA is created using:
- [Python](https://www.python.org/) - 
Python as the main programming language.
- [HTML](https://www.w3.org/html) - HTML is the fundamental markup language for webpages.
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Flask is a web framework for Python, based on the Werkzeug toolkit.
- [Bootstrap](https://getbootstrap.com/) - Bootstrap is a front-end framework that allows for the creation of easy and responsive web layouts.
- [Heroku](https://www.heroku.com/) - Heroku is a platform as a service (PaaS) that we use to deploy our apps.


## Structure 📂
```
ETF-DFA
├── .github
├── docs
├── handlers
├── modules
├── static
│   ├── images
│   ├── scripts
│   └── styles
├── templates
├── tests
├── .gitignore
├── LICENSE
├── Procfile
├── README.md
├── app.py
└── requirements.txt
```
- [.github](.github/) is a folder that used to place Github related stuff, like PR template and CI pipeline.
- [docs](docs/) contain documentation of this app.
- [handlers](handlers/) contain handler to handling HTTP request methods, especially POST method.
- [modules](modules/) contain the main modules for each language.
- [static](static/) contain static files like images, CSS, and JavaScript files.
- [templates](templates/) contain the file that will be rendered for display in the browser.
- [tests](tests/) contain unit test to make sure the main module work properly.
- [.gitignore](.gitignore) is a file to exclude some folders like venv.
- [LICENSE](LICENSE) is a file that contains the license we use in this app.
- [Procfile](Procfile) is a file that specifies the commands that are executed by an Heroku app on startup.
- [README.md](README.md) is the file you are reading now.
- [app.py](app.py) is the main file of this app.
- [requirements.txt](requirements.txt) is a file that contains a list of dependencies used in this app.

## Requirements 📦
- Python 3.10 or later
- HTML 5 or later

## Installation 🛠️
- Clone the repository:
```
git clone https://github.com/putuwaw/etf-dfa.git
```
- Create a virtual environment:
```
python -m venv venv
```
- Activate virtual environment:
```
./venv/Scripts/Activate.ps1
```
- Install dependencies:
```
pip install -r requirements.txt
```
- Run app:
```
python app.py
```
- Run test:
```
pytest
```

## Contributors ✨
<br>
<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/putuwaw"><img src="https://avatars.githubusercontent.com/u/90038606?v=4" width="150px;" alt=""/><br><sub><b>Putu Widyantara</b></sub></td> 
    <td align="center"><a href="https://github.com/KEVINMOSESWALELENG"><img src="https://avatars.githubusercontent.com/u/103045275?v=4" width="150px;" alt=""/><br><sub><b>Kevin Moses</b></sub></td> 
    <td align="center"><a href="https://github.com/Antoniusata12"><img src="https://avatars.githubusercontent.com/u/113809833?v=4" width="150px;" alt=""/><br><sub><b>Antonius Ata</b></sub></td>
    <td align="center"><a href="https://github.com/YogaLaksana"><img src="https://avatars.githubusercontent.com/u/103047470?v=4" width="150px;" alt=""/><br><sub><b>Yoga Laksana</b></sub></td>
  </tr>
</table>