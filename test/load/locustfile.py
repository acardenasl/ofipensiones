from locust import HttpUser, tag, task


class LoadPaymentReceiveService(HttpUser):
    @tag("payments")
    @task
    def payment_receipt(self):
        self.client.get("/api/payment_receipts/")

    @tag("bills")
    @task
    def bills(self):
        self.client.get("/api/bills/")
