from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    if recv[:3] != '220':
        # print('220 reply not received from server.')
        pass

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        # print('250 reply not received from server.')
        pass
        

    # Send MAIL FROM command and print server response.
    MAILFROM = 'MAIL FROM: <test@client.net>\r\n'
    clientSocket.send(MAILFROM.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        #print('250 reply not received from server.')
        pass

    # Send RCPT TO command and print server response.
    RCPT = 'RCPT TO: <test@recipient.net>\r\n'
    clientSocket.send(RCPT.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
       # print('250 reply not received from server.')
       pass

    # Send DATA command and print server response.
    DATA = 'Message data\r\n'
    clientSocket.send(DATA.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
       # print('250 reply not received from server.')
        pass

    # Send message data.
    # msg_data = 'Date: Wed, 30 July 2019 06:04:34, From: test@client.net, Subject: How SMTP works, To: user@recipient.net, Body text\r\n'
    # msg_data = msg
    clientSocket.send(msg.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
       # print('250 reply not received from server.')
       pass

    # Message ends with a single period.
    # period = '\r\n.\r\n'
    clientSocket.send(endmsg.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        # print('250 reply not received from server.')
        pass

    # Send QUIT command and get server response.
    quit_command = 'QUIT\r\n'
    clientSocket.send(quit_command.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        # print('250 reply not received from server.')
        pass


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
