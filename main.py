""""Создать API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа.
"""


# from typing import Optional
# from fastapi import FastAPI, HTTPException
# import uvicorn
# from pydantic import BaseModel

# app = FastAPI()




# tasks = []
# class Task(BaseModel):
#     id: int
#     title: str
#     description: Optional[str]
#     status: str


# class TaskInn(BaseModel):
#     title: str
#     description: Optional[str]
#     status: str


# @app.get('/tasks/', response_model= list[Task])
# async def root():
#     return tasks


# @app.post('/tasks/', response_model= Task)
# async def create_task(new_task: TaskInn):
#     tasks.append(Task(id= len(tasks)+1), title= new_task.title, description= new_task.description, status = new_task.status)
#     return tasks


# @app.put('/tasks/', response_model= list[Task])
# async def edit_task(task_id: int, new_task: TaskInn):
#     for i in range(0, len(tasks)):
#         if tasks[i].id == task_id:
#             curent_task = tasks[task_id - 1]
#             curent_task.title = new_task.title
#             curent_task.description = new_task.description
#             curent_task.status = new_task.status
#             return curent_task
#     raise HTTPException(status_code=404, detail= 'Task not found')    
    


# @app.delete('/tasks/', response_model= dict)
# async def edit_task(task_id: int):
#     curent_task = None
#     for i in range(0, len(tasks)):
#         if tasks[i].id == task_id:
#             tasks.remove(tasks[i])
#             return {'message': 'task was delited'}
#     raise HTTPException(status_code=404, detail= 'Task not found')    
    


# if __name__ == '__main__':
#     uvicorn.run("__main__:app", host="127.0.0.1", port=8000, reload=True)


"""Создать API для получения списка фильмов по жанру. Приложение должно
иметь возможность получать список фильмов по заданному жанру.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Movie с полями id, title, description и genre.
Создайте список movies для хранения фильмов.
Создайте маршрут для получения списка фильмов по жанру (метод GET).
Реализуйте валидацию данных запроса и ответа.
"""

# from typing import Optional
# from fastapi import FastAPI, HTTPException
# import uvicorn
# from pydantic import BaseModel
# from enum import Enum

# app = FastAPI()

# movies = []

# class Genre(Enum):
#     action_movie = 'боевик'
#     fantastic = 'фантатика'
#     horror = 'ужасы'
#     comedy = 'комедия'
    

# class Movie(BaseModel):
#     id: int
#     title: str
#     description: str
#     genre: Genre

# class MovieInn(BaseModel):
#     id: int
#     title: str
#     description: str
#     genre: Genre


# @app.post('/movies/', response_model= Movie)
# async def create_movie(new_movie: MovieInn):
#     movies.append(Movie(id= len(movies)+1), title= new_movie.title, description= new_movie.description, genre = new_movie.genre)
#     return movies[-1]


# @app.get('/movies/{genre}', response_model= list[Movie])
# async def get_movies(genre: str):
#     result = []
#     for movie in movies:
#         if movie.genre == genre:
#             result.append(movie)
#     return result



# if __name__ == '__main__':
#     uvicorn.run("__main__:app", host="127.0.0.1", port=8000, reload=True)


"""Создать веб-страницу для отображения списка пользователей. Приложение
должно использовать шаблонизатор Jinja для динамического формирования HTML
страницы.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
содержать заголовок страницы, таблицу со списком пользователей и кнопку для
добавления нового пользователя.
Создайте маршрут для отображения списка пользователей (метод GET).
Реализуйте вывод списка пользователей через шаблонизатор Jinja.
"""

from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel
from enum import Enum

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []

class UserOut(BaseModel):
    id: int
    name : str
    email : str


class UserInn(BaseModel):
    name: str
    email: str
    password : str

class User(UserInn):
    id: int


for i in range(10):
    users.append(User(
        id = i+1,
        name = f'{i + 1}',
        email = f'email{i + 1}@mail.ru',
        password = '123'
    ))


@app.get('/users/', response_model= HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse('users.html',{'request': Request, 'users': users})



# if __name__ == '__main__':
#     uvicorn.run("__main__:app", host="127.0.0.1", port=8000, reload=True)

