import pdfkit
import jinja2
import base64


def get_image_file_as_base64_data(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode()


def create_pdf(context):

    template_loader = jinja2.FileSystemLoader(".")
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template("./templates/basic-template.html")
    output_text = template.render(context, img_string=get_image_file_as_base64_data("./assets/images/logo.png"))

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    prefix = f'{context["surname"] if context["surname"] else ""}{"-" + context["name"][0] if context["name"] else ""}' \
             f'{"-" + context["patronymic"][0] if context["patronymic"] else ""}' \
             f'{"-" + context["birthday"] if len(context["birthday"]) > 2 else ""}'

    pdfkit.from_string(output_text, f"./pdfs/{prefix}.pdf", css="./assets/styles/style.css", configuration=config)
    pdfkit.from_string(output_text, f"./videos/{prefix}/{prefix}.pdf", css="./assets/styles/style.css",
                       configuration=config)

    print("PDF generated!")

    return True
