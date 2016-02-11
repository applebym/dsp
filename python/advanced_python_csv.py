import csv
import advanced_python_regex as apr


def write_emails(list):
    with open('emails.csv', 'wb') as file:
        writer = csv.writer(file)
        for email in list:
            writer.writerow([email])

def main():
    data = apr.read_data('faculty.csv')
    email_list = apr.get_emails(data)
    write_emails(email_list)

if __name__ == '__main__':
    main()


