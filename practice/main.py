import os
import csv
import glob
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from pandas.io.excel import ExcelWriter
import pandas
from jinja2 import Environment, FileSystemLoader

SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT = 587
FROM_ADDR = '61966225@qq.com'
PASSWORD = 'qxqvbhtctbutbgfg'
TO_ADDRS = ['61966225@qq.com']


def gen_msg(content, subject, attachments, nick_from=None, nick_to='测试组'):
    if nick_from is None:
        nick_from = FROM_ADDR

    msg = MIMEMultipart()
    msg['from'] = nick_from
    msg['to'] = nick_to
    msg['subject'] = Header(subject)
    msg.attach(MIMEText(content, 'html', 'utf-8'))

    for attachment in attachments:
        with open(attachment, 'rb') as f:
            attach = MIMEText(f.read(), 'base64', 'utf-8')
        attach['Content-Type'] = 'application/octet-stream'
        attach['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'  # noqa
        msg.attach(attach)
    return msg


def send_mail(content, subject, attachments, nick_from=None):
    msg = gen_msg(content, subject, attachments, nick_from)
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(FROM_ADDR, PASSWORD)
    server.sendmail(FROM_ADDR, TO_ADDRS, msg.as_string())
    server.quit()


def jinja2_render(data, tmpl_file, directories):
    env = Environment(loader=FileSystemLoader(directories))
    template = env.get_template(tmpl_file)
    return template.render(data)


def main(path):
    csv_files = glob.glob('/Users/dongweiming/PycharmProjects/mysql_project/*.csv')[:1]
    with ExcelWriter(path) as ew:
        for csv_file in csv_files:
            pandas.read_csv(csv_file).to_excel(ew, sheet_name=os.path.basename(csv_file))

    here = os.path.abspath(os.path.dirname(__file__))
    directories = [os.path.join(here, 'tmpl')]

    with open(csv_files[0]) as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = {'headers': headers, 'rows_data': reader}
        content = jinja2_render(data, 'data.jinja2', directories)
    send_mail(content, '测试', [path], nick_from='爱湃森')
    print('Send success!')


if __name__ == '__main__':
    main('my_excel.xlsx')