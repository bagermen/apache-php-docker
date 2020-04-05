import argparse
import os
import helpers

parser = argparse.ArgumentParser(description='Deploy Stack')
parser.add_argument('-r', '--remove', action='store_true')

stack = 'apachephp'

args = parser.parse_args()

if args.remove:
    os.system('docker stack rm ' + stack)
else:
    # deploy composer file into swarm
    os.environ.update(helpers.dot_env_vars('.env'))
    os.system('docker stack deploy --compose-file docker-compose.yml ' + stack)