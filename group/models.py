from django.db import models
from django.urls import reverse


class Child(models.Model):
    name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    age = models.IntegerField()
    hobbies = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    disorder = models.CharField(max_length=200)
    solution = models.CharField(max_length=200)
    risk_level = models.IntegerField()
    icon =models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.full_name} {self.age} {self.hobbies} {self.disorder} {self.solution} {self.risk_level}"














# from django.db import models
# from django.urls import reverse
#
#
# class Child(models.Model):
#     name = models.CharField(max_length=200)
#     age = models.IntegerField()
#     hobbies = models.TextField()
#     picture = models.TextField()
#
#     def __str__(self):
#         return f"{self.name} {self.age} {self.hobbies} {self.picture}"
#
#     def get_absolute_url(self):
#         return reverse("group:detail", args=(self.id,))
#
#
# # class Solution(models.Model):
# #     info = models.CharField(max_length=200)
# #
# #     def __str__(self):
# #         return f"{self.info}"
#
#
# class Disorder(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     # solution = models.ForeignKey(Solution, on_delete=models.CASCADE, related_name= "disorders")
#     symptom = models.TextField()
#
#     def __str__(self):
#         return f"{self.name} {self.symptom}"
#
#
# class ChildDisorder(models.Model):
#     solution = models.CharField(max_length=200)
#     disorder = models.ForeignKey(Disorder, on_delete=models.CASCADE, related_name="children")
#     child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="disorders")
#     risk_level = models.IntegerField()
#
#     class Meta:
#         unique_together = (
#             ("disorder", "child"),
#         )
#
#     def __str__(self):
#         return f"{self.child} {self.disorder} {self.solution} {self.risk_level}"
#

















# from django.db import models
# from django.urls import reverse
#
#
# class Child(models.Model):
#     name = models.CharField(max_length=200)
#     age = models.IntegerField()
#     hobbies = models.TextField()
#     picture = models.TextField()
#
#     def __str__(self):
#         return f"{self.name} {self.age} {self.hobbies} {self.picture}"
#
#     def get_absolute_url(self):
#         return reverse("group:detail", args=(self.id,))
#
#
# # class Solution(models.Model):
# #     info = models.CharField(max_length=200)
# #
# #     def __str__(self):
# #         return f"{self.info}"
#
#
# class Disorder(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     # solution = models.ForeignKey(Solution, on_delete=models.CASCADE, related_name= "disorders")
#     symptom = models.TextField()
#
#     def __str__(self):
#         return f"{self.name} {self.symptom}"
#
#
# class ChildDisorder(models.Model):
#     solution = models.CharField(max_length=200)
#     disorder = models.ForeignKey(Disorder, on_delete=models.CASCADE, related_name="children")
#     child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="disorders")
#     risk_level = models.IntegerField()
#
#     class Meta:
#         unique_together = (
#             ("disorder", "child"),
#         )
#
#     def __str__(self):
#         return f"{self.child} {self.disorder} {self.solution} {self.risk_level}"
#
