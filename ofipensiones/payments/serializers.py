from rest_framework import serializers
from .models import TermPayment
from .models import Bill


class PaymentReceiptSerializer(serializers.ModelSerializer):
    student_info = serializers.SerializerMethodField()
    school_info = serializers.SerializerMethodField()

    class Meta:
        model = TermPayment
        fields = [
            "student_info",
            "school_info",
            "amount",
            "due_date",
        ]

    def get_student_info(self, obj):
        return {
            "DNI": obj.student.DNI,
            "name": str(obj.student),
            "grade": obj.student.grade.name,
        }

    def get_school_info(self, obj):
        return {
            "name": obj.student.school.name,
            "city": obj.student.school.city,
            "address": obj.student.school.address,
        }


class BillSerializer(serializers.ModelSerializer):
    student_info = serializers.SerializerMethodField()

    class Meta:
        model = Bill
        fields = [
            "student_info",
            "total_amount",
            "due_date",
        ]

    def get_student_info(self, obj):
        return {
            "DNI": obj.student.DNI,
            "name": str(obj.student),
            "grade": obj.student.grade.name,
        }
