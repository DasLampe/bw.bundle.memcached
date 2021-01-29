global node

packages = {
    'memcached': {
        'installed': True,
        'tags': ['pkg_memcached', ]
    }
}

if node.os in node.OS_FAMILY_REDHAT or node.os == 'amazonlinux':
    pkg_yum = packages
if node.os in node.OS_FAMILY_DEBIAN:
    pkg_apt = packages

svc_systemd = {
    'memcached': {
        'running': True,
        'enabled': True,
        'needs': [
            'tag:pkg_memcached',
        ]
    },
}
