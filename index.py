# One to Many #
from classes.models import Car, Garage

# Many to Many #
from classes.models import Doctor, Patient, Appointment

# HARD MODE # (You may need to make more models to make this work!)
from classes.models import Student, Enrollment, Course

# SEED DATA GOES BELOW

g1 = Garage(address="11 Broadway")
g2 = Garage(address="123 Mean Street")

c1 = Car(make="BMW", model="X6", license_plate="VROOM", garage=g1)
c2 = Car(make="BMW", model="E30", license_plate="V FAST", garage=g2)
c3 = Car(make="Mercedes", model="GLE", license_plate="BALLIN", garage=g1)
c4 = Car(make="Audi", model="R8", license_plate="BOOLIN", garage=g2)

# doctors / patients / appointments

d1 = Doctor(name="Dre", specialty="beats")
d2 = Doctor(name="Lee", specialty="dentist")

p1 = Patient(first_name="Scooby", last_name="Doo")
p2 = Patient(first_name="Scrappy", last_name="Doo")

a1 = Appointment(doctor=d1, patient=p1)
a2 = Appointment(doctor=d1, patient=p2)
a3 = Appointment(doctor=d2, patient=p1)
a4 = Appointment(doctor=d2, patient=p1)