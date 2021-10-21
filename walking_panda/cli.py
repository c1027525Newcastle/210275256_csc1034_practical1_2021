from . import panda

import argparse

def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")

    parser.add_argument("--no-rotate", help="Suppress Rotation",
                        action="store_true")

    parser.add_argument("--scale", help="Change Scale of the Panda",
                        type=float, required=False, default=1)

    parser.add_argument("--environmentscale", help="Change Scale of the Environment",
                        type=float, required=False, default=1)

    parser.add_argument("--pandaBaby", help="Add an extra baby panda on top of the main panda",
                        action="store_true")
    parser.add_argument("--pandaArmy", help="Add 10 more Pandas",
                        action="store_true")

    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
