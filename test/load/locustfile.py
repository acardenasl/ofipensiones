from locust import HttpUser, task


class LoadPaymentReceiveService(HttpUser):
    @task
    def payment_receipt(self):
        pass

    @task
    def healthcheck(self):
        """
        DELETE ME
        """
        self.client.get("/facturas")
