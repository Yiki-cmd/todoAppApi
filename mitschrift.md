Todo App

- manages tasks for projects
- projects are owned by managers
- tasks are implemented by users
- admins own projects, managers and users
- tasks habe the following properties
  - id
  - description
  - owner [ manager]
  - assigned_to [user]
  - project_id [ which project the task belongs to]
  - created_date
  - updated_date []

- tasjs are created by managers
- projects are created by managers
- tasks ae grouped in projects
- tasks are assigned to users
- users update and read tasks
- admins create users, managers
- admins create projects and assign projects to managers
- admins can delete or update [users, managers, projects and tasks]
-
  
tasks [todos] => [Project] => [ Goal ]

user - use - task implementer [ RU, read and update task]
     - manager - task owner, project owner [ CRUD taske, CRUD project]
     - admin - task owner, user owner, manager owner + user + manager + [ CRUD user, CRUD manager]

=> how to know whether fastapi installed is oder not
        1,* look .venv -> lib
        2, see project.toml -> dependencies -> fast api

to be installed

- uv init
- uv venv --python 3.12
- uv add fastapi
- uv add uvicorn
- uv add python-multipart
- uv add pydantic-settings
- uv add requests
- uv add motor
- uv add beanie
- uv add python-jose[cryptography]
- uv add pyjwt
- uv add passlib
- uv add passlib[bcrypt]
- 




[CONTROLLER/ROUTE/ENDPOINT/API]  [SERVICE]    <->    [REPOSITORY]  <-> [DATABASE]
[databasee agnostic]
does not care about type of database





=> git checkout -b feat/environment - it is completely the copy of the main another branch is making
  main accepts only gut finshed (xfuf)










docker-compose up
docker-compose api built

uvicorn app.main:app --reload --env-file .env


git checkout -b feat/logger







