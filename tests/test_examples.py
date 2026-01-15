import os
import signal
import subprocess
import sys
import time

import pytest


def run_process(cmd):
    env = os.environ.copy()
    env['PYTHONUNBUFFERED'] = '1'
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, preexec_fn=os.setsid, env=env)


def kill_process(proc):
    if proc.poll() is None:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        except OSError:
            pass


def collect_remaining_output(proc, timeout=1):
    """Collect any remaining output from a process."""
    output = ''
    start = time.time()
    while time.time() - start < timeout:
        line = proc.stdout.readline()
        if line:
            output += line
        else:
            break
    return output


def wait_for_output(proc, pattern, timeout=20):
    start_time = time.time()
    output = ''
    while time.time() - start_time < timeout:
        line = proc.stdout.readline()
        if line:
            output += line
            print(f'[DEBUG] {line.strip()}')  # Print for CI visibility
            if pattern in line:
                return True, output
        if proc.poll() is not None:
            # Process exited, collect any remaining output
            output += collect_remaining_output(proc)
            break
        time.sleep(0.1)
    return False, output


@pytest.mark.timeout(30)
def test_pub_sub():
    print('\n[TEST] Starting listener...')
    listener = run_process([sys.executable, 'zenoh_ros_type/examples/listener.py', '-l', 'tcp/127.0.0.1:7447', '--no-multicast-scouting'])
    time.sleep(3)  # Wait for listener to start and bind

    print('[TEST] Starting talker...')
    talker = run_process([sys.executable, 'zenoh_ros_type/examples/talker.py', '-e', 'tcp/127.0.0.1:7447', '--no-multicast-scouting'])

    try:
        success, output = wait_for_output(listener, 'Receive: Hello World')
        if not success:
            # Collect talker output too for debugging
            talker_output = collect_remaining_output(talker, timeout=2)
            print(f'[TEST] Talker output: {talker_output}')
        assert success, f'Listener did not receive data.\nListener output: {output}'
    finally:
        kill_process(talker)
        kill_process(listener)


@pytest.mark.timeout(30)
def test_service():
    print('\n[TEST] Starting service server...')
    server = run_process([sys.executable, 'zenoh_ros_type/examples/service_server.py', '-l', 'tcp/127.0.0.1:7448', '--no-multicast-scouting'])
    time.sleep(3)  # Wait for server to start and bind

    print('[TEST] Starting service client...')
    client_proc = run_process([sys.executable, 'zenoh_ros_type/examples/service_client.py', '-e', 'tcp/127.0.0.1:7448', '--no-multicast-scouting'])

    try:
        success, output = wait_for_output(client_proc, 'Get result: sum=3')
        if not success:
            # Collect server output too for debugging
            server_output = collect_remaining_output(server, timeout=2)
            print(f'[TEST] Server output: {server_output}')
        assert success, f'Client did not get correct result.\nClient output: {output}'
    finally:
        kill_process(client_proc)
        kill_process(server)


@pytest.mark.timeout(60)
def test_action():
    print('\n[TEST] Starting action server...')
    server = run_process([sys.executable, 'zenoh_ros_type/examples/action_server.py', '-l', 'tcp/127.0.0.1:7449', '--no-multicast-scouting'])
    time.sleep(3)  # Wait for server to start and bind

    print('[TEST] Starting action client...')
    client_proc = run_process([sys.executable, 'zenoh_ros_type/examples/action_client.py', '-e', 'tcp/127.0.0.1:7449', '--no-multicast-scouting'])

    try:
        # Action client takes some time as it calculates Fibonacci
        # The pattern should match what's printed in action_client.py:
        # print(f'The result: {reply.status} {reply.sequence}')
        # Succeeded status is 4.
        success, output = wait_for_output(client_proc, 'The result: 4 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]', timeout=50)
        if not success:
            # Collect server output too for debugging
            server_output = collect_remaining_output(server, timeout=2)
            print(f'[TEST] Server output: {server_output}')
        assert success, f'Action client did not get correct result.\nClient output: {output}'
    finally:
        kill_process(client_proc)
        kill_process(server)
