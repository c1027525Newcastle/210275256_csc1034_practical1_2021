from . import panda

import argparse

def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate",help="Suppress Rotation",
                        action="store_true")

    parser.add_argument("--scale", help="Increase Scale",
                        type=int, required=False, default=1) ###python walking_panda.py --scale 7 (have to write this in terminal)

    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
