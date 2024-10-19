from django.db import models
from datetime import timedelta



class Institution(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    address = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=32)
    subsection = models.CharField(max_length=4)

    def __str__(self) -> str:
        return self.name


class GradeTerm(models.Model):
    name = models.CharField(max_length=32)
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    DNI = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    school = models.ForeignKey(Institution, on_delete=models.DO_NOTHING)
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class TermPayment(models.Model):
    term = models.ForeignKey(GradeTerm, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)

    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ("term", "student")

    def __str__(self) -> str:
        return f"{self.student} - {self.term}"


class OfipensionesLog(models.Model):
    operation_name = models.CharField(max_length=32)
    time_taken = models.DurationField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self) -> str:
        return f"{self.operation_name} - {self.timestamp}"
    
class Factura(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()

    def __str__(self) -> str:
        return f"Factura for {self.student} - Total: {self.total_amount}"

    

