# Седьмая программа

import paramiko, time

host_ip = '10.31.70.209'
login = 'restapi'
password = 'j0sg1280-7@'

def net_com(sess, cmd, timeout=1):

    buf_size = 65536

    sess.send("\n")
    sess.recv(buf_size)
    if cmd[:-1] != "\n":
        cmd = cmd + "\n"
    sess.send(cmd)
    time.sleep(timeout)
    return sess.recv(buf_size).decode()

def dis_scroll(sess):
    return net_com(sess, 'terminal length 0')

ssh_connect = paramiko.SSHClient()
ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connect.connect(host_ip,
                    username=login,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)
sess = ssh_connect.invoke_shell()

dis_scroll(sess)
cmd_line = net_com(sess, 'show ip int brief', timeout=3).split('\n')

m = 0
for L in cmd_line:
    m += 1
    print(f"line {m} is {L}")

ssh_connect.close()