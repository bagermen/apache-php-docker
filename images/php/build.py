import argparse
import shlex
from subprocess import Popen, PIPE
import os,sys,inspect

# load custom helpers module
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)
import helpers

parser = argparse.ArgumentParser(description='Create image')
parser.add_argument('image')
parser.add_argument('-f', '--force', action='store_true', help="build image and replace it with if collision is found")
parser.add_argument('-p', '--push', action='store_true', help="Push to Docker Hub after image build")

args = parser.parse_args()
parts = args.image.split(':')

if len(parts) == 2:
    image = parts[0]
    tag = parts[1]
else:
    image = args.image
    tag = 'latest'

# check if image exists
def check_image_exists(image, tag='latest'):
    if len(tag) == 0:
        tag = 'latest'

    command = "docker images --format '{{.Repository}}' --filter=reference='" + image + ":" + tag + "'"
    out, err = Popen(shlex.split(command), stdout=PIPE, stderr=PIPE).communicate()

    return not err and not len(out.strip()) == 0

if check_image_exists(image, tag=tag):
    if args.force:
        print("Remove image list")
        os.system("docker image rm " + image + ":" + tag)
    else:
        print("Images list")
        os.system("docker images --filter=reference='" + image + ":" + tag + "'")
        sys.exit()

build_cmd = "docker build -t " + image + ":" + tag
variables = helpers.dot_env_vars('.env')

for var in variables:
    build_cmd += " --build-arg " + var + "=" + variables[var]

build_cmd += " ."

print("Build image")
os.system(build_cmd)

if args.force:
    os.system("docker push " + image + ":" + tag)
else:
    print("docker push " + image + ":" + tag)