import argparse
import os
import sys
import shlex
from subprocess import Popen, PIPE
from helpers import dot_env_vars

sys.dont_write_bytecode=True
current_dir = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(description='Deploy Stack')
parser.add_argument('-r', '--remove', action='store_true', help="remove stack")
parser.add_argument('-k', '--kubernetes', action='store_true', help="Deploy to kubernetes")

stack = 'apachephp'

def check_stack_running(stack):
    command = "docker stack ls --format '{{.Name}}'"
    out, err = Popen(shlex.split(command), stdout=PIPE, stderr=PIPE).communicate()
    stacks = out.strip().decode('utf-8').split(sep='\n')

    return not err and stacks.count(stack) > 0

def get_variables():
    is_windows = sys.platform.startswith('win')
    variables = {'ACTIVE_USER': '0:0'}
    env = dot_env_vars('.env')

    if not is_windows:
        variables['ACTIVE_USER'] = str(os.getuid()) + ':' + str(os.getgid())

    return {**env, **variables}

args = parser.parse_args()

if args.remove:
    command = 'docker stack rm '
    if args.kubernetes:
        command += '--orchestrator=kubernetes '
    os.system(command + stack)
elif (not check_stack_running(stack)):
    # deploy composer file into swarm
    os.environ.update(get_variables())
    command = 'docker stack deploy --compose-file docker-compose.yml '
    if args.kubernetes:
        command += '--orchestrator=kubernetes '
    print(command + stack)
    os.system(command + stack)