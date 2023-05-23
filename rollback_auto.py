def process_file(filename, output_file):
    with open(filename) as file:
        data = [line.strip() for line in file]

    with open(output_file, 'a') as output:  # Open the file in append mode ('a')
        for line in data:
            if 'ADD' in line:
                print(line.replace('ADD', 'RMV'), file=output)
            elif 'RMV' in line:
                print(line.replace('RMV', 'ADD'), file=output)
            elif 'MOD' in line:
                continue
            else:
                print(line, file=output)


def process_additional_data(filename, output_file, condition):
    with open(filename) as file, open(output_file, 'a') as tulis:
        data = [line.strip() for line in file]
        for line in data:
            if condition in line:
                if ',OBJECTATTRIBUTE' in line:
                    print(line.split(',OBJECTATTRIBUTE')[0].replace('ADD', 'RMV') + ';', file=tulis)
                elif 'ADD CONDITIONGROUP:CONDITIONGROUPNAME="CG_' in line:
                    print(line.replace('ADD', 'RMV') + ';', file=tulis)                

# Process '03_FILE_CONF_XXX_XXX.txt'
process_file('03_FILE_CONF_XXX_XXX.txt', 'TEST_OLD_ROLLBACK_03.txt')

# Process '02_NEW_QUOTA.txt'
process_file('02_NEW_QUOTA.txt', 'TEST_OLD_ROLLBACK_03.txt')


process_additional_data('00_CG_GEN_AOs.txt', 'TEST_OLD_ROLLBACK_03.txt', ',OBJECTATTRIBUTE')
process_additional_data('00_CG_GEN_AOs.txt', 'TEST_OLD_ROLLBACK_03.txt', 'ADD CONDITIONGROUP:CONDITIONGROUPNAME="CG_')
