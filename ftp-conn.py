from ftplib import FTP_TLS
# FTPS server details
ftp_server = "************.cloud.ibm.com"
ftp_port = 990  # Example port number
ftp_username = "************"
ftp_password = "************"
try:

    ftp = FTP_TLS()
    ftp.connect(ftp_server, ftp_port)
    ftp.login(user=ftp_username, passwd=ftp_password)

    print("Connection successful! Connected with FTPS.")

    ftp.prot_p()
    

    remote_file_name = 'aa.txt'
    local_file_name = 'download.txt'
    
    with open(local_file_name, 'wb') as local_file:
        ftp.retrbinary('RETR ' + remote_file_name, local_file.write)
    print(f"File '{remote_file_name}' downloaded as '{local_file_name}'.")

    ftp.quit()
    print("FTPS connection closed.")
except Exception as e:
    print(f"FTPS connection error: {e}")