
# FastAPI Student CRUD API

A FastAPI application that supports full CRUD (Create, Read, Update, Delete) operations for managing student data.

Developed collaboratively by **Chandrakant Majumdar** and **Saima**.

---

## 🔧 How to Set Up the Project on Any Machine

Follow the steps below to set up and run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/Chandrakant-Majumdar/fastAPI_CRUD_Excercise.git
cd fastAPI_CRUD_Excercise
````

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
fastapi dev main.py
```

Visit the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🚀 Project Features

* Add a new student
* Retrieve student details by ID
* Update student information
* Delete a student
* Root endpoint displaying available endpoints and contributors

---

## ⚙️ Developer Setup History

### 🔹 Chandrakant's Setup

* Initialized Git repository and project folder structure
* Created and switched to `dev/chandrakant` branch
* Set up Python virtual environment
* Installed FastAPI with:

  ```bash
  pip install "fastapi[standard]"
  ```
* Created `.gitignore` and added environment folder
* Added initial `POST` and `GET` endpoints
* Saved dependencies:

  ```bash
  pip freeze > requirements.txt
  ```
* Pushed branch to GitHub and opened pull request

### 🔹 Saima's Setup

* Cloned the repository:

  ```bash
  git clone https://github.com/Chandrakant-Majumdar/fastAPI_CRUD_Excercise.git
  cd fastAPI_CRUD_Excercise
  ```

* Checked out a new branch:

  ```bash
  git checkout -b dev/saima
  ```

* Created and activated her own virtual environment:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

* Installed dependencies from `requirements.txt`:

  ```bash
  pip install -r requirements.txt
  ```

* Added the following API endpoints:

  * `PUT /students/{student_id}` – Update student
  * `DELETE /students/{student_id}` – Delete student
  * `GET /` – Root API metadata

* Committed and pushed changes:

  ```bash
  git add .
  git commit -m "Added update, delete, and root endpoints"
  git push origin dev/saima
  ```

* Merged changes via pull request

---

## 📘 API Endpoints

| Method | Endpoint                 | Description                   |
| ------ | ------------------------ | ----------------------------- |
| POST   | `/students/{student_id}` | Create a new student          |
| GET    | `/students/{student_id}` | Retrieve student by ID        |
| PUT    | `/students/{student_id}` | Update student information    |
| DELETE | `/students/{student_id}` | Delete student by ID          |
| GET    | `/`                      | View API overview and authors |

### 📎 Example Request Body (POST / PUT)


---

## 🛠 Git Workflow Summary

```bash
# Chandrakant
git checkout -b dev/chandrakant
git add .
git commit -m "Initial commit with create and read endpoints"
git push origin dev/chandrakant

# Saima
git clone https://github.com/Chandrakant-Majumdar/fastAPI_CRUD_Excercise.git
cd fastAPI_CRUD_Excercise
git checkout -b dev/saima
git add .
git commit -m "Added update, delete, and root endpoints"
git push origin dev/saima

# Final merge via GitHub pull request
