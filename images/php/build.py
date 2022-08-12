import argparse
import shlex
from subprocess import Popen, PIPE
import os,sys,inspect
from functools import reduce

sys.dont_write_bytecode=True
# load custom helpers module
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

from helpers import dot_env_vars

parser = argparse.ArgumentParser(description='Create image')
parser.add_argument('image')

parser.add_argument('-t', '--tag', action='append', help="build image with this tag as well")
parser.add_argument('-f', '--force', action='store_true', help="build image and replace it with if collision is found")
parser.add_argument('-p', '--push', action='store_true', help="Push to Docker Hub after image build")

args = parser.parse_args()

build_dir = os.path.join(current_dir, args.image)

if not os.path.exists(build_dir):
    print("Directory \"" + build_dir + "\" does not exist")
    sys.exit()

image = "besogon1/php"
tags = list(map(lambda tag: tag + "-fpm-alpine-ext",  [args.image, *(args.tag or [])]))

# check if image exists
def check_image_exists(image, tag='latest'):
    if len(tag) == 0:
        tag = 'latest'

    command = "docker images --format '{{.Repository}}' --filter=reference='" + image + ":" + tag + "'"
    out, err = Popen(shlex.split(command), stdout=PIPE, stderr=PIPE).communicate()

    return not err and not len(out.strip()) == 0

# Check image existence and remove if it exists in case 'force' parameter were passed
for tag in tags:
    if check_image_exists(image, tag=tag):
        if args.force:
            print("Remove image list")
            os.system("docker image rm " + image + ":" + tag)
        else:
            print("Images list:")
            os.system("docker images --filter=reference=\"" + image + ":" + tag + "\"")
            sys.exit()


build_cmd = "docker build --no-cache -t " + image + ":" + reduce(lambda tags_str, tag: tags_str + " -t " + image + ":" + tag, tags)

variables = dot_env_vars('.env')

for var in variables:
    build_cmd += " --build-arg " + var + "=" + variables[var]

build_cmd += " \"" + build_dir + "\""

print("Building image with command")
print(build_cmd)
os.system(build_cmd)

for tag in tags:
    if args.push:
        os.system("docker push " + image + ":" + tag)
    else:
        print("docker push " + image + ":" + tag)