# DesafioPrevisao

# Overview

Challenge to build an api with flask to export the weather forecast

# Setup

```
python -m venv .venv
```

```
.\.venv\Scripts\activate
```

```
pip install -r requirements.txt
```

Run app
```
python app.py
```

Run Tests
```
python tests.py
```

# Architecture

MVC ( Model-View-Controller )

<h2>Code structure</h2>

```
├── application
├── Previsao
│   ├── models.py (Model)
│   ├── resources.py (Controller)
│   └── schemas.py (View)
├── app.py (Controller)
├── requirements.txt
├── dao.py
├── cache.py
├── requirements.txt
└── test.py
```

<h2> Real test with Postman </h2>

https://documenter.getpostman.com/view/20045494/UVysxvVt
