from locust import User, task, between, TaskSet, SequentialTaskSet, events


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("______Initializing Load Test_________ON Test Start")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("_________Load Test Completed________Test ENDS HERE")


class SearchProduct(SequentialTaskSet):

    def on_start(self):
        print("---Search Product : Task execution starts ---")

    def on_stop(self):
        print("---Search Product : Task execution stops ---")

    @task
    def search_men_products(self):
        print("searching mens product")

    @task
    def search_kids_products(self):
        print("searching kids product")

    @task
    def exit_task(self):
        self.interrupt()


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]

    def on_start(self):
        print("MyUser: Adding new users")

    def on_stop(self):
        print("MyUser: Deleting users")
