import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import cm

def calculate_capacitance(length, distance, voltage, number_of_points):
  """
  Calculates the capacitance of a parallel plate capacitor using the
  boundary element method.

  Parameters:
  -----------
  length : float
      Length of the plate in meters.
  distance : float
      Distance between the plates in meters.
  voltage : float
      Voltage applied to the plates in volts.
  number_of_points : int
      Number of points used to discretize the plate surface.

  Returns:
  --------
  capacitance : float
      The capacitance of the parallel plate capacitor in farads.
  """
  delta = length / number_of_points
  epsilon_0 = 8.8541878176e-12

  # Generating the coordinates of the plate points
  x = np.zeros(2 * number_of_points ** 2)
  y = np.zeros(2 * number_of_points ** 2)
  number_of_points_used = 0
  for i in range(2):
    for j in range(number_of_points):
      for k in range(number_of_points):
        if not (j > number_of_points / 2 and k > number_of_points / 2):
          x[number_of_points_used] = delta * (j + 1 - 0.5)
          y[number_of_points_used] = delta * (k + 1 - 0.5)
          number_of_points_used += 1
  z = np.zeros(number_of_points_used)
  for n in range(int(number_of_points_used / 2)):
    z[n] = 0
    z[n + int(number_of_points_used / 2)] = distance

  # Generating the voltage column vector V
  V = np.zeros(number_of_points_used)
  for i in range(int(number_of_points_used / 2)):
    V[i] = voltage
    V[i + int(number_of_points_used / 2)] = 0

  # Generating the impedance matrix Z
  Z = np.zeros((number_of_points_used, number_of_points_used))
  for i in range(number_of_points_used):
    for j in range(number_of_points_used):
      if i == j:
        Z[i, j] = (delta / (np.pi * epsilon_0)) * np.log(1 + sqrt(2))
      else:
        R = sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2)
        Z[i, j] = (1 / (4 * np.pi * epsilon_0)) * ((delta ** 2) / R)

  # Solving the linear system Z * A = V
  A = np.linalg.solve(Z, V)

  # Calculating the total charge by summing the charge distributions
  total_charge = sum(A) * (delta ** 2)
  # Calculating the capacitance
  capacitance = abs(total_charge) / voltage

  return capacitance
