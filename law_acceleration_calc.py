def get_force(m, a):
    return m * a

def get_mass(f, a):
    return f / a

def get_acceleration(f, m):
    return f / m

objective = input("Quantity to be calculated (Force, Mass, Acceleration): ")

if objective == "force":
    mass = float(input("Enter object's mass (kg): "))
    acceleration = float(input("Enter object's acceleration (m/s^2): "))
    print("The force applied on object is " + str(get_force(mass, acceleration)) + " N.")
elif objective == "mass":
    force = float(input("Enter force applied (N): "))
    acceleration = float(input("Enter object's acceleration (m/s^2): "))
    print("The mass of the object is " + get_mass(force, acceleration) + " kg.")
else:
    force = float(input("Enter force applied (N): "))
    mass = float(input("Enter object's mass (kg): "))
    print("The acceleration of the object is " + get_acceleration(force, mass) + " m/s^2.")
