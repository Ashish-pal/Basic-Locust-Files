from locust import User, task, between


class MyUser(User):
    wait_time = between(1, 2)

    @task
    def my_task1(self):
        print("Executing task1")

    @task
    def my_task2(self):
        print("Executing task2")
