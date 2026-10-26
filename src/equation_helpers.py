import numpy as np

def magnetic_force(charge, velocity, magnetic_field):
    """
    This function calculates the magnetic force on a charged particle moving in a 
    magnetic field using the Lorentz force equation: F = q * (v x B).
    """
    return charge * np.cross(velocity, magnetic_field)

def larmor_radius(mass, velocity, charge, magnetic_field_strength):
    """
    This function calculates the Larmor radius of a charged particle moving in a 
    magnetic field.
    """
    return (mass * velocity) / (charge * magnetic_field_strength)
