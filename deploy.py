import argparse
import os
import helpers

parser = argparse.ArgumentParser(description='Deploy Stack')
parser.add_argument('-r', '--remove', action='store_true', help="remove stack")
parser.add_argument('-k', '--kubernetes', action='store_true', help="Deploy to kubernetes")

stack = 'apachephp'

args = parser.parse_args()

if args.remove:
    command = 'docker stack rm '
    if args.kubernetes:
        command += '--orchestrator=kubernetes '
    os.system(command + stack)
else:
    # deploy composer file into swarm
    os.environ.update(helpers.dot_env_vars('.env'))
    command = 'docker stack deploy --compose-file docker-compose.yml '
    if args.kubernetes:
        command += '--orchestrator=kubernetes '
    os.system(command + stack)