# Reminder for Unread Notices
This is an application that sends an email to a list of registered users whenever a new notice is uploaded on NSUT IMS website. It is built using a python script that scrapes notices from IMS website and is deployed on an AWS backend. The mails are sent using SendGrid API and the script is scheduled to run daily with the help of cron job.

# Requirements
   - An AWS account
   - SendGrid API
   - Install Putty for SSH and Filezilla for FTP to your server instance

# Installations

    pip install pandas numpy sendgrid bs4 lxml xlrd --user 

    - Pandas and Numpy are modules to handle data
    - SendGrid is an API to send emails
    - bs4 or beautiful soup 4 is a package in python used to extract information from various data formats
    - lxml is a data format
    - xlrd is used to handle excel files (The attenders list is an excel file.)
    -  "--user" grants the privilege to make permanent changes to the server.
    
    The script is scheduled to run daily with the help of crontab.

