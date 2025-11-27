from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    # Scenario 1: Load Home Page
    @task
    def load_home(self):
        self.client.get("/")

    # Scenario 2: Load Login Page
    @task
    def load_login(self):
        self.client.get("/login")
    