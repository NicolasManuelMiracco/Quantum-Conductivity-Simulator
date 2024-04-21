import math
import random

class MyQubit:
    def __init__(self, alpha, beta):
        if abs(alpha**2 + beta**2 - 1) > 1e-6:
            raise ValueError("Invalid qubit state: amplitudes must normalize to 1")
        self.alpha = alpha
        self.beta = beta

    def apply_hadamard(self):
        inv_sqrt2 = 1 / math.sqrt(2)
        new_alpha = inv_sqrt2 * (self.alpha + self.beta)
        new_beta = inv_sqrt2 * (self.alpha - self.beta)
        self.alpha, self.beta = new_alpha, new_beta

    def get_alpha(self):
        return self.alpha

    def get_beta(self):
        return self.beta

    def get_conductivity_probability(self):
        return self.alpha**2


class MyAtom:
    def __init__(self, num_electrons):
        self.num_electrons = num_electrons
        self.electrons = []
        for _ in range(num_electrons):
            theta = random.uniform(0, math.pi)
            alpha = math.cos(theta / 2)
            beta = math.sin(theta / 2)
            self.electrons.append(MyQubit(alpha, beta))

    def get_conductivity_probability(self):
        total_probability = sum(electron.get_conductivity_probability() for electron in self.electrons)
        return total_probability / self.num_electrons

    def get_num_electrons(self):
        return self.num_electrons


class Semiconductor:
    def __init__(self, num_carbon, num_silicon, num_germanium=0):  # Add germanium
        self.atoms = [MyAtom(6) for _ in range(num_carbon)] + \
                     [MyAtom(14) for _ in range(num_silicon)] + \
                     [MyAtom(32) for _ in range(num_germanium)]  # 32 electrons for germanium

    def calculate_required_electrons(self):
        cumulative_probability = 1.0
        num_electrons = 0

        for atom in self.atoms:
            cumulative_probability *= atom.get_conductivity_probability()
            num_electrons += atom.get_num_electrons()

            if cumulative_probability < 1e-6:
                raise RuntimeError("Electron unlikely to reach the end due to low conductivity.")

            if cumulative_probability < 0.01:
                additional_electrons = 10
                num_electrons += additional_electrons
                cumulative_probability = 1.0

        return num_electrons

if __name__ == "__main__":
    sc1 = Semiconductor(6000, 50000)
    conductivity1 = sc1.calculate_required_electrons()
    print("Result (Semiconductor 1):", conductivity1)

    sc2 = Semiconductor(0, 10000, 8000)  # Second semiconductor
    conductivity2 = sc2.calculate_required_electrons()
    print("Result (Semiconductor 2):", conductivity2)
    
    conductivity_ratio = conductivity1 / conductivity2
    print("Conductivity Ratio (Semiconductor 1 / Semiconductor 2):", conductivity_ratio)