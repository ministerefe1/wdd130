class WaterFlow:
    # Constants
    GRAVITY_ACCELERATION = 9.80665  # m/s^2
    WATER_DENSITY = 998.2  # kg/m^3
    WATER_VISCOSITY = 0.0010016  # kg/(ms)
  
    def __init__(self, tower_height, tank_height):
        self.tower_height = tower_height
        self.tank_height = tank_height

    def water_column_height(self):
        h = self.tower_height + (3 * self.tank_height / 4)
        return h

    def pressure_gain_from_water_height(self, height):
        water_density = 998.2
        earths_gravity = 9.80665
        pressure = (water_density * earths_gravity * height) / 1000
        return pressure

    def pressure_loss_from_pipe(self, pipe_diameter, pipe_length, friction_factor, fluid_velocity):
        water_density = 998.2
        pressure_loss = -(friction_factor * pipe_length * water_density * fluid_velocity**2) / (2000 * pipe_diameter)
        return pressure_loss

    def pressure_loss_from_fittings(self, fluid_velocity, quantity_fittings):
        pressure_loss = (-0.04 * self.WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000
        return pressure_loss

    def reynolds_number(self, hydraulic_diameter, fluid_velocity):
        reynolds_number = (self.WATER_DENSITY * hydraulic_diameter * fluid_velocity) / self.WATER_VISCOSITY
        return reynolds_number

    @staticmethod
    def pressure_in_psi(pressure_kpa):
        psi = pressure_kpa * 0.14503773773375  # 1 kPa = 0.14503773773375 psi
        return psi

    def calculate_k(self, Reynolds_number, D, d):
        k = 0.1 + (50 / Reynolds_number) * (D / d)**(4 / 3 - 1)
        return k

    def pressure_loss_from_pipe_reduction(self, Reynolds_number, D, d, velocity):
        k = self.calculate_k(Reynolds_number, D, d)
        pressure_loss = -(k * self.WATER_DENSITY * velocity**2) / 2000
        return pressure_loss

    PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
    PVC_SCHED80_FRICTION_FACTOR = 0.013 # (unitless)
    SUPPLY_VELOCITY = 1.65 # (meters / second)

    HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
    HDPE_SDR11_FRICTION_FACTOR = 0.018 # (unitless)
    HOUSEHOLD_VELOCITY = 1.75 # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    wv = WaterFlow(tower_height, tank_height)

    water_height = wv.water_column_height()
    pressure = wv.pressure_gain_from_water_height(water_height)

    diameter = WaterFlow.PVC_SCHED80_INNER_DIAMETER
    friction = WaterFlow.PVC_SCHED80_FRICTION_FACTOR
    velocity = WaterFlow.SUPPLY_VELOCITY
    reynolds = wv.reynolds_number(diameter, velocity)
    loss = wv.pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = wv.pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = wv.pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, WaterFlow.HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = WaterFlow.HDPE_SDR11_INNER_DIAMETER
    friction = WaterFlow.HDPE_SDR11_FRICTION_FACTOR
    velocity = WaterFlow.HOUSEHOLD_VELOCITY
    loss = wv.pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()

