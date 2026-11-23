import numpy as np
from Parameters import e_type, order

def GaussPoints():
    if e_type == 1:
        if order == 1:
            # Triangle with 1 Gauss integration point

            shi = np.array([1.0 / 3.0])
            eta = np.array([1.0 / 3.0])
            w = np.array([1.0])

        elif order == 2:
            # Triangle with 4 integration points

            shi = np.array([
                1.0 / 3.0,
                3.0 / 5.0,
                1.0 / 5.0,
                1.0 / 5.0
            ])

            eta = np.array([
                1.0 / 3.0,
                1.0 / 5.0,
                3.0 / 5.0,
                1.0 / 5.0
            ])

            w = np.array([
                27.0 / 48.0,
                25.0 / 48.0,
                25.0 / 48.0,
                25.0 / 48.0
            ])

        else:
            raise ValueError(
                f"Unsupported quadrature order for triangle: {order}"
            )

    elif e_type == 2:

        if order == 1:
            # Quadrilateral with 4 Gauss integration points

            shi = np.array([
                np.sqrt(3.0) / 3.0,
                -np.sqrt(3.0) / 3.0
            ])

            eta = shi.copy()

            w = np.array([1.0, 1.0])

        elif order == 2:
            # Quadrilateral with 9 Gauss integration points

            shi = np.array([
                0.0,
                np.sqrt(15.0) / 5.0,
                -np.sqrt(15.0) / 5.0
            ])

            eta = shi.copy()

            w = np.array([
                8.0 / 9.0,
                5.0 / 9.0,
                5.0 / 9.0
            ])

        else:
            raise ValueError(
                f"Unsupported quadrature order for quadrilateral: {order}"
            )

    else:
        raise ValueError(
            f"Unsupported element type: {e_type}"
        )

    return shi, eta, w
