import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math


class Trayectoria7(Node):

    def __init__(self):
        super().__init__('trayectoria_7')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        # =====================================
        # PARAMETROS DE LA TRAYECTORIA
        # =====================================

        self.velocidad_lineal = 0.1       # m/s
        self.velocidad_angular = -5.0     # rad/s (giro horario)

        self.distancia_1 = 1.0            # metros
        self.distancia_2 = math.sqrt(2)   # 1.414 metros

        # Tiempo teorico para girar 135 grados:
        # (135 * pi / 180) / 0.3 = 7.85 s
        #
        # Como el robot se atasca cada 90 grados,
        # aumentamos el tiempo de giro.

        self.tiempo_giro = 16.5

    # =====================================
    # PUBLICAR VELOCIDAD
    # =====================================

    def publicar(self, lineal, angular):

        msg = Twist()

        msg.linear.x = float(lineal)
        msg.angular.z = float(angular)

        self.publisher.publish(msg)

    # =====================================
    # DETENER ROBOT
    # =====================================

    def detener(self):

        for _ in range(10):
            self.publicar(0.0, 0.0)
            time.sleep(0.05)

    # =====================================
    # MOVIMIENTO RECTO
    # =====================================

    def avanzar(self, distancia):

        tiempo = distancia / self.velocidad_lineal

        self.get_logger().info(
            f'Avanzando {distancia:.3f} metros'
        )

        inicio = time.monotonic()

        while (
            time.monotonic() - inicio < tiempo
            and rclpy.ok()
        ):

            self.publicar(
                self.velocidad_lineal,
                0.0
            )

            time.sleep(0.05)

        self.detener()
        time.sleep(1.0)

    # =====================================
    # GIRO
    # =====================================

    def girar(self):

        self.get_logger().info(
            f'Girando en sentido horario durante '
            f'{self.tiempo_giro:.2f} segundos'
        )

        inicio = time.monotonic()

        while (
            time.monotonic() - inicio < self.tiempo_giro
            and rclpy.ok()
        ):

            self.publicar(
                0.0,
                self.velocidad_angular
            )

            time.sleep(0.05)

        self.detener()
        time.sleep(1.0)

    # =====================================
    # TRAYECTORIA NUMERO 7
    # =====================================

    def ejecutar(self):

        self.get_logger().info(
            'Iniciando trayectoria del numero 7'
        )

        # Esperar conexion con el bridge
        while (
            self.publisher.get_subscription_count() == 0
            and rclpy.ok()
        ):
            self.get_logger().info(
                'Esperando conexion con Gazebo...'
            )
            time.sleep(0.5)

        time.sleep(1.0)

        # PRIMER MOVIMIENTO
        self.avanzar(self.distancia_1)

        # SEGUNDO MOVIMIENTO
        self.girar()

        # TERCER MOVIMIENTO
        self.avanzar(self.distancia_2)

        self.detener()

        self.get_logger().info(
            'Trayectoria del numero 7 finalizada'
        )


def main():

    rclpy.init()

    robot = Trayectoria7()

    try:
        robot.ejecutar()

    except KeyboardInterrupt:
        pass

    finally:
        robot.detener()
        robot.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
