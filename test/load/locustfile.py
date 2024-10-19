from locust import HttpUser, tag, task


class LoadPaymentReceiveService(HttpUser):
    @tag("payments")
    @task
    def payment_receipt(self):
        self.client.get("/payment_receipts/")

    @tag("biils")
    @task
    def bills(self):
        self.client.get("/bills/")
