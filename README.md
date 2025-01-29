# RoadSim
RoadSim a simulation of traffic management system using PyGame, wich models the movement, turning, and stopping of vehicles and pedestrians through an intersection controlled by traffic 


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/OssianGH/road-sim.git
    cd road-sim
    ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
    ```sh
    pip install pygame
    ```

## Usage

To run the simulation, execute the following command:
```sh
python main.py
```

## Modules

### Controller

- `controller/principal.py`: Main controller that initializes and runs the simulation using the following methods:
  - `handle_events`: Processes PyGame events like quitting the application and timer events for the counter.
  - `update`: Updates the state of vehicles, pedestrians, and traffic lights.
  - `render`: Draws the updated state to the screen.
- `controller/controller_contador.py`: Manages a timer that increments every second and changes traffic light colors at specific intervals.
- `controller/controller_semaforos.py`: Manages the state of vehicle traffic lights.
- `controller/controller_vehiculos.py`: Manages vehicle generation and movement.
- `controller/controller_semaforos_peaton.py`: Manages the state of pedestrian traffic lights.
- `controller/controller_peatones.py`: Manages pedestrian generation, movement, and animation.

### Model

- `model/contador.py`: Represents a counter.
- `model/semaforo_estado.py`: Defines the states and transitions for vehicle traffic lights.
- `model/semaforo.py`: Represents a vehicle traffic light.
- `model/vehiculo.py`: Represents a vehicle.
- `model/semaforo_peaton.py`: Represents a pedestrian traffic light.
- `model/peaton.py`: Represents a pedestrian.

### View

- `view/calles.py`: Handles the graphical representation of the streets, vehicles, pedestrians, and traffic lights.
