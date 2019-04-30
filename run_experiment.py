import sys
import os
import argparse


def execute(cmd):
    with os.popen(cmd) as f:
        ret = f.read()
    return ret


def command_ssh(user, dest, cmd):
    ssh_cmd = 'ssh -x %s@%s "%s"' % (user, dest, cmd)
    print("Command:", ssh_cmd)
    return execute(ssh_cmd)


def check_dep(user, dest, list_packages):
    needs_install = []
    for pkg in list_packages:
        print("Checking", pkg)
        cmd = 'apt -qq list %s' % pkg
        ret = command_ssh(user, dest, cmd)
        print("Return:", ret)
        if 'installed' not in ret:
            needs_install.append(pkg)
    return needs_install


def check_dep_ap(user, dest):
    needs_install = check_dep(user, dest,
                              list_packages=['hostapd', 'iw', 'wireless-tools']
                              )
    if len(needs_install) > 0:
        print('The following packages are needed:', ','.join(needs_install))
        sys.exit(0)  # quit program


def check_dep_sta(user, dest):
    needs_install = check_dep(user, dest,
                              list_packages=['wpasupplicant', 'firefox', 'git', 'nodejs', 'npm']
                              )
    if len(needs_install) > 0:
        print('The following packages are needed:', ','.join(needs_install))
        sys.exit(0)  # quit program


def copy_config_files_to_ap(user, dest, files_location='.', files_dest='coleta'):
    for file in ['hostapd.conf', 'hostapd.access']:
        origin = os.path.join(files_location, file)
        destination = os.path.join(files_dest, file)
        cmd = 'scp -x %s@%s %s %s' % (user, dest, origin, destination)
        print('copy', file, ':', cmd)
        command_ssh(user, dest, cmd)


def copy_config_files_to_sta(user, dest, files_location='.'):
    for file in ['wpa_supplicant.conf']:
        origin = os.path.join(files_location, file)
        destination = os.path.join(files_dest, file)
        cmd = 'scp -x %s@%s %s %s' % (user, dest, origin, destination)
        print('copy', file, ':', cmd)
        command_ssh(user, dest, cmd)


def install_server_js(user, dest):
    # download the server.js
    cmd = 'git clone https://github.com/h3dema/server.js'
    command_ssh(user, dest, cmd)
    cmd = 'cd server.js/server; npm install fs os express'
    command_ssh(user, dest, cmd)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', 'check if the dependencies are installed')
    parser.add_argument('--config', action='store_false', 'copy configuration to ap and station')
    parser.add_argument('--server-js', action='store_true', 'install the server.js files in the stations')

    parser.parse_args()

    aps = [{'user': 'winet', 'dest': 'gnu-nb3'},
           ]

    stas = [{'user': 'winet', 'dest': 'cloud'},
            {'user': 'winet', 'dest': 'storm'},
            ]

    if parser.check:
        # check if the dependencies are ok
        for ap in aps:
            check_dep_ap(ap['user'], ap['dest'])

        for sta in stas:
            check_dep_sta(sta['user'], ap['dest'])

    if parser.config:
        # copy the last configuration files
        for ap in aps:
            copy_config_files_to_ap(ap['user'], ap['dest'])

        for sta in stas:
            copy_config_files_to_sta(sta['user'], sta['dest'])

    if parser.server_js:
        for sta in stas:
            install_server_js(sta['user'], sta['dest'])

    # loop

    # station -run server.js
    cmd = "cd server.js/server; nohub nodejs server.js &"
