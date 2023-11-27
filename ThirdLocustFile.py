from locust import User, task, between, TaskSet, SequentialTaskSet


class SearchProduct(SequentialTaskSet):
    @task
    def search_men_products(self):
        print("searching mens product")

    @task
    def search_kids_products(self):
        print("searching kids product")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]