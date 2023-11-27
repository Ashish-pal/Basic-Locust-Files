from locust import User, task, between, TaskSet, SequentialTaskSet


class SearchProduct(SequentialTaskSet):
    @task
    def search_men_products(self):
        print("searching mens product")

    @task
    def search_kids_products(self):
        print("searching kids product")

    @task
    def exit_task(self):
        self.interrupt()


class ViewCart(SequentialTaskSet):
    @task
    def get_all_cart_items(self):
        print("searching mens product")

    @task
    def search_cart_items(self):
        print("searching kids product")

    @task
    def exit_task(self):
        self.interrupt()


class MyUser(User):
    wait_time = between(1, 2)
    # tasks = [SearchProduct, ViewCart]

    tasks = {
        SearchProduct: 4,
        ViewCart: 1
    }
