def get_force(m, a):
    """Force = mass * acceleration"""
    return m * a

def get_mass(f, a):
    """Mass = force / acceleration"""
    return f / a

def get_acceleration(f, m):
    """Acceleration = force / mass"""
    return f / m

print("Type the assigned number of your requested quantity.")
print("Inputs are case-sensitive. Please enter in lowercase.")
objective = input("Force (1), Mass (2), Acceleration (3): ")

if objective == "1": # Calculates force applied
    mass = float(input("Mass (kg): "))
    acceleration = float(input("Acceleration (m/s^2): "))
    direction = input("Direction of Acceleration (Right/Left): ")
    force = get_force(mass, acceleration)
    if direction == "left":
        force = -force
    print("Force: " + str(force) + " N.")
elif objective == "2": # Calculates object's mass
    force = float(input("Force (N): "))
    acceleration = float(input("Acceleration (m/s^2): "))
    mass = get_mass(force, acceleration)
    print("Mass: " + str(mass) + " kg.")
elif objective == "3": # Calculates object's acceleration
    force = float(input("Force: (N): "))
    mass = float(input("Mass: (kg): "))
    direction = input("Direction of Force (Right/Left): ")
    acceleration = get_acceleration(force, mass)
    if direction == "left":
        acceleration = -acceleration
    print("Acceleration: " + str(acceleration) + " m/s^2.")
else:
    print("Error: Unrecognized Request.")