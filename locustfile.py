from locust import HttpUser, task, events


class MyUser(HttpUser):

    @task
    def checkJioEndpoint(self):
        response = self.client.get('/')
        assert response.status_code == 200


