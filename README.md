# Quantum-Conductivity-Simulator

One-line description: Python module for simulating conductivity in semiconductors using quantum qubit principles.

Summary: This Python script models quantum states of electrons as qubits in atoms within semiconductors. It uses the classes `MyQubit` and `MyAtom` to represent quantum states and atomic configurations. Each `MyAtom` instance contains a number of `MyQubit` electrons, initialized with random quantum states. The main class, `Semiconductor`, aggregates these atoms and calculates the required number of electrons to achieve a specified conductivity probability threshold. It considers additional electrons to maintain conductivity above a critical threshold, simulating different materials like carbon, silicon, and optionally germanium. This simulation is useful for understanding quantum effects in semiconductor physics and comparing conductivity between different semiconductor configurations.
