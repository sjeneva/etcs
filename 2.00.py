import os

# List of filenames as a single string, each quoted and separated by commas
specific_numbers_str = '"112159","122158","300170","300577","300790","300983","301080","301219","301268","301312","301350","301439","301730","301952","302179","302188","302187","302189","302190","302191","302192","302193","302219","302285","302428","302503","302615","302625","302631","302714","302751","302792","302796","302806","302818","302889","302890","302891","302892","302893","302894","302895","302884","302885","302886","302887","302888","302896","302935","302947","302997","303079","303123","303132","303284","303448","303457","303688","304040","304285","304388","304416","304451","304499","304602","304927","305008","305050","305211","305391","305418","305437","305561","305604","305666","305695","305700","305765","305796","305827","305833","305840","305881","305942","305965","306150","306182","306193","306288","306346","306360","306369","306459","306491","306673","306873","307269","307479","307543","307595","307606","307638","307662","307708","307804","307865","308306","308528","308639","308879","308898","308998","309104","309197","309226","309227","309346","309407","309442","309640","309767","309794","309795","309796","309798","309799","309800","309802","309803","309804","309893","309899","309907","309933","309969","309981","310286","310309","310379","310398","310630","310876","310921","311234","311332","311342"'

# Split the string into individual numbers, remove quotes
specific_numbers = specific_numbers_str.replace('"', '').split(",")

# Convert the list of numbers into filenames with the specified pattern
filenames = [f"translated_article_{num.strip()}.txt" for num in specific_numbers]

def combine_specific_files(source_directory, output_file, filenames):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in filenames:
            filepath = os.path.join(source_directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read() + "\n\n")
                print(f"Successfully added {filename}")
            except FileNotFoundError:
                print(f"File not found: {filepath}")
            except Exception as e:
                print(f"Error reading file {filepath}: {e}")

    print(f"Combined specific files into '{output_file}'")

# Example usage with corrected output_file_path
source_directory_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\1.4_Korea_KLN_Translate'
output_file_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\combined_files.txt'
combine_specific_files(source_directory_path, output_file_path, filenames)

