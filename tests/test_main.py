def test_register(client):
    res = client.post("/register", json={"username": "newuser", "email": "new@t.com", "password": "pass123"})
    assert res.status_code == 201

def test_register_duplicate(client):
    client.post("/register", json={"username": "dupuser", "email": "dup@t.com", "password": "pass"})
    res = client.post("/register", json={"username": "dupuser", "email": "dup2@t.com", "password": "pass"})
    assert res.status_code == 400

def test_login(client):
    client.post("/register", json={"username": "loginuser", "email": "l@t.com", "password": "pass123"})
    res = client.post("/login", json={"username": "loginuser", "password": "pass123"})
    assert res.status_code == 200
    assert "access_token" in res.json()

def test_login_wrong_password(client):
    client.post("/register", json={"username": "wrongpass", "email": "wp@t.com", "password": "correct"})
    res = client.post("/login", json={"username": "wrongpass", "password": "wrong"})
    assert res.status_code == 400

def test_create_task(auth_client):
    res = auth_client.post("/tasks/", json={"title": "Test Task", "description": "Desc"})
    assert res.status_code == 201
    assert res.json()["title"] == "Test Task"

def test_get_tasks(auth_client):
    res = auth_client.get("/tasks/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_task_by_id(auth_client):
    created = auth_client.post("/tasks/", json={"title": "Single", "description": "D"}).json()
    res = auth_client.get(f"/tasks/{created['id']}")
    assert res.status_code == 200
    assert res.json()["id"] == created["id"]

def test_complete_task(auth_client):
    created = auth_client.post("/tasks/", json={"title": "Complete Me", "description": "D"}).json()
    res = auth_client.put(f"/tasks/{created['id']}", json={"completed": True})
    assert res.status_code == 200
    assert res.json()["completed"] is True

def test_filter_completed(auth_client):
    res = auth_client.get("/tasks/?completed=true")
    assert res.status_code == 200
    assert all(t["completed"] for t in res.json())

def test_delete_task(auth_client):
    created = auth_client.post("/tasks/", json={"title": "Delete Me", "description": "D"}).json()
    res = auth_client.delete(f"/tasks/{created['id']}")
    assert res.status_code == 200

def test_task_not_found(auth_client):
    res = auth_client.get("/tasks/99999")
    assert res.status_code == 404

def test_pagination(auth_client):
    res = auth_client.get("/tasks/?skip=0&limit=2")
    assert res.status_code == 200
    assert len(res.json()) <= 2

def test_unauthorized_access(client):
    res = client.get("/tasks/")
    assert res.status_code == 401
