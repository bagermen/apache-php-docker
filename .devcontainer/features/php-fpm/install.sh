#!/usr/bin/env bash
set -e

if [ "$(id -u)" -ne 0 ]; then
    echo -e 'Script must be run as root. Use sudo, su, or add "USER root" to your Dockerfile before running this script.'
    exit 1
fi

# Write out a scripts that can be referenced as an ENTRYPOINT to auto-start sshd and fix login environments
tee /usr/local/share/php-fpm-init.sh > /dev/null \
<< 'EOF'
#!/usr/bin/env bash
# This script is intended to be run as root with a container that runs as root (even if you connect with a different user)
# However, it supports running as a user other than root if passwordless sudo is configured for that same user.

set -e 

sudoIf()
{
    if [ "$(id -u)" -ne 0 ]; then
        sudo "$@"
    else
        "$@"
    fi
}

EOF
tee -a /usr/local/share/php-fpm-init.sh > /dev/null \
<< 'EOF'

# ** Start SSH server **
sudoIf docker-php-entrypoint php-fpm 2>&1 | sudoIf tee /tmp/php-fpm.log > /dev/null

set +e
exec "$@"
EOF
chmod +x /usr/local/share/php-fpm-init.sh