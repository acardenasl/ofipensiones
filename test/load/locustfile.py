from locust import HttpUser, task, between, tag

# Usuario con comportamiento normal: menos de 100 peticiones por minuto
class NormalUser(HttpUser):
    wait_time = between(0.6, 0.7)  # Aproximadamente 100 peticiones por minuto

    @tag("payments")
    @task
    def normal_behavior_payment_receipt(self):
        self.client.get("/api/payment_receipts/")

    @tag("bills")
    @task
    def normal_behavior_bills(self):
        self.client.get("/api/bills/")

# Usuario con comportamiento malicioso: más de 100 peticiones por minuto
class MaliciousUser(HttpUser):
    wait_time = between(0.1, 0.2)  # Mucho más de 100 peticiones por minuto

    @task
    def malicious_behavior(self):
        self.client.get("/api/payment_receipts/")
