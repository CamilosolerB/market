import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sendTo,idFactura):
    sender_email = 'tiendapacoterreros@gmail.com'
    password = 'Cc1070942659'
    subject = 'Facturacion No '+idFactura+' INVENTSOFT SAS'
    body = 'Por favor revise que la información registrada sea correcta en caso contrario comunicarse con soporte tecnico'
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = sendTo
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, sendTo, text)
    server.quit()
    
def json2xml(json_obj, line_padding=""):
    result_list = list()

    json_obj_type = type(json_obj)

    if json_obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json2xml(sub_elem, line_padding))

        return "\n".join(result_list)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append("%s<%s>" % (line_padding, tag_name))
            result_list.append(json2xml(sub_obj, "\t" + line_padding))
            result_list.append("%s</%s>" % (line_padding, tag_name))

        return "\n".join(result_list)

    return "%s%s" % (line_padding, json_obj)