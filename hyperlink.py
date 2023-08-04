from bs4 import BeautifulSoup
import csv
import os

def populate_html_with_csv(html_template, css_file, csv_file, output_folder):
    # Read the CSS content
    with open(css_file, 'r') as css_file:
        css_content = css_file.read()

    # Read the CSV data
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Parse the HTML template
    with open(html_template, 'r') as file:
        soup = BeautifulSoup(file, 'lxml')

    for idx, row in enumerate(data):
        # Find divs with matching ids and populate them with data
        for key, value in row.items():
            div = soup.find('div', {'id': key})
            if div:
                div.string = value

        # Add the CSS content to the head tag
        style_tag = soup.new_tag('style')
        style_tag.string = css_content
        head_tag = soup.find('head')
        if head_tag:
            head_tag.append(style_tag)

        # Write the populated data to the output HTML file
        output_file = f'{output_folder}/output_{idx + 1}.html'
        with open(output_file, 'w') as file:
            file.write(str(soup))

        print(f'{output_file} has been created with data from row {idx + 1}.')

if __name__ == '__main__':
    html_template = 'index.html'
    css_file = 'style.css'
    csv_file = 'data.csv'
    output_folder = 'output'  # Create this folder before running the script

    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    populate_html_with_csv(html_template, css_file, csv_file, output_folder)











