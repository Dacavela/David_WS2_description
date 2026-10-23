# David WS2 — Differential Drive Mobile Robot

## Workshop 2 — Mobile Robotics

### Descripción

Este proyecto implementa la simulación de un robot móvil de tracción diferencial utilizando **ROS 2 Jazzy y Gazebo Sim**.

El robot fue modelado en SolidWorks y exportado al formato URDF/Xacro para su integración con ROS 2.

El objetivo del taller es implementar el movimiento de un robot diferencial y realizar una trayectoria con forma del número **7**.

## Características

- Modelo 3D del robot mediante archivos STL.
- Descripción del robot mediante URDF/Xacro.
- Simulación física en Gazebo Sim.
- Control diferencial mediante el plugin DiffDrive.
- Comunicación ROS 2–Gazebo mediante `ros_gz_bridge`.
- Control de movimiento mediante Python y el tópico `/cmd_vel`.

## Estructura del proyecto

- `urdf/`: descripción del robot, articulaciones, materiales y configuración de Gazebo.
- `meshes/`: modelos STL del robot.
- `launch/`: archivos para iniciar la simulación.
- `config/`: archivos de configuración.
- `scripts/trayectoria_7.py`: programa de movimiento del robot.

## Trayectoria del número 7

La trayectoria programada comprende tres etapas:

1. Movimiento rectilíneo de 1 metro.
2. Giro horario de aproximadamente 135°.
3. Movimiento rectilíneo de aproximadamente 1.414 metros.

Las velocidades y los tiempos de giro pueden ajustarse de acuerdo con el comportamiento del robot en la simulación.

## Requisitos

- Ubuntu
- ROS 2 Jazzy
- Gazebo Sim
- `ros_gz_sim`
- `ros_gz_bridge`
- `robot_state_publisher`
- `xacro`
- Python 3 y `rclpy`

## Instalación

Clonar el repositorio dentro de un espacio de trabajo ROS 2:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone URL_DEL_REPOSITORIO
```

Compilar:

```bash
cd ~/ros2_ws
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash
```

## Ejecución

### Terminal 1 — Iniciar Gazebo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch David_WS2_description gazebo.launch.py
```

### Terminal 2 — Comunicación de velocidades

Comprobar primero si el bridge ya está suscrito a `/cmd_vel`:

```bash
ros2 topic info /cmd_vel -v
```

Si no hay un bridge para ese tópico, ejecutarlo:

```bash
ros2 run ros_gz_bridge parameter_bridge \
'/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist'
```

### Terminal 3 — Ejecutar la trayectoria

```bash
source ~/ros2_ws/install/setup.bash
python3 ~/ros2_ws/src/David_WS2_description/scripts/trayectoria_7.py
```

## Video de demostración

La ejecución del robot en Gazebo Sim puede observarse en el siguiente video:

**[Ver simulación en YouTube](PEGAR_AQUI_ENLACE_DE_YOUTUBE)**

## Tecnologías utilizadas

- ROS 2 Jazzy
- Gazebo Sim
- Python
- URDF / Xacro
- SolidWorks

## Autor

David — Workshop 2, Robots Móviles.

