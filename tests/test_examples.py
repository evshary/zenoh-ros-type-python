import os
import signal
import subprocess
import sys
import time

import pytest


def run_process(cmd):
    env = os.environ.copy()
    env['PYTHONUNBUFFERED'] = '1'
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, preexec_fn=os.setsid, env=env)


def kill_process(proc):
    if proc.poll() is None:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        except OSError:
            pass


def wait_for_output(proc, pattern, timeout=20):
    start_time = time.time()
    output = ''
    while time.time() - start_time < timeout:
        line = proc.stdout.readline()
        if line:
            output += line
            if pattern in line:
                return True, output
        if proc.poll() is not None:
            break
        time.sleep(0.1)
    return False, output


@pytest.mark.timeout(30)
def test_pub_sub():
    listener = run_process([sys.executable, 'zenoh_ros_type/examples/listener.py'])
    time.sleep(2)  # Wait for listener to start
    talker = run_process([sys.executable, 'zenoh_ros_type/examples/talker.py'])

    try:
        success, output = wait_for_output(listener, 'Receive: Hello World')
        assert success, f'Listener did not receive data. Output: {output}'
    finally:
        kill_process(talker)
        kill_process(listener)


@pytest.mark.timeout(30)
def test_service():
    server = run_process([sys.executable, 'zenoh_ros_type/examples/service_server.py'])
    time.sleep(2)  # Wait for server to start
    client_proc = run_process([sys.executable, 'zenoh_ros_type/examples/service_client.py'])

    try:
        success, output = wait_for_output(client_proc, 'Get result: sum=3')
        assert success, f'Client did not get correct result. Output: {output}'
    finally:
        kill_process(client_proc)
        kill_process(server)


@pytest.mark.timeout(60)
def test_action():
    server = run_process([sys.executable, 'zenoh_ros_type/examples/action_server.py'])
    time.sleep(2)  # Wait for server to start
    client_proc = run_process([sys.executable, 'zenoh_ros_type/examples/action_client.py'])

    try:
        # Action client takes some time as it calculates Fibonacci
        # The pattern should match what's printed in action_client.py:
        # print(f'The result: {reply.status} {reply.sequence}')
        # Succeeded status is 4.
        success, output = wait_for_output(client_proc, 'The result: 4 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]', timeout=50)
        assert success, f'Action client did not get correct result. Output: {output}'
    finally:
        kill_process(client_proc)
        kill_process(server)
