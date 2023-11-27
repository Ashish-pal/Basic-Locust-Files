from locust import User, task, between, TaskSet


class SearchProduct(TaskSet):
    @task(4)
    def search_men_products(self):
        print("searching mens product")

    @task(1)
    def search_kids_products(self):
        print("searching kids product")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]
